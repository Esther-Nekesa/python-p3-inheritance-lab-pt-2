# lib/student.py

class Student:
    def hello(self):
        # Base implementation for the greeting
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        # Base implementation for raising a hand
        print("Pick me!")

# lib/chattystudent.py

from student import Student # Absolute import (assuming 'student.py' is accessible)

class ChattyStudent(Student):
    
    # 1. Augmenting the hello() method
    def hello(self):
        # Call the parent's hello() method (prints "Hey there...")
        super().hello()
        
        # Then, add the chatty elaboration
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    # 2. Augmenting the raise_hand() method (calling super ten times)
    def raise_hand(self):
        # Use a loop to call the parent's raise_hand() method ten times.
        # This prints "Pick me!" ten times.
        for _ in range(10):
            super().raise_hand()
    
    pass
