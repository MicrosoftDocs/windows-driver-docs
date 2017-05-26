---
title: Installing TCP/IP Printers
author: windows-driver-content
description: Installing TCP/IP Printers
ms.assetid: 15339cce-69aa-480d-bfee-11ea509ff5d4
keywords:
- TCP/IP WDK printer
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20TCP/IP%20Printers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


