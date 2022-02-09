# -*- coding: utf-8 -*-
import json
import moipy
import sys


def main(arg):

    moipy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    moipy.charges.SetSplit(id="chr_8C87D875719FE478195F5AE32309F77B", split=[
        moipy.Split(
            recipientToken="Token",
            amount=10.0,
            amountRemainder=True,
            chargeFee=True),
        moipy.Split(
            recipientToken="Token2",
            amount=10.0,
            amountRemainder=False,
            chargeFee=True)
    ])


if __name__ == "__main__":
    main(sys.argv)
