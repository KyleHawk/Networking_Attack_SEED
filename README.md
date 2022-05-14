# Networking_Attack_SEED
Features:​

Sniffering​

Spoofing​

Redirect attack​

MITM Attack​

TCP Reset Attack​

The network I designed is shown in the figure below, with two networks. One of the subnets has attacker, victim, user one, router and a malicious router, and the other has only one host.

Network:

![image](https://user-images.githubusercontent.com/86921341/168404376-bb7d9a1d-bf3c-431e-8d13-ea80f2251ae7.png)

At the beginning of the project I need to create containers with docker. I use this command, then I will get two networks, the screenshot below is one of them. The string starting with "br- " is the interface name of the network 10.9.0.1, which I need to use in the autoattack.Py file.

Docker

![image](https://user-images.githubusercontent.com/86921341/168404420-6f4b2d96-b694-4aec-93fd-329a6cb5c6c5.png)
![image](https://user-images.githubusercontent.com/86921341/168404423-d91cc204-5177-4bfb-b142-543708994189.png)

Sniffering

![image](https://user-images.githubusercontent.com/86921341/168404450-ff7059f7-1953-4b04-b6c7-aa1efcdc363c.png)

![image](https://user-images.githubusercontent.com/86921341/168404462-36d84064-fbc3-449c-8ef4-4d1261a953ab.png)
