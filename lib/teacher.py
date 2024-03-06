#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Mathematics", "Science", "History"]

    def teach(self):
        if self.knowledge:
            topic_to_teach = random.choice(self.knowledge)
            return f"{self.first_name} is teaching {topic_to_teach}."
        else:
            return f"{self.first_name} doesn't have any knowledge to teach."
