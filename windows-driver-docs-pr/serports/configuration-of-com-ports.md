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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Configuration%20of%20COM%20Ports%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


