import pytest
from brownie import network

from scripts.simple_collectible.deploy_and_create import deploy_and_create
from scripts.utils import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collectible = deploy_and_create()
    # 合约创建者，属于当前账号
    assert simple_collectible.ownerOf(0) == get_account()
