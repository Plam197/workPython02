#1. ใช้ ,
print("hello...",456,'hi...',True,10+20,"hey...")
#2. ใช้ + มีข้อแม้ว่าทุกตัวที่เอามาต่อกันต้องเป้น String 
print("hello..."+str(456)+'hi...'+str(True)+' '+str(20+10)+"hey...")
#3. ใช้เมธอด Format 
print('hello{}hi...{} {} hey...' .format(456,True,10+20))
print('hello{0}hi...{1} {2} hey...' .format(456,True,10+20)) #index number ตำแหน่งข้อมูลในปีกกา
#4. ใช้ f-string
print(f"hello...{456} hi...{True} {10+20} hey...")
#5. ใช้ modular operator (%) -> %d, %f, %c, %s,...
print('hello... %d hi... %s %d hey...' %(456,True,10+20))