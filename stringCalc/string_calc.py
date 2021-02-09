import re

def add(numbers: str) -> int:
    
    delimiter_regex = re.compile("^(\D)*\n(.+)", re.MULTILINE | re.DOTALL)
    delimiter_match = delimiter_regex.match(numbers)
    delimiter = "," # default
    
    if delimiter_match:
        delimiter = delimiter_match.group(1)
        numbers = delimiter_match.group(2)           
    
    if(delimiter and delimiter.strip()): 
        numbers = numbers.strip() #removes trailing/leading spaces
            
    if "\n" not in delimiter:
        numbers = numbers.replace("\n", "") #removes new lines    
    
    if numbers:         
        numbers_list = numbers.split(delimiter)                
        result = 0        
        converted_list = [int(x) for x in numbers_list]
        filtered_list = [number for number in converted_list if number <= 1000] #numbers <= 1000
        negative_numbers_list = [number for number in filtered_list if number < 0] 
        if len(negative_numbers_list) > 0:
            raise Exception("Negatives not allowed. {}".format(negative_numbers_list) )
        result = sum(filtered_list)                            
        return result
    else:
        return 0
