# coding=utf-8

from conf.logger import logger

from module.module import print_module


def is_tdd_course():
    """
    Indicates that is the tdd course
    :return: true
    """
    return True


if __name__ == '__main__':

    logger.info('TDD Course')
    if is_tdd_course():
        logger.info('Yes it is!')
        print_module()

