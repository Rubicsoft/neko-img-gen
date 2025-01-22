"""
Code by Reymo Je

Library used nekos.py
"""

import nekos


# Function to generate neko images
def generate_img(prompt: str, amount: int, desc: bool = True) -> str:
    links: str = ""
    if desc:
        print("Generating links...")
    
    # Generate each links
    for i in range(1, amount + 1, 1):
        if desc:
            links += str(i) + ". NEKO IMAGE : " + nekos.img(prompt) + "\n"
        else:
            links += nekos.img(prompt) + "\n"
    
    return links


def main() -> None:
    while True:
        # User input
        prompt: str = input("Prompt : ")
        amount: int = int(input("Amount of images : "))
        print("")

        # Generate images
        print(generate_img(prompt, amount))

        # Ask for running again
        run_again: str = input("Continue? (y/n)\n> ")
        match run_again:
            case 'y':
                print("")
                continue
            case 'n':
                break
        
    print("\nNYAAA :3\n")


if __name__ == "__main__":
    main()
