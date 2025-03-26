from Crypto.Hash import SHA3_256

def sha3(message):
    hash = SHA3_256.new()
    hash.update(message) 
    return hash.hexdigest() 

def main():
    text = input("Nhập chuỗi cần băm: ") 
    text_bytes = text.encode('utf-8')  
    hashed_text = sha3(text_bytes) 

    print("Chuỗi văn bản đã nhập: ", text)
    print("SHA-3 Hash:", hashed_text)  

if __name__ == "__main__":
    main()