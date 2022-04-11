from brownie import accounts, convert, Functional, FunctionalFixed, ProxyFunc
import pytest
import pdb


def test_proxy():
    funcWrong = Functional.deploy({"from": accounts[0]})
    funcGood = FunctionalFixed.deploy({"from": accounts[0]})
    proxy = ProxyFunc.deploy(funcWrong.address, {"from": accounts[0]})
    # print(type(proxy.get_func_proxy_storage().return_value[1])) # returned value is classbrownie.convert.datatypes.HexString(value, type_)
    assert proxy.get_func_proxy_storage().return_value[1] == "0x0"
    proxy.set_func_proxy_storage(4)
    assert proxy.get_func_proxy_storage().return_value[1] == "0x5"
    proxy.upgrade(funcGood.address)
    assert proxy.get_func_proxy_storage().return_value[1] == "0x5"
    proxy.set_func_proxy_storage(4)
    assert proxy.get_func_proxy_storage().return_value[1] == "0x4"
