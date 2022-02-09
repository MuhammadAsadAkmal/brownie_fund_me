from brownie import FundMe, accounts, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def main():
    deploy_fundme()


# if we are on persistent network then we need to thoo this contructor on
# add address of exchange in constructor of fund me


def deploy_fundme():
    account = get_account()
    # pass the price feed address to fund me contract
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # price_feed_address = "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # print(f"Contract is deployed to {fund_me.address}")
    print("Contract deployed to the address : " + fund_me.address)
    return fund_me
