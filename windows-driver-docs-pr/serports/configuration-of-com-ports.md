---
title: Configuration of COM Ports
author: windows-driver-content
description: Configuration of COM Ports
ms.assetid: 519ca9c8-bc67-4a85-87ae-6015c6212dea
keywords:
- COM ports WDK serial devices
- serial devices WDK , COM ports
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Configuration of COM Ports


## <a href="" id="ddk-configuration-of-com-ports-kg"></a>


Starting with Windows 2000, a COM port is a type of serial port that complies with the following additional requirements:

-   You access the COM port through an instance of the COM port device interface class. The GUID for this class is GUID\_DEVINTERFACE\_COMPORT, which is defined in Ntddser.h.

-   You operate the COM port by using the 16550 UART-compatible interface that is defined in Ntddser.h.

-   To ensure compatibility with most applications that access COM ports, you should assign a symbolic link name that uses the standard naming convention "COM*&lt;n&gt;*", where *&lt;n&gt;* is the COM port number (for example, COM1). If you use a COM*&lt;n&gt;* name, you must obtain the COM port number *&lt;n&gt;* from the [COM port database](com-port-database.md). COM port numbers should only be used with COM*&lt;n&gt;* names.

By default, the combined operation of the class installer for the Ports [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) and the Serial function driver configure a device as a COM port.

For information about how the Ports class installer and Serial create a COM port device interface for a COM port, see [External Naming of COM Ports](external-naming-of-com-ports.md).

 

 




