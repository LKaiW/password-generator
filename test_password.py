from main import generate_password

def test_default_length():
    pw = generate_password()
    assert len(pw) == 12

def test_custom_length():
    pw = generate_password(20)
    assert len(pw) == 20

def test_content():
    pw = generate_password(30)
    # 至少有一個字母或數字
    assert any(c.isalpha() for c in pw)
    assert any(c.isdigit() or c in "!@#$%^&*()" for c in pw)

def test_fail_example():
    pw = generate_password()
    assert len(pw) == 5, "這個測試一定會失敗"
