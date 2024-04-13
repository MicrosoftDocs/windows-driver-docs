---
title: Learning About Miniport Drivers
description: Learning About Miniport Drivers
keywords:
- connectionless drivers WDK networking
- connection-oriented drivers WDK networking
- WAN miniport drivers WDK networking
- miniport drivers WDK networking , WAN miniport drivers
- NDIS miniport drivers WDK , WAN miniport drivers
- miniport drivers WDK networking , miniport drivers with WDM lower edge
- NDIS miniport drivers WDK , miniport drivers with WDM lower edge
- WDM lower edge WDK networking
- miniport drivers WDK networking , IrDA miniport drivers
- NDIS miniport drivers WDK , IrDA miniport drivers
- IrDA drivers WDK networking
- miniport drivers WDK networking , scalable networking support
- NDIS miniport drivers WDK , scalable networking support
- network drivers WDK , types
ms.date: 04/20/2017
---

# Learning About Miniport Drivers





There are several types of miniport drivers. The following list describes which sections of the WDK documentation you should read, depending on the type of miniport driver that you are writing:

<a href="" id="connectionless-miniport-drivers"></a>**Connectionless miniport drivers**  
If you are writing a miniport driver that controls a network interface card (NIC) for connectionless network media (such as Ethernet), read:

-   [Introduction to NDIS Miniport Drivers](deserialized-ndis-miniport-drivers.md)

-   [NDIS Miniport Drivers](./initializing-a-miniport-driver.md)

<a href="" id="connection-oriented-miniport-drivers"></a>**Connection-oriented miniport drivers**  
If you are writing a miniport driver for connection-oriented network media (such as ISDN), read:

-   All of the sections that are listed earlier in this topic under "Connectionless miniport drivers"

-   [Connection-Oriented NDIS](connection-oriented-ndis.md)

<a href="" id="wan-miniport-drivers"></a>**WAN miniport drivers**  
If you are writing a miniport driver that controls a wide area network (WAN) NIC, read:

-   All of the sections that are listed earlier in this topic under "Connectionless miniport drivers"

-   [WAN Miniport Drivers](wan-miniport-drivers.md)

<a href="" id="miniports-with-a-wdm-lower-interface"></a>**Miniports with a WDM lower interface**  
If you are writing a miniport driver that interfaces to other kernel drivers and has a Microsoft Windows Driver Model (WDM) lower interface, read:

-   All of the sections that are listed earlier in this topic under "Connectionless miniport drivers"

-   [Miniport Drivers with a WDM Lower Interface](miniport-drivers-with-a-wdm-lower-interface.md)

<a href="" id="irda-miniport-drivers"></a>**IrDA miniport drivers**  
If you are writing a miniport driver that controls an IrDA adapter, read:

-   All of the sections that are listed earlier in this topic under "Connectionless miniport drivers"

<a href="" id="miniport-drivers-that-support-scalable-networking"></a>**Miniport drivers that support scalable networking**  
To learn about miniport drivers that support scalable networking, read:

-   [Scalable Networking](/windows-hardware/drivers/ddi/_netvista/)

<a href="" id="miniport-drivers-that-support-offloading-tcp-ip--------to-hardware-------"></a>**Miniport drivers that support offloading TCP/IP to hardware**   
To learn about miniport drivers that offload TCP/IP to hardware, read:

-   [TCP/IP Offload](tcp-ip-offload.md)

 

