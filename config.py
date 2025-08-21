import os
from appium.options.android import UiAutomator2Options
from wikipedia_app_demo import utils
from pydantic import BaseModel


class Config(BaseModel):
    context: str
    remote_url: str = os.getenv('REMOTE_URL')
    device_name: str = os.getenv('DEVICE_NAME')
    app_wait_activity: str = os.getenv('APP_WAIT_ACTIVITY')
    app_local: str = utils.file.abs_path_from_project(os.getenv('APP'))
    app_bstack: str = os.getenv('APP')
    platform_name: str = os.getenv('PLATFORM_NAME')
    platform_version: str = os.getenv('PLATFORM_VERSION')
    username: str = os.getenv('BSTACK_USERNAME')
    access_key: str  = os.getenv('BSTACK_ACCESSKEY')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        options.set_capability('remote_url', self.remote_url)
        options.set_capability('deviceName', self.device_name)
        options.set_capability('appWaitActivity', self.app_wait_activity)

        if context in ('local_emulator', 'local_real_device'):
            options.set_capability('app', self.app_local)

        if context == 'bstack':
            options.set_capability('app', self.app_bstack)
            options.set_capability('platformName', self.platform_name)
            options.set_capability('platformVersion', self.platform_version)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'Wikipedia project',
                    'buildName': 'browserstack-build-1',
                    'sessionName': 'BStack test',
                    'userName': self.username,
                    'accessKey': self.access_key
                }
            )

        return options

config = Config(context='bstack')
