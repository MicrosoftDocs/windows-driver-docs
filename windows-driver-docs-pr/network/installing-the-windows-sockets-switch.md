---
title: Installing the Windows Sockets Switch
description: Installing the Windows Sockets Switch
keywords:
- Windows Sockets Direct WDK , installing components
- layered service providers WDK SANs
ms.date: 04/20/2017
---

# Installing the Windows Sockets Switch





Microsoft Windows installs the Windows Sockets switch as a *layered service provider*, with the Windows Sockets service provider interface (SPI) as both the top and bottom interface. The switch exports the protocol characteristics of TCP/IP just like the TCP/IP service provider. The switch is the first visible TCP/IP provider, which makes the switch the default choice for applications that open sockets for the [WSK address families](ws2def-h.md).

 

