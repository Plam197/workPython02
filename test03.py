#รับค่า/ป้อนทางแป้นพิมพ์ ใช้ฟังชั่น input() โดยสิ่งที่ป้อนทั้งหมดคือs String
#ตัวแปร variable เป็น indentifier มีหน้าที่เก็บข้อมมูลที่เกิดขึ้นในโปรแกรม ข้อมมูลที่เก้บจะอยู่ใน Ram
# indentifier คือชื่อที่ Dev . ตั้งขึ้นมาเอง ต้องเป็นไปตามกฏการตั้งช่องของภาษานั้นๆ

std_id = input('รหัสนักศึษา :')
std_name = input('ชื่อนักศึกษา : ')
stdYearBorn = input('ปีเกิด : ')
print("..................")
stdAge = 2023 - int(stdYearBorn) #ต้องแปลง Strinf เป็น Nomber -> int(),float()
print(f'ยินดีตอนรับ {std_id} ชื่อ {std_name}')
print(f'คูณเกิดปี {stdYearBorn} อายู {stdAge}')
print("..................")
print('ยินดีตอนรับ '+std_id+  "ชื่อ " +std_name)
print('คูณเกิดปี ' +stdYearBorn+ 'อายู ' +str(stdAge))
print("..................")
print('ยินดีตอนรับ' ,std_id,  "ชื่อ" ,std_name, )
print('คูณเกิดปี' ,stdYearBorn, 'อายู' ,stdAge,)
print("..................")
print('ยินดีตอนรับ {} ชื่อ {}'.format(std_id,std_name))
print('คูณเกิดปี {} อายู {}'.format(stdYearBorn,stdAge))
print("..................")
print('ยินดีตอนรับ %s ชื่อ %s'%(std_id,std_name))
print('คูณเกิดปี %s อายู %d'%(stdYearBorn,stdAge))