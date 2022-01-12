import requests

COMMENTS_URL = "https://jsonplaceholder.typicode.com/posts/1/comments"
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
TUES_URL = "https://tues2022.proxy.beeceptor.com/my/api/test"

class ApiProcessor:
    @staticmethod
    def longest_comment():
        data = requests.get(COMMENTS_URL)
        comments = sorted(data.json(), key=lambda d: d['body'], reverse=True)
        return comments[0]

    @staticmethod
    def post_with_longest_title():
        data = requests.get(POSTS_URL)
        posts = sorted(data.json(), key=lambda d: d['title'], reverse=True)
        return posts[0]

temperatures = []
data = requests.post(TUES_URL).json()

for x in range(0, 5):
    temperatures.append(data["data"][x]["temperature"])


class ApiTuesProcessor:

    @staticmethod
    def get_data():
        return temperatures

    @staticmethod
    def min_temp():

        return min(temperatures)
    @staticmethod
    def max_temp():

        return max(temperatures)
    @staticmethod
    def avg_temp():

        return sum(temperatures) / len(temperatures)
