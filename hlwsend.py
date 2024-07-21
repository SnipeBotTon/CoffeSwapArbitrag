from pytoniq import LiteBalancer, HighloadWallet

import asyncio

from config import adrress_dist, amount_out, mnemonic




mnemonics = mnemonic

async def main():
    client = LiteBalancer.from_mainnet_config(trust_level=1)
    await client.start_up()
    wallet = await HighloadWallet.from_mnemonic(mnemonics=mnemonics, provider=client)


    
    await wallet.transfer(destinations=[adrress_dist], amounts=[int(float(amount_out)*1e9)], bodies=['Send'])
    await client.close_all()

if __name__ == '__main__':
    asyncio.run(main())




