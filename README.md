# CounterParty-domain-query (v.001)
A utility to query decentralised DAT domains stored as counterparty assets on the blockchain.

The premise of this is code snippet is to lay the tiniest of groundwork for an idea: using the CounterParty protocols asset registration features, on top of the bitcoin blockchain as a decentralised domain name registry. Using such an approach, Decentralised vanity domain names would able to be brought and sold in a p2p setting trustlessly across a DeX or directly between two users and with ownership of the domain names in perpuity remaining with the owners of the private keys and not a centralised registrar- with no renewal fees, expirys or limitations on who can register what.

For the first iteration and as a demo DAT protocol is used. In the DAT protocol each URL is represented by a 64 byte hexadecimal key; to register a short domain name, we can take an existing DAT domain and encode it to fit inside the character limitation embedded within counterparty asset descriptions. Future versions could support other possible options- like Using IPFS and a public gateway in conjuction with an extension to resolve and navigate to 'friendly' asset names stored as counterparty assets without the need for a specialized browser. 

Although this would not be purely p2p, it would still allow the ownership, and control of domains to be in the hands of users, and allow the ability to navigate to friendly, easy to remember names rather than long ambigous strings. Alternatively direct IP resolution could also be used, in conjuction with a local DNS server, for which there already exists a standalone project- and resolver under the CounterParty DNS code base.

In v 0.001 An (extremely basic) python script currently accepts an asset name as an argument. This asset name is queried, the encoded asset name is decoded and re-represented as a dat compatible URL. You can then launch the URL using beaker browser. Future versions would auto launch the URL, and future versions beyond that would seek to natively integrate this into browser without need for a standalone script. 

Any pull requests, issues or none code related contributions to expand on this idea are highly welcomed.



Instructions to register a vanity URL on the decentralised web
==============================================================

1) Create a DAT site, clone an existing site or use an existing DAT URL.
2) Convert the DAT URL (exempting the dat:// prepending) to Base32.
3) embed this string to your counterparty asset of choice. This asset name will be your vanity URL


Instructions to browse the decentralised web using vanity URL
=============================================================
1) Download this python file
2) Download beaker browser, if on Linux place the AppImage in the same directory
3) Run this python file and pass an asset name you wish to browse to. If it is a valid URL the decentralized webpage should open

Todo/improvements: 
=============================================================
A lot! 

No checking for whether an asset actually contains a valid URL or not yet.

Beaker doesn't accept arguments to programatically launch the discovered url in anything other than linux yet, so this must be done manually in v 0.0001

Currently standalone script is utilised, it will be far more ideal for this scripts name lookup to be natively baked into the beaker-browser. 


Subassets are an interesting line to look into (as TLD's) e.g PIZZA.BTC, PIZZA.ETH, PIZZA.LTC

