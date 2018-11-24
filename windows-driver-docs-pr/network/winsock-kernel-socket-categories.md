---
title: Winsock Kernel Socket Categories
description: Winsock Kernel Socket Categories
ms.assetid: e99cbef5-c484-43ee-be02-8088f51117ef
keywords:
- Winsock Kernel WDK networking , socket categories
- WSK WDK networking , socket categories
- basic sockets WDK Winsock Kernel
- listening sockets WDK Winsock Kernel
- datagram sockets WDK Winsock Kernel
- connection-oriented sockets WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Winsock Kernel Socket Categories


The Winsock Kernel (WSK) [Network Programming Interface (NPI)](network-programming-interface.md) defines five different categories of sockets: *basic sockets*, *listening sockets*, *datagram sockets*, *connection-oriented sockets*, and *stream sockets*. Each WSK socket category has unique functionality and supports a different set of socket functions. A WSK application must specify which category of WSK socket it is creating whenever it creates a new socket. The purpose for each WSK socket category is as follows:

<a href="" id="basic-sockets-------"></a>**Basic Sockets**   
Basic sockets are used only to get and set transport stack socket options or to perform socket I/O control operations. Basic sockets cannot be bound to a local transport address and do not support sending or receiving network data.

<a href="" id="listening-sockets-------"></a>**Listening Sockets**   
Listening sockets are used to listen for incoming connections from remote transport addresses. The functionality of a listening socket includes all of the functionality of a basic socket.

<a href="" id="datagram-sockets-------"></a>**Datagram Sockets**   
Datagram sockets are used to send and receive datagrams. The functionality of a datagram socket includes all of the functionality of a basic socket.

<a href="" id="connection-oriented-sockets-------"></a>**Connection-Oriented Sockets**   
Connection-oriented sockets are used to send and receive network data over established connections. The functionality of a connection-oriented socket includes all of the functionality of a basic socket.

<a href="" id="stream-sockets-------"></a>**Stream Sockets**   
Stream sockets are used to either listen for incoming connections from remote transport addresses (act as a listening socket), or to send and receive network data over established connections (act as a connection-oriented socket). Use a stream socket when you do not know at the time of socket creation if you want a listening socket or a connection-oriented socket. The functionality of a stream socket includes all of the functionality of a basic socket.
 





