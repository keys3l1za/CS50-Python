def gqa(answer):
    return answer.strip().lower() in ['42', 'forty-two', 'forty two']

def main():
    u_answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    if gqa(u_answer):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
