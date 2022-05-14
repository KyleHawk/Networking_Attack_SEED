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
![image](https://user-images.githubusercontent.com/86921341/168404635-e5854101-411d-4b5b-aec1-a91d19517d59.png)

autoattack.py
It is important to change the "iface"
![image](https://user-images.githubusercontent.com/86921341/168404622-a97a6039-e202-483e-828d-0be0aa9d9430.png)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Sniffering

![image](https://user-images.githubusercontent.com/86921341/168404450-ff7059f7-1953-4b04-b6c7-aa1efcdc363c.png)

![image](https://user-images.githubusercontent.com/86921341/168404462-36d84064-fbc3-449c-8ef4-4d1261a953ab.png)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

SPOOFING

![image](https://user-images.githubusercontent.com/86921341/168404701-9512538d-3ce8-482c-b2fc-47e524068d70.png)
![image](https://user-images.githubusercontent.com/86921341/168404703-2717aebf-3cbc-4152-953e-ed07b4771a5e.png)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Redirect attack

![image](https://user-images.githubusercontent.com/86921341/168404723-7542b1a3-914b-4164-8107-0e11f832ed8a.png)
![image](https://user-images.githubusercontent.com/86921341/168404725-764f1bed-012c-4b32-9d96-1b5a5dbade28.png)
![image](https://user-images.githubusercontent.com/86921341/168404729-13977e83-eddb-4be3-be85-0d69c76081e2.png)
![image](https://user-images.githubusercontent.com/86921341/168404733-f05eb54a-3b33-4287-a837-10d68b01cc09.png)

On destination host docker:

![image](https://user-images.githubusercontent.com/86921341/168404752-c161929b-e40c-4c52-80ba-5ffa0919841f.png)

On victim docker:

![image](https://user-images.githubusercontent.com/86921341/168404756-e5239942-7078-41f8-abb2-cbd06dbd7df5.png)


On malicious router docker:

![image](https://user-images.githubusercontent.com/86921341/168404761-3cec7cd8-0850-4625-a938-dcec5a1617fb.png)

Use mitm_nc python program on malicious router
Victim:  

![image](https://user-images.githubusercontent.com/86921341/168404785-145b33bf-ddc3-4804-b898-af9be2af7557.png)

Destination:

![image](https://user-images.githubusercontent.com/86921341/168404788-20ae6e08-275f-4634-bada-395411167333.png)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

TCP AUTO ATTACK

Sniff victim(10.9.0.5) who connects to user1(10.9.0.6)

![image](https://user-images.githubusercontent.com/86921341/168404803-af69268d-48bc-4736-ae65-cb8a32871123.png)

Reset the connection

![image](https://user-images.githubusercontent.com/86921341/168404807-5cfabdb7-7c9a-41b6-baf8-5f008da33f61.png)

When victim tries to connect user1
![image](https://user-images.githubusercontent.com/86921341/168404815-f400e115-fdaf-43d8-844d-fa3b3dfdf233.png)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Autoattack python program continues its surveillance

![image](https://user-images.githubusercontent.com/86921341/168404828-1f93d4a6-01ea-45cc-b085-23ed983618d7.png)
![image](https://user-images.githubusercontent.com/86921341/168404829-7c4003d1-ef99-4a28-865d-c9644acef234.png)






