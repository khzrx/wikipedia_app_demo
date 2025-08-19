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

    load_dotenv(dotenv_path=env_file_path)