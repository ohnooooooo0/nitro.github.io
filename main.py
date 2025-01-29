import random
import string
import time
import requests
import os

def generate_random_code(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def check_nitro_link(url):

    code = url.split('/')[-1]
    api_url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return "有効"
        else:
            return "無効"
    except requests.exceptions.RequestException:
        return "無効"

def main():
    PURPLE = '\033[35m'    
    GREEN = '\033[32m'
    END = '\033[0m'

    print(GREEN + "-----------------------------------------------------------------------------------" + END)
    print("\n")
    print(PURPLE +"""
     _   _ _ _                           
    | \ | (_) |  ___      　           
    |  \| |_| |_/  _\__       
    | . ` | | __| /  _ \  
    | |\  | | | | | |_| |   
    |_| \_|_|\__|_|\___/      
   """ + END)
    print("\n")
    print(GREEN + "-----------------------------------------------------------------------------------" + END)
    print(GREEN + "-=================================================================================-" + END)
    print("\n")
    print(GREEN + "[1] リンクの作成 \n[2] コードチェック \n[3] ツールの終了" + END)
    print("\n")
    print(GREEN + "-----------------------------------------------------------------------------------" + END)
    print("\n")

    while True:
        try:
            print("\n")
            choice = int(input(GREEN + "選択肢の数値を入力してください: "))
            if choice == 1:
                num_codes = int(input("生成するコードの数を入力してください: "))
                interval = float(input("生成する間隔（秒単位）を入力してください（0から10の範囲 推奨 : 0）: "))

                if interval < 0 or interval > 10:
                    print("間隔は0から10の範囲で入力してください。(通信速度により、生成が遅れる場合があります。)")
                    continue

                code_length = 16  
                generate_and_check_codes(num_codes, code_length, interval)


            elif choice == 3:
                print("終了します。")
                break
            else:
                print("無効な選択です。もう一度入力してください。")
        except ValueError:
            print("無効な入力です。整数を入力してください。")

if __name__ == "__main__":
    main()
