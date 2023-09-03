import pyshorteners

def shorten_url(url):
    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        return shortened_url
    except pyshorteners.exceptions.ShorteningErrorException:
        return "Error: Could not shorten the URL."

if __name__ == "__main__":
    long_url = input("Enter the URL you want to Shorten: ")
    shortened_url = shorten_url(long_url)
    print("Shortened URL:", shortened_url)

#www.linkedin.com/in/madhur-gupta-b2b84a202