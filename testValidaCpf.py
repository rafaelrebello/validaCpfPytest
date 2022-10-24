from validaCpf import *

def testValidaCpf():
    assert validaNumeroCpf('12345678909') == True
    assert validaNumeroCpf('12345678900') == False

def testGeraCpfValido():
    assert validaNumeroCpf(geraCpfValido()) == True

def testGeraListaCpf():
    assert len(geraListaCpf(10)) == 10
    assert len(geraListaCpf(100)) == 100
