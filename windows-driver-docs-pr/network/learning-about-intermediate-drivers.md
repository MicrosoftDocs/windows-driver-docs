---
title: Learning About Intermediate Drivers
description: Learning About Intermediate Drivers
ms.assetid: 9ce2594a-cdae-4b3e-91f7-c61f860a325e
keywords:
- connectionless drivers WDK networking
- connection-oriented drivers WDK networking
- intermediate drivers WDK networking , connectionless lower edge
- NDIS intermediate drivers WDK , connectionless lower edge
- intermediate drivers WDK networking , connection-oriented lower edge
- NDIS intermediate drivers WDK , connection-oriented lower edge
- network drivers WDK , types
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Learning About Intermediate Drivers


## <a href="" id="ddk-intermediate-drivers-ng"></a>


You can write an intermediate driver that has either a connectionless or a connection-oriented lower edge. The following list describes which sections of the WDK documentation you should read, depending on the type of intermediate driver that you are writing:

<a href="" id="intermediate-drivers-that-have-a-connectionless-lower-edge"></a>**Intermediate drivers that have a connectionless lower edge**  
If you are writing an intermediate driver whose lower edge provides an interface to connectionless miniport drivers, read:

-   [NDIS Intermediate Drivers](ndis-intermediate-drivers.md)

<a href="" id="intermediate-drivers-that-have-a-connection-oriented-lower-edge"></a>**Intermediate drivers that have a connection-oriented lower edge**  
If you are writing an intermediate driver whose lower edge provides an interface to connection-oriented miniport drivers, read:

-   [NDIS Intermediate Drivers](ndis-intermediate-drivers.md)

-   [Connection-Oriented NDIS](connection-oriented-ndis.md)

 

 





