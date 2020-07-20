import asyncio


async def IOrequest(url):
    print(f"Request: {url}")
    await asyncio.sleep(5)


async def IOsave():
    print("Saved..")
    await asyncio.sleep(5)


# def async_request(func, url):
#     async def wrapper():
#         source = await IOrequest(url)
#         func(source)
#         await IOsave()
#     return wrapper


class decorator2:

    def __init__(self, f, url):
        self.f = f
        self.url = url

    async def __call__(self):
        source = await IOrequest(self.url)
        self.f(source)
        print("Decorating", self.f.__name__)






@decorator2(url="www.google.com")
def testing_yolo(source):
    print('yolo')

testing_yolo()



# wtf how? #################################################################

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)