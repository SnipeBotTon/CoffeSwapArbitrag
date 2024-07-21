import asyncio

from pytoniq import LiteBalancer, HighloadWallet

from tonsdk.crypto import mnemonic_new


mnemonics = mnemonic_new()


async def main():
    client = LiteBalancer.from_mainnet_config(trust_level=1)
    await client.start_up()
    wallet = await HighloadWallet.from_mnemonic(mnemonics=mnemonics, provider=client)

    adrrwallet = wallet.address
    await client.close_all()
    filename = 'wallet_data.txt'

    with open(filename, 'w') as f:
        f.write(f"Mnemonics: {mnemonics}\n")
        f.write(f"Adrress: {adrrwallet}\n")
        

    
    print(f'Пополни баланс кошелька {adrrwallet} минимум на 0.01 TON, и когда тоны будут на кошельке нажми Enter.')
    input()
    await client.start_up()
    await wallet.send_init_external()

    
    
    await client.close_all()

if __name__ == '__main__':
    asyncio.run(main())
