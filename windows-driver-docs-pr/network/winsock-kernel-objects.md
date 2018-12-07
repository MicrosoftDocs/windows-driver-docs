---
title: Winsock Kernel Objects
description: Winsock Kernel Objects
ms.assetid: 1ce9bd19-9159-4a73-96f6-6e2adac886b9
keywords:
- Winsock Kernel WDK networking , objects
- WSK WDK networking , objects
- objects WDK Winsock Kernel
- socket objects WDK Winsock Kernel
- client objects WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Winsock Kernel Objects


The Winsock Kernel (WSK) [Network Programming Interface (NPI)](network-programming-interface.md) is designed around two main object types: *Client* and *Socket* .

<a href="" id="client-object-------"></a>**Client Object**   
A *client object* represents the attachment, or binding, between a WSK application and the WSK subsystem. A client object is represented by the [**WSK\_CLIENT**](https://msdn.microsoft.com/library/windows/hardware/ff571155) structure. A pointer to a client object is returned to a WSK application during the process of attachment to the WSK subsystem. A WSK application passes this pointer to all WSK functions that operate at the client object level.

<a href="" id="socket-object-------"></a>**Socket Object**   
A *socket object* represents a network socket that can be used for network I/O. A socket object is represented by the [**WSK\_SOCKET**](https://msdn.microsoft.com/library/windows/hardware/ff571182) structure. A pointer to a socket object is returned to a WSK application when the application creates a new socket or when the application accepts an incoming connection. A WSK application passes this pointer to all WSK functions that are specific to a particular socket.

 

 





