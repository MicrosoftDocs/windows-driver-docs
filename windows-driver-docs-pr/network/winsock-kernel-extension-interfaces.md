---
title: Winsock Kernel Extension Interfaces
description: Winsock Kernel Extension Interfaces
ms.assetid: db0030fa-0ee9-482b-b6ba-e95b40a25473
keywords:
- Winsock Kernel WDK networking , extension interfaces
- WSK WDK networking , extension interfaces
- extension interfaces WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Winsock Kernel Extension Interfaces


The Winsock Kernel (WSK) [Network Programming Interface (NPI)](network-programming-interface.md) includes support for *extension interfaces*. The WSK subsystem can use extension interfaces to extend the functionality of WSK sockets beyond the set of socket functions and event callback functions currently defined by the WSK NPI. Each extension interface is defined by an NPI that is independent of the WSK NPI. Currently no extension interfaces have been defined.

A WSK application can register for an extension interface that is supported by the WSK subsystem by using the [**SIO\_WSK\_REGISTER\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff570819) socket IOCTL operation. A WSK application registers for extension interfaces on a socket-by-socket basis.

For more information about registering an extension interface, see [Registering an Extension Interface](registering-an-extension-interface.md).

 

 





