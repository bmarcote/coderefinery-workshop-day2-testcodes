import argparse

def dog_speak(msg):
  return f"bark bark, {msg}" 

def main():
    parser = argparse.ArgumentParser(description="Print custom message on the screen')
    parser.add_argument("--message", "-m", help="Enter a message that will be printed on the screen")
    args = parser.parse_args()

    dog_speak(args.message)



if __name__ == "__main__":
    main()




