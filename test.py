import sys
#In ra toàn bộ thông số dòng lệnh 
print("Danh sách tham số:",sys.argv)
#Nếu có tham số in từng cái
if len(sys.argv)>1:
    print("Tham số 1:",sys.argv[1])
if len(sys.argv)>2:
    print("Tham số 2:",sys.argv[2])
if len(sys.argv)>3:
    print("Tham số 3:",sys.argv[3])