# url gen
def urlgen():
  brand = input("brand: ")
  brand = brand.replace(" ", "-")
  brand = brand.lower()
  code = input("product code: ")
  size = int(input("size: "))
  while size.isdigit() == False:
   size = int(input("size: ")) 
  url = "https://www.adidas.co.uk/" + brand + "-shoes/" + code + ".html?forceSelSize=" + code + "_" + str(460 + (size * 20))
  print(url)

urlgen()