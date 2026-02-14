time = int(input("enter total seconds: "))
hr = time//3600
rem_sec = time%3600
min = rem_sec//60
sec= rem_sec%60
print(hr,"hours",min,"minutes",sec,"seconds")