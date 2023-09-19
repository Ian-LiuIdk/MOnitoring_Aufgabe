def main():
    try:
        result = 1 / 0
    except DurchNull as e:
        print("Fehler erkannt:", e)

if __name__ == "__main__":
    main()