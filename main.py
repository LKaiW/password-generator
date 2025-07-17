import random
import string
# 測試 GitHub Actions 是否被觸發了
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    pw = generate_password()
    print("你的隨機密碼是：", pw)
