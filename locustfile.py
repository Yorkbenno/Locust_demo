import json
from locust import HttpUser, task, between
import random
import logging
logging.basicConfig(level=logging.INFO)

class MovieRecommendationUser(HttpUser):
    wait_time = between(1, 5)
    user_list = ['586983', '177883', '618296', '651953', '516855', '569628', '152655', 
                 '162978', '30666', '755410', '206285', '491226', '690059', '751306', 
                 '434324', '746714', '527386', '789630', '799324', '495880', '523182', 
                 '561813', '411152', '10552', '243418', '154602', '125745', '574314', 
                 '235381', '144525']
    @task
    def get_movie_recommendation(self):
        user_id = random.choice(self.user_list)
        with self.client.get(f"/recommend/{user_id}", catch_response=True) as response:
            try:
                assert response.status_code == 200, f"Status code not 200, instead {response.status_code}"
                recommendation_movies = response.text
                assert len(recommendation_movies.split(',')) == 20, "Recommended movie less than 20!"
                logging.info(f"Received recommendation movie for user: {user_id}")
                # If everything is fine, mark the response as successful
                response.success() 
            except AssertionError as e:
                # If an assertion fails, mark the response as a failure and report the error
                response.failure(str(e))

class MovieInfoServiceUser(HttpUser):
    wait_time = between(1, 3)
    movie_list = ['the+wrong+trousers+1993', 'presto+2008', 'kids+1995',
                'dont+torture+a+duckling+1972', 'the+shawshank+redemption+1994',
                'the+silence+of+the+lambs+1991', 'shoah+1985', 'the+wrong+trousers+1993',
                'pulp+fiction+1994', 'the+power+of+kangwon+province+1998',
                'the+lives+of+others+2006', 'the+merchant+of+venice+2004', 'inception+2010',
                'the+godfather+1972', 'the+silence+of+the+lambs+1991', 'highlander+1986', 
                'pulp+fiction+1994', 'the+silence+of+the+lambs+1991', 'the+terminator+1984',
                'fury+2014', 'the+silence+of+the+lambs+1991', 'monsieur++hulots+holiday+1953',
                'shoah+1985', 'the+silence+of+the+lambs+1991', 'shoah+1985', 'how+to+deal+2003', 
                'wreck-it+ralph+2012', 'shoah+1985', 'shoah+1985', 'the+shawshank+redemption+1994']

    @task
    def get_movie_info(self):
        movie_name = random.choice(self.movie_list)
        with self.client.get(f"/movie/{movie_name}", catch_response=True) as response:
            try:
                assert response.status_code == 200, "Status code not 200"
                movie_info = json.loads(response.content)
                assert movie_info['id'] == movie_name, "response does not correspond to the request movie!"
                logging.info(f"Received movie info of: {movie_info['id']}")
                # If everything is fine, mark the response as successful
                response.success()
            except AssertionError as e:
                # If an assertion fails, mark the response as a failure and report the error
                response.failure(str(e))

class UserInfoServiceUser(HttpUser):
    wait_time = between(1, 3)
    user_list = ['586983', '177883', '618296', '651953', '516855', '569628', '152655', 
                 '162978', '30666', '755410', '206285', '491226', '690059', '751306', 
                 '434324', '746714', '527386', '789630', '799324', '495880', '523182', 
                 '561813', '411152', '10552', '243418', '154602', '125745', '574314', 
                 '235381', '144525']

    @task
    def get_user_info(self):
        user_id = random.choice(self.user_list)
        with self.client.get(f"/user/{user_id}", catch_response=True) as response:
            try:
                assert response.status_code == 200, "Status code not 200"
                user_info = json.loads(response.content)
                assert user_info['user_id'] == int(user_id), "response does not correspond to the request user!"
                logging.info(f"Received user info of: {user_info['user_id']}")
                # If everything is fine, mark the response as successful
                response.success() 
            except AssertionError as e:
                # If an assertion fails, mark the response as a failure and report the error
                response.failure(str(e))


# class MovieInfoServiceErrorUser(HttpUser):
#     user_list = ['586983', '177883', '618296', '651953', '516855', '569628', '152655', 
#                 '162978', '30666', '755410', '206285', '491226', '690059', '751306', 
#                 '434324', '746714', '527386', '789630', '799324', '495880', '523182', 
#                 '561813', '411152', '10552', '243418', '154602', '125745', '574314', 
#                 '235381', '144525']
    
#     @task
#     def get_user_info(self):
#         user_id = random.choice(self.user_list)
#         with self.client.get(f"/user/{user_id}", catch_response=True) as response:
#             try:
#                 assert response.status_code == 200, "Status code not 200"
#                 user_info = json.loads(response.content)
#                 # An error here
#                 assert user_info['user_id'] == user_id, "response does not correspond to the request user!"
#                 logging.info(f"Received user info of: {user_info['user_id']}")
#                 # If everything is fine, mark the response as successful
#                 response.success()
#             except AssertionError as e:
#                 # If an assertion fails, mark the response as a failure and report the error
#                 response.failure(str(e))

