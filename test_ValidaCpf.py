from validaCpf import *


def testGeraDv1():
    assert geraDv1("123456789") == 10
    assert geraDv1("936558900") == 2


def testGeraDv2():
    assert geraDv2("123456789", 10) == 0
    assert geraDv2("936558900", 2) == 8


def testvalidaNumeroCpf():
    assert validaNumeroCpf("12345678909") == False
    assert validaNumeroCpf("12345678900") == True
    assert validaNumeroCpf("123.456.789-00") == True
    assert validaNumeroCpf("") == False
    assert validaNumeroCpf(12345678900) == True


def testGeraCpfValido():
    assert validaNumeroCpf(geraCpfValido()) == True


def testGeraListaCpf():
    assert len(geraListaCpf(10)) == 10
    assert len(geraListaCpf(100)) == 100

def testgeraCpfValidoComMascara():
    assert validaNumeroCpf(geraCpfValidoComMascara()) == True