#Simple license verification based on early 90s software


def is_valid_license_key(key: str) -> bool:
    if len(key) != 9 or not key.isdigit():
        return False
    
    return int(key) % 7 == 0

def main():
    print("=== Welcome to FictionalSoft Activation ===")

    while True:
        license_key = input("Please enter your 9-digit license key: ")

        if is_valid_license_key(license_key):
            print("✅ License key is valid. Thank you for activating!")
            break
        else:
            print("❌ Invalid license key. Please try again.\n")

if __name__ == "__main__":
    main()
