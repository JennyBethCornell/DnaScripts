#!/usr/bin/env python3

"""
This script checks whether a DNA sequence has any undefined bases ('n' or 'N').
"""
dna = input('Enter DNA sequence:')


if 'n' in dna or 'N' in dna:
	nbases=dna.count('n')+dna.count('N')
	print("dna sequence has %d undefined bases " % nbases)
else:
	print("dna sequence has no undefined bases")

