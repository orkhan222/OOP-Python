# Comment isminde bir sinif olusturunuz.
# Comment sinifi username, text, likes, dislikes isimde ozelliklere sahip olsun.
# 5 adet farkli commet olusturup dongu yardimiyla yorumlari ekrana yazdiriniz.


class Comment:
    def __init__(self,username,text,dislikes,likes):
        self.username = username
        self.text = text
        self.dislikes = dislikes
        self.likes = likes
        
user1 = Comment('Orkhan','lorem ium',20,50)
user2 = Comment('Orkhan','lorem sum',240,60)
user3 = Comment('Orkhan','lorempsum',24470,57470)
user4 = Comment('Orkhan','lor ipsum',20474,574740)
user5 = Comment('Orkhan','lorem',20171,547170)


comments = [user1,user2,user3,user4,user5]

for c in comments:
    print(f'{c.username}: {c.text}')
    print(f'likes: {c.likes} - dislikes: {c.dislikes}')
