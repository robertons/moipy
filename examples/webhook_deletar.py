# -*- coding: utf-8 -*-
import json
import moippy
import sys


def main(arg):
    moippy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    webhook = moippy.Webhook(id='wbh_11B3758670F065DA').Delete()


if __name__ == "__main__":
    main(sys.argv)
