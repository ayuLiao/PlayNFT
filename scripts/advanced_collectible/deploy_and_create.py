from brownie import AdvancedCollectible
from brownie import network, config

from scripts.utils import *


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    fund_with_link(advanced_collectible.address)
    # 创建NFT
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    # 返回合约对象，和创建NFT的交易对象
    return advanced_collectible, creating_tx


def main():
    deploy_and_create()
