# -*- coding: utf-8 -*-
import moippy
import json
import sys


def main(arg):

    moippy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    # PLANO
    plano = moippy.Plan(id='pln_76A6AC4929EF068B').Get()


if __name__ == "__main__":
    main(sys.argv)
