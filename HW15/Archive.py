import argparse
import logging
from Exeptions import InvalidNumberError, InvalidTextError

FORMAT = '{levelname}, {asctime}, {msg}'
logging.basicConfig(format=FORMAT, style='{', filename= 'HW15/log_arch.log',
                    filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


class Archive:
    _instance = None

    def __new__(cls, text, number):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)

        return cls._instance

    def __init__(self, text, number):
        try:
            if not isinstance(text, str) or len(text.strip()) == 0:
                raise InvalidTextError(f'Invalid text: {text}. '
                                       f'text empty or not string.')
        except InvalidTextError as e:
            logger.error(f'{e}')
        else:
            self.text = text

        try:
            if (not (isinstance(number, int) or isinstance(number, float))
                    or number < 0):
                raise InvalidNumberError(f'Invalid number: {number}. '
                                         f'Number not positive integer or float.')
        except InvalidNumberError as e:
            logger.error(f'{e}')
        else:
            self.number = number

        logger.info(f'Created archive with text: {self.text} '
                    f'and number: {self.number}')

    def __str__(self) -> str:
        return (f"Text is {self.text} and number is {self.number}. "
                f"also {self.archive_text} and {self.archive_number}")

    def __repr__(self) -> str:
        return f"Archive({self.text}, {self.number})"

    # def add_to_archive(self):


def main():
    parser = argparse.ArgumentParser(description='Archive Information')
    parser.add_argument('-t', '--text', type=str, help='Text')
    parser.add_argument('-n', '--number', type=float, help='Number')
    args = parser.parse_args()
    archive = Archive(args.text, args.number)
    return f'{archive}'



if __name__ == "__main__":
    print(main())
# вызов из консоли
# python C:\Users\ksmos\PycharmProjects\pythonProject\HW15\Archive.py -t gg -n 45