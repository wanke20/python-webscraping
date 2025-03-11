from bs4 import BeautifulSoup

def extract_content(html):
    soup = BeautifulSoup(html, "html.parser")
    outerbox = soup.find("div", id="outerbox")

    if not outerbox:
        print("Target div not found")
        return {}

    content_dict = {}
    current_title = None

    for element in outerbox.find_all(["h2", "p", "ul", "li"], recursive=True):
        if element.name == "h2":
            current_title = element.get_text(strip=True)
            content_dict[current_title] = []
        elif current_title:
            if element.name == "ul":
                content_dict[current_title].extend(
                    [li.get_text(strip=True) for li in element.find_all("li")]
                )
            else:
                content_dict[current_title].append(element.get_text(strip=True))

    return content_dict
