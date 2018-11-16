---
title: Installing TCP/IP Printers
description: Installing TCP/IP Printers
ms.assetid: 15339cce-69aa-480d-bfee-11ea509ff5d4
keywords:
- TCP/IP WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing TCP/IP Printers


Networked printers that use TCP/IP can take advantage of features of the TCP Port Monitor to install and configure printers:

-   **Auto-Discovery**: All TCP/IP printers on a subnet are automatically found and installed.

-   **Auto-Selection**: Printer drivers can be automatically selected when TCP/IP printers are installed, based on information that is retrieved from either the new Printer Port Monitor Management Information Base (MIB) or Tcpmon.ini.

These features were introduced with Windows Vista.

### Port Monitor MIBs

An extended MIB specification for printers provides additional capacity for network card parameters. This extension allows customization of printer information that was stored only in Tcpmon.ini in Windows versions before Windows Vista.

By using this extended MIB, you can manage updates to printer information without needing to revise Tcpmon.ini. If the extended MIB is not implemented, the TCP port monitor will revert to using Tcpmon.ini.

For more information about the extended MIB specification, see the [Printer Port Monitor MIB v1.0](http://go.microsoft.com/fwlink/p/?linkid=526286) Printer Working Group document.

 

 




