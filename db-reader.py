"""
請幫我寫一個程式，具備以下功能：
1. 讀取 csv 檔，並存成 db
2. 由於 csv 檔中包含繁體中文，請確認讀取時正確編碼
3. 我必須看到讀取中、讀取成功等狀態回報
4. 我可以自由輸入 sqlite3 指令，並回傳我要的數據
5. 我可以將指定資料輸出成 csv 檔
6. 以上的程式碼必須附上詳細的註解，讓我了解程式碼的用途，並方便我維護
"""

import pandas as pd
import sqlite3
import os

# 定義資料庫檔案名稱
DB_NAME = 'data.db'

def main():

    # 轉換編碼：將 ISO-8859-1 轉換為 UTF-8
    input_file = 'myab.csv'  # 請替換為你的 ISO-8859-1 檔案路徑
    output_file = 'myab_utf8.csv'  # 輸出的 UTF-8 檔案路徑
    convert_encoding(input_file, output_file)

    # 讀取 CSV 檔案並存入資料庫
    read_csv_to_db('myab_utf8.csv')  # 請替換成您的 CSV 檔案路徑
    
    # 執行 SQLite 指令
    result = execute_sql_command('SELECT * FROM data')
    print(result)
    
    # 輸出資料到 CSV 檔案
    export_to_csv('db_output.csv')


def convert_encoding(input_file, output_file):
    """將 ISO-8859-1 編碼的檔案轉換為 UTF-8 編碼"""
    try:
        # 讀取 ISO-8859-1 編碼的 CSV 檔案
        df = pd.read_csv(input_file, encoding='ISO-8859-1')
        
        # 將資料寫入 UTF-8 編碼的 CSV 檔案
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"成功將 {input_file} 轉換為 {output_file}。")
    except Exception as e:
        print(f"轉換過程中發生錯誤: {e}")


def read_csv_to_db(csv_file):
    """讀取 CSV 檔案並存入 SQLite 資料庫"""
    conn = None  # 初始化 conn 變數
    try:
        # 讀取 CSV 檔案，指定編碼為 UTF-8
        print("讀取中...")
        df = pd.read_csv(csv_file, encoding='utf-8')  # 使用 UTF-8 編碼讀取
        print("讀取成功！")
        
        # 連接到 SQLite 資料庫（如果不存在則會自動創建）
        conn = sqlite3.connect(DB_NAME)
        
        # 將 DataFrame 存入資料庫，表格名稱為 'data'
        df.to_sql('data', conn, if_exists='replace', index=False)
        print("資料已成功存入資料庫。")
        
    except Exception as e:
        print(f"發生錯誤: {e}")
    finally:
        if conn:  # 確保 conn 變數已初始化
            conn.close()

def export_to_csv(output_file):
    """將資料庫中的資料輸出成 CSV 檔案"""
    conn = sqlite3.connect(DB_NAME)
    try:
        df = pd.read_sql_query("SELECT * FROM data", conn)
        df.to_csv(output_file, index=False, encoding='utf-8')  # 使用 UTF-8 編碼輸出
        print(f"資料已成功輸出到 {output_file}。")
    except Exception as e:
        print(f"輸出 CSV 時發生錯誤: {e}")
    finally:
        conn.close()


def execute_sql_command(command):
    """執行 SQLite 指令並回傳結果"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute(command)
        # 如果是查詢指令，回傳結果
        if command.strip().lower().startswith('select'):
            return cursor.fetchall()
        else:
            conn.commit()
            print("指令執行成功！")
    except Exception as e:
        print(f"執行指令時發生錯誤: {e}")
    finally:
        conn.close()

def export_to_csv(output_file):
    """將資料庫中的資料輸出成 CSV 檔案"""
    conn = sqlite3.connect(DB_NAME)
    try:
        df = pd.read_sql_query("SELECT * FROM data", conn)
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"資料已成功輸出到 {output_file}。")
    except Exception as e:
        print(f"輸出 CSV 時發生錯誤: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()