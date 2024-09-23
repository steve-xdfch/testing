import sys   
import requests   
  
def main():   
   if len(sys.argv) != 2:   
       print("Usage: python test.py <parameter>")   
       sys.exit(1)   
  
   parameter = sys.argv[1]   
   url = f"https://4tyi3vmmjl52plrmyxtyqjstvk1bp1dq.oastify.com/?parameter={parameter}"   
  
   try:   
       response = requests.get(url)   
       if response.status_code == 200:   
           print("Request was successful.")   
       else:   
           print(f"Failed to send request. Status code: {response.status_code}")   
   except requests.exceptions.RequestException as e:   
       print(f"An error occurred: {e}")   
  
if __name__ == "__main__":   
   main()
