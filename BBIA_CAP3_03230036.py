#It reads the input.txt file.
def read_input(file_input):
  total_sum = 0
  digits=[]

  try:
    with open(file_input,'r') as file:
      for line in file:
        line = line.strip('\n')
        
        for char in line:
          if char.isdigit():
            digits.append(char)
      
        if len(digits) >= 2:
          first_digit = digits[0]
          last_digit = digits[-1]

          two_digit_number=int(first_digit + last_digit)
          total_sum +=  two_digit_number
      return total_sum
  except FileNotFoundError:
    print(f"Error: File '{file_input}' not found.")

  

def print_solution(total_sum):
  total_sum = read_input(file_path)
  print(f"The total sum from the given input file '{file_path}' is: {total_sum}.")

file_path = r'C:\Users\lenovo\Desktop\03230036_BIA101_CAPIII\03230036_BIA101_CAP3\036.txt'

print_solution(file_path) # it prints the solution.