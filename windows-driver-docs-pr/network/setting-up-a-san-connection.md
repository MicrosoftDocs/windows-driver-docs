---
title: Setting Up a SAN Connection
description: Setting Up a SAN Connection
ms.assetid: f5d5e759-d77c-4db8-9b63-fb4c79344dff
keywords:
- Windows Sockets Direct WDK , connection setup
- connections WDK SANs
- SAN connection setup WDK
- SAN connection setup WDK , about SAN connection setup
- SAN service providers WDK , connection setup
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Up a SAN Connection





During connection setup, the Windows Sockets switch determines which service provider will service the TCP socket. This provider will handle most subsequent operations on the socket. Regardless of whether the switch chooses a SAN service provider, the TCP/IP provider exclusively handles a few types of setup operations.

This section describes the connection setup operations that a SAN service provider performs and the connection setup operations that the TCP/IP provider handles. This information is provided in the following topics:

[Creating and Binding SAN Sockets](creating-and-binding-san-sockets.md)

[Initiating a Connection](initiating-a-connection.md)

[Listening for Connections on a SAN](listening-for-connections-on-a-san.md)

[Accepting Connection Requests](accepting-connection-requests.md)

[Registering Memory for Operations on a SAN](registering-memory-for-operations-on-a-san.md)

[Caching Registered Memory](caching-registered-memory.md)

 

 





