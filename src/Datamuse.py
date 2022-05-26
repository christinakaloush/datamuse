import requests
import json

class Datamuse:

    def __init__(self):
        self.user_list = []
        self.user_defs = []
        self.user_input = input('Enter a word: ')
        self.num_of_output = int(input('Enter the number of examples you would like: '))
        self.url = f"https://api.datamuse.com/words?sp={self.user_input}&max={self.num_of_output}&md=d"

    def jprint(self, obj):  # create a formatted string of python JSON object
        text = json.dumps(obj, sort_keys = True, indent = 4)
        print(text)
        
    def format_words(self): # create a formatted string of user's word results
        unique_list = list(set(self.user_list))
        final_string_words = ", "
        print(f"\nYour results: {final_string_words.join(unique_list)}\n")

    def format_defs(self): #create a formatted string of the user's definition results
        unique_defs = self.user_defs
        final_string_defs = ","
        for x in range(len(unique_defs)):
            print(f"Your definition(s), respectively: {unique_defs[x]}\n")

    def generate_words(self): 
        while True:
            response = requests.get(self.url)
            self.jprint(response.json())
            data_list = response.json()
            if len(data_list) == 0:
                print("Sorry, no words or definitions associated with your entry.")
                break
            else:
                for x in range(len(data_list)):
                    my_dictionary = data_list[x]
                    self.user_list.append(my_dictionary['word'])
                    if 'defs' in my_dictionary:
                        self.user_defs.append(my_dictionary['defs'])
                    else:
                        self.user_defs.append("Sorry, no definitions have been provided for this word.")
                final_output_words = self.format_words()
                final_output_defs = self.format_defs()
                break
        

        

        
