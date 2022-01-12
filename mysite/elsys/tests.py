from django.test import TestCase
from elsys.models import Car
from elsys.processors.api_processor import ApiProcessor, ApiTuesProcessor
from datetime import datetime

class TestCarModel(TestCase):
    def setUp(self):
        #called when test is started
        Car.objects.create(color="red", made=datetime.now(), brand="audi", description = "red audi", is_electric=False)
        Car.objects.create(color="green", made=datetime.now(), brand="bmw", description = "red bmw")

    def tearDown(self):
        #called after tests were run
        pass

    def test_car_is_red(self):
        assert Car.objects.get(brand="audi").color == "red"

    def test_car_is_green(self):
        assert Car.objects.get(brand="bmw").color == "green"

    def test_car_sound(self):
        assert Car.objects.get(brand="audi").sound_check() == "brum brum"

#from unittest.mock import patch

class TestApiProcessor(TestCase):

    def test_longest_comment(self):
        self.assertEqual(ApiProcessor.longest_comment(), {"postId": 1, "id": 3, "name": "odio adipisci rerum aut animi", "email": "Nikita@garfield.biz", "body": "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"})

    def test_post_with_longest_title(self):
        self.assertEqual(ApiProcessor.post_with_longest_title(), {"userId": 6, "id": 58, "title": "voluptatum itaque dolores nisi et quasi", "body": "veniam voluptatum quae adipisci id\net id quia eos ad et dolorem\naliquam quo nisi sunt eos impedit error\nad similique veniam"})


class TestApiTuesProcessor(TestCase):

    def test_min(self):
        self.assertEqual(ApiTuesProcessor.min_temp(), 3)

    def test_max(self):
        self.assertEqual(ApiTuesProcessor.max_temp(), 8)

    def test_avg(self):
        self.assertEqual(ApiTuesProcessor.avg_temp(), 5.0)

#class ApiHandler:
#    def call_api(self):
#        response = requests.get("url")
#        data = response['data']
#        return data['a'] + 1


#class TestC(TestCase):
#    @patch("requests.get")
#    def test_call_api(self, mocked_requests):
#        mocked_requests.return_value = {'data':{'a': 1}}
#        response = ApiHandler().call_api()
#        assert response == 2
