from decouple import config
from .models import Social
import requests
import json
from tiktok_scheduler.s3_utils import S3Utils

class TiktokUtils:
    def __init__(self, url=None, access_token = None, open_id = None):
        self.url = url
        self.client_secret = config('TIKTOK_APP_CLIENT_SECRET')
        self.client_key = config('TIKTOK_APP_CLIENT_KEY')
        self.access_token = access_token
        self.open_id = open_id
        
    def authorize_tiktok_url():
        csrf_token = 'wrvef34783'
        
        tiktok_key = config('TIKTOK_APP_CLIENT_SECRET')
        auth_url = config('TIKTOK_AUTH_URL')
        redirect_url = config('PLATFORM_REDIRECT_URL')
        redirect_url_endpoint = f"{redirect_url}platform=tiktok&"
        
        url = f"{auth_url}/?client_key={tiktok_key}&scope=user.info.basic,video.list,video.add&response_type=code&redirect_uri={redirect_url_endpoint}&state={csrf_token}"
        return url
        #example tiktok url
        #https://www.tiktok.com/auth/authorize/?client_key={tiktok app secret key}&scope=user.info.basic,video.list&response_type=code&redirect_uri={SERVER_ENDPOINT_REDIRECT}&state={csrf token}
        #after user authorizes access to their account
        #they will be redirect to the provided server endpoint with query params appended to it
        #the 'code' will be provided if successful, 'error' if not
        
        #use the 'code' to get an auth token for tiktok user account
        #store 'code' in db
        
        #return url
        
    def store_code(self, code=None, user=None):
        social = Social.objects.create(user = user, code=code, platform='tiktok')
        return social
    
    #takes social db object as argument
    def get_access_token(self, social = None):
        base_url = social.platform.token_url
        formatted_url = f"{base_url}client_key={self.client_key}&client_secret={self.client_secret}&code={social.code}&grant_type=authorization_code"
        response = requests.post(formatted_url).json()
        self.access_token = response['data']['access_token']
        self.open_id = response['data']['open_id']
        
        if self.access_token:
            return True
        return False
    
    def add_post_errors(self, post, error):
        error_list = post.errors
        if error_list:
            error_list = f"{error_list}, {error}"
        else:
            error_list = error
        post.errors = error_list
        post.save()
        
    def upload_post(self, social = None, post = None):
        tokens = self.get_access_token(social)
        
        if not tokens:
            self.add_post_errors(post, 'tiktok auth error')
            return False
        
        video = S3Utils.get_video(post.video)
        url = f"{social.platform.add_url}open_id={self.open_id}&access_token={self.access_token}"
        
        request = requests.post(url, 
                                headers = json.dumps({'Content-Type':'multipart/form-data'}),
                                files = {'video':video}).json()
        
        error = request['data']['error_code']
        print(request['data']['error_message'])
        
        if error:
            self.add_post_errors(post, 'error posting tiktok')
            return False
        
        return True