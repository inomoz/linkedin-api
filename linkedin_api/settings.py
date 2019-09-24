import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_URL = 'https://www.linkedin.com/uas/login?trk=guest_homepage-basic_nav-header-signin'
HOMEPAGE_SALES_URL = 'https://www.linkedin.com/uas/login?session_redirect=%2Fsales&fromSignIn=true&trk=navigator'
LOGIN_URL = 'https://www.linkedin.com/checkpoint/lg/login-submit'
CHECKPOINT_URL = 'https://www.linkedin.com/checkpoint/challenge/verify'

ADDITONAL_USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'
]

KEYORDER = ['csrfToken',
            'session_key',
            'ac',
            'sIdString',
            'controlId',
            'parentPageKey',
            'pageInstance',
            'trk',
            'session_redirect',
            'loginCsrfParam',
            'fp_data',
            '_d',
            '_f',
            'session_password']

LOGIN_TIMEOUT = 320