from wheather_app import WheatherApp


def main():
    app = WheatherApp()
    app.load_cities()

    while True:
        app.show()
        print("\n[a] add city   [r] remove city   [q] quit")
        choice = input("> ").strip().lower()

        if choice == "a":
            name = input("City name: ").strip()
            try:
                app.add_city(name)
            except ValueError as e:
                print(f"❌ {e} — give me a real city, boy 😎")
        elif choice == "r":
            index = int(input("🗑️  index to remove: "))
            app.remove_city(index)
        elif choice == "q":
            print("Bye! 👋")
            break
        else:
            print("Unknown option, try again.")


if __name__ == "__main__":
    main()