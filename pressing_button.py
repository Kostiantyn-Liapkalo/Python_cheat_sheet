'''
The sequence_buttons function shows the sequence of buttons that must be pressed 
in order for the text entered by the user to appear on the phone screen.
'''


string = 'Hi there!'

def sequence_buttons(string):
    
    buttons = {
        1: ".,?!:",
        2: "ABC",
        3: "DEF",
        4: "GHI",
        5: "JKL",
        6: "MNO",
        7: "PQRS",
        8: "TUV",
        9: "WXYZ",
        0: " "
    }
    
    fin_str = ""

    for ch in string.upper():
        for key, value in buttons.items():
            if ch in value:
                fin_str += str(key) * (value.find(ch) + 1)
                
    return fin_str


if __name__ == "__main__":
    print(sequence_buttons(string))
