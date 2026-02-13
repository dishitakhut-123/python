def extract_usernames(emails, allowed_domains):
    valid_usernames = []

    for email in emails:

        parts = email.split("@")
        
        if len(parts) == 2:
            username, domain = parts
            
            if domain in allowed_domains:
                valid_usernames.append(username)

    return valid_usernames


def main():
    emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
    allowed_domains = {"gmail.com"}

    result = extract_usernames(emails, allowed_domains)
    print(result)


if __name__ == "__main__":
    main()
