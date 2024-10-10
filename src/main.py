from components import parse_model, Establishment

def main():
    """
    Main function that loads the establishments from a CSV file and prints them.
    """
    try:
        # Parse the CSV file into Establishment objects
        establishments = parse_model('../data_sources/establishments.csv', Establishment)
        
        # Display the parsed establishments
        establishments_list = list(map(str, establishments))
        for e_ in establishments_list:
            print(e_)
        #print('Establishments:', list(map(str, establishments)))
    
    except FileNotFoundError:
        print("Error: The specified file '../resources/establishments.csv' could not be found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
