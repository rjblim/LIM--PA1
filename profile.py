class StudentProfile:
    def __init__(self):
        self.name = "Rose"
        self.age = "14"
        self.favorite = "pink"
        self.hobbies = ["listening to music"]

    def display_profile(self):
        print("===== STUDENT PROFILE =====")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Favorite:", self.favorite)
        print("Hobbies:", ", ".join(self.hobbies))