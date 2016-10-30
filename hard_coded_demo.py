#!/usr/bin/env python2.7

import serial
import re
import time


class Arduino:
    def __init__(self, port, duties):
        assert isinstance(port, str)
        assert isinstance(duties, str)
        self.port = port
        self.duties = duties

        self.serial = serial.Serial(port=port, baudrate=9600)

    def do_command(self, command):
        assert isinstance(command, str)
        command = "".join(filter(lambda s: s[0] in self.duties, re.split(r"([a-zA-Z]\d+)")))
        self.serial.write(command)


class Crane:
    def __init__(self, arduinos):
        self.arduinos = arduinos

    def do_command(self, command):
        assert isinstance(command, str)
        assert re.match(r"^([a-zA-Z]\d+)*$", command) is not None
        map(lambda x:x.do_command(command), self.arduinos)


class M:
    def __init__(self, command, wait_time):
        self.command = command
        self.wait_time = wait_time

        assert re.match(r"^([a-zA-Z]\d+)*$", command) is not None
        assert wait_time >= 0

    def apply(self, crane):
        crane.do_command(self.command)
        time.sleep(self.wait_time)


movements = [
    M("",1)
]
assert map(lambda x: isinstance(x, M), movements)


def main():
    arduinos = [
        Arduino("/dev/tty0", "st"),
        Arduino("/dev/tty1", "ew"),
        Arduino("/dev/tty2", "gr")
    ]
    crane = Crane(arduinos)
    for m in movements:
        m.apply(crane)


if __name__ == "__main__":
    main()
