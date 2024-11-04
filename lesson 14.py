class Criminal:
    def  __init__(self, name,id_num, crime,gender):
        self.name=name
        self.id_num=id_num
        self.crime=crime
        self.gender=gender

    def show_details(self):
        print(f"Name:{self.name}\n Id number:{self.id_num}\n Crime:{self.crime}\n Gender:{self.gender}")

c1=Criminal("Awilo Longomba","345670","Theft","Male")
c1.show_details()