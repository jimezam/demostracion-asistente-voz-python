import assistant

def main():
    assistant.speak("Marco")
    listened = assistant.listen()
    print(f">> {listened}")

    if(listened == "Polo"):
        assistant.speak("Excelente")
    else:
        assistant.speak("Muy mal")

if __name__ == "__main__":
    main()
