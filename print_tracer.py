import builtins
import sys

origin_print = builtins.print


def print_trace(*args, sep=' ', end='\n', file=None):
    """
    打印追踪器
    :param args:要打印的值
    :param sep:值之间插入的字符串,默认为空格
    :param end:最后一个值后追加的字符串,默认为换行符
    :param file:类文件对象
    :return:
    """
    if file:
        origin_print(*args, sep, end, file)
        return
    # noinspection PyProtectedMember, PyUnresolvedReferences
    file_name = sys._getframe().f_back.f_code.co_filename  # 获取调用函数所在的文件路径
    # noinspection PyProtectedMember, PyUnresolvedReferences
    line = sys._getframe().f_back.f_lineno  # 获取调用函数所在的行号
    origin_print(f'{file_name}:{line}  ', *args, sep, end)


# 猴子补丁,运行时修改
builtins.print = print_trace
