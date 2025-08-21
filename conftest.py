from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        '--context',
        default='bstack',
        help='Specify the test context'
    )

def pytest_configure(config):
    context = config.getoption('--context')
    env_file_path = f'.env.{context}'
    env_credentials_file_path = '.env.credentials'

    load_dotenv(dotenv_path=env_file_path)
    load_dotenv(dotenv_path=env_credentials_file_path)
