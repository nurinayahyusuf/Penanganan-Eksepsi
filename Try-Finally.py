def main():
   try:
      f = open("data.txt", "r")
      
      try:
         f.write("Pemrograman Python")
      finally:
         f.close()
   except IOError:
       print("\nERROR: File tidak dapat" + " dibuka/ditulis")
       
if __name__ == "__main__":
   main()
