import re

def extract_error_messages():
  # Read the log file and extract lines matching the pattern   
  pattern = r"Error downloading (.*?): An error occurred \(404\)"
  
  try:
    with open('/home/venkat/log_file.txt', 'r') as input_file:
      with open('/home/venkat/log_file_output.txt', 'w') as output_file:
        for line in input_file:
          match = re.search(pattern, line)
          if match:
            extracted_text = match.group(1)
            output_file.write(extracted_text + '\n')
            
  except FileNotFoundError:
    print("Input file not found!")
  except Exception as e:
    print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
  extract_error_messages()