from Prac07.programminglanguage import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    print(ruby)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    print(python)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(vb,"\n")

    languages = [ruby, python, vb]

    print("The dynamically typed languages are:")

    for row in languages:
        if row.is_dynamic():
            print(row.name)


main()