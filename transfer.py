from thor_requests.connect import Connect
from thor_requests.wallet import Wallet
from thor_devkit import cry
from thor_devkit.cry import hdnode

connector = Connect("http://3.71.71.72:8669")


def privateKey():
    words = [] #insert Seed words here ["word", "word", ....]
    hd_node = cry.HDNode.from_mnemonic(words)
    for i in range(0, 1):
        address='0x'+hd_node.derive(i).address().hex()
        privkey=hd_node.derive(i).private_key().hex() 
    print(privkey) 
    return str(privkey)

_wallet = Wallet.fromPrivateKey(bytes.fromhex(privateKey())) 

connector.transfer_token(
    _wallet, 
    to=#insert Address where you want to send it,
    token_contract_addr= #insert token address, 
    amount_in_wei=10 * (10 ** 18)
)
