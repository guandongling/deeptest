# coding=utf-8
# 命令行参数
import sys

if __name__ == "__main__":
    print("命令行参数个数: %d" % len(sys.argv))
    print("命令行参数列表：%s" % str(sys.argv))
