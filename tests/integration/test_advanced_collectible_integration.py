from brownie import network, AdvancedCollectible
import time
import pytest
from scripts.utils import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible_integration():

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    # Act
    # deploy_and_create() => 部署合约并创建了NFT
    advanced_collectible, creation_transaction = deploy_and_create()
    # 等待回调，获得random
    time.sleep(60)
    # Assert
    # token计数 + 1
    assert advanced_collectible.tokenCounter() == 1
