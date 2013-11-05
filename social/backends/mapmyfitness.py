"""
MapMyFitness OAuth support.

This contribution adds support for MapMyFitness Oauth service. The settings
SOCIAL_AUTH_MAPMYFITNESS_KEY and SOCIAL_AUTH_MAPMYFITNESS_SECRET must be
defined with the values given by RunKeeper application registration process.
"""
from social.backends.oauth import BaseOAuth1


class MapMyFitnessOAuth(BaseOAuth1):
    """
    MapMyFitness OAuth authentication backend
    """
    name = 'mapmyfitness'
    AUTHORIZATION_URL = 'https://www.mapmyfitness.com/oauth/authorize/'
    REQUEST_TOKEN_URL = 'https://api.mapmyapi.com/v7.0/oauth/temporary_credential/'
    ACCESS_TOKEN_URL = 'https://api.mapmyapi.com/v7.0/oauth/token_credential/'
    REQUEST_TOKEN_METHOD = 'POST'
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_details(self, response):
        return {'username': response.get('username'),
                'email': response.get('email'),
                'fullname': ' '.join((response.get('first_name'),
                                      response.get('last_name'))),
                'first_name': response.get('first_name'),
                'last_name': response.get('last_name')}

    def user_data(self, access_token):
        user_data = self.get_json('https://api.mapmyapi.com/v7.0/user/self/', auth=self.oauth_auth(access_token))
        return user_data