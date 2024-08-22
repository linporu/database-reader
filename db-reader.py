import pandas as pd
import sqlite3
import os

# 定義資料庫檔案名稱
DB_NAME = 'data.db'

def main():

    # 讀取 CSV 檔案並存入資料庫
    read_csv_to_db('myab.csv')  # 請替換成您的 CSV 檔案路徑
    
    # 執行 SQLite3 指令
    while True:
        sql_command = input("SQL command: ")
        result = execute_sql_command(sql_command)
        if result == None:
            print("退出 sqlite3 模式")
            break
        else:
            print(result)
    
    # 輸出資料到 CSV 檔案
    export_to_csv('db_output.csv')


def read_csv_to_db(csv_file):
    """讀取 CSV 檔案並存入 SQLite 資料庫"""
    conn = None  # 初始化 conn 變數
    try:
        # 讀取 CSV 檔案，指定編碼為 big5
        print("讀取中...")
        df = pd.read_csv(csv_file, encoding='big5')  # 使用 big5 編碼讀取
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


def execute_sql_command(command):
    """執行 SQLite 指令並回傳結果"""
    if command.strip().lower() in ['.exit', '.quit']:  # 處理 .exit 和 .quit 指令
        print("退出程式。")
        return None  # 返回 None 以指示退出

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        # 處理特殊指令
        if command.strip().lower() == '.table':
            return cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        elif command.strip().lower() == '.schema':
            return cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';").fetchall()
        
        cursor.execute(command)
        # 如果是查詢指令，回傳結果
        if command.strip().lower().startswith(('select', 'pragma')):
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
        df.to_csv(output_file, index=False, encoding='big5')  # 使用 big5 編碼輸出
        print(f"資料已成功輸出到 {output_file}。")
    except Exception as e:
        print(f"輸出 CSV 時發生錯誤: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()