from brownie import network, AdvancedCollectible
import pytest
from scripts.utils import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
    get_breed,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    # Act
    # deploy_and_create => 部署与创建NFT
    advanced_collectible, creation_transaction = deploy_and_create()
    # 获得事件中存储的requestId
    requestId = creation_transaction.events["requestedCollectible"]["requestId"]
    random_number = 777
    # Mock 模拟回调，将requestId传入，将random_number作为回调返回的随机数
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advanced_collectible.address, {"from": get_account()}
    )
    # Assert
    # tokenCounter计数+1
    assert advanced_collectible.tokenCounter() == 1
    # 判断随机数获得的品种
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3


def test_get_breed():
    # Arrange / Act
    breed = get_breed(0)
    # Assert
    assert breed == "PUG"
