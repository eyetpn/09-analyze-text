# Remember to reach out for help after your own due diligence

def analyze_text(text):
    total_char = len(text)
    num_e = 0
    mystr = "e"
    for char in text:
        if char == "e" or "E":
            num_e +=1
    percent = num_e/total_char *100
    print ("The text contains", total_char,"alphabetic characters, of which", num_e,"(",percent, "%) are 'e'.")
    return  
