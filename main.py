import application


application = application.Application()

app = 1

while app == 1:
    question = input(">> ")

    if question != "quit":
        answer = application.generate_text(question)
        print(answer)
        continue

    else:
        app = 0
