from validaCpf import *

def testGeraDv1():
    assert geraDv1('123456789') == 10

def testGeraDv2():
    assert geraDv2('123456789', 10) == 0

def testValidaCpf():
    assert validaNumeroCpf('12345678909') == False
    assert validaNumeroCpf('12345678900') == True
    assert validaNumeroCpf('123.456.789-00') == True
    assert validaNumeroCpf('') == False

def testGeraCpfValido():
    assert validaNumeroCpf(geraCpfValido()) == True

def testGeraListaCpf():
    assert len(geraListaCpf(10)) == 10
    assert len(geraListaCpf(100)) == 100
