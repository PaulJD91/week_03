class Account:

    def __init__(self, username, dob):
        self.username = username
        self.dob = dob
        self.followers = []
        self.likes = []
        self.posts = []

    def follow(self, account_to_follow):
        self.followers.append(account_to_follow)

    def follows_me(self, account_to_check):
        for account in account_to_check.followers:
            if account is self:
                return True
            
    def add_post(self, post):
        self.post.append(post)
            
class Post:
    def __init__(self, content, date):
        self.content = content
        self.date = date

post1= Post("Jasons cool lesson", "18/07/2023")


account1 = Account("James", "12/02/1996")
account2 = Account("Liam", "17/08/1991")
account3 = Account("Blair", "29/05/2003")

account1.follow(account3)
account1.follow(account2)
account2.follow(account1)

print(account1.followers)

for account in account1.followers:
    print(account.followers)

print(account1.follows_me(account2))

print("Posts")

account1.add_post(post1)

print(account1.posts)


    