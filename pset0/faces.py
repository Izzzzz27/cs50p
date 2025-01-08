def main():
    fun=input()
    f=convert(fun)
    print(f)
def convert(text):
    text = text.replace(":)" ,"🙂")
    text = text.replace (":(", "🙁")
    return text

main()
