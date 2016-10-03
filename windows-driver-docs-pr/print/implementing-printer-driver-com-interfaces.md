---
title: Implementing Printer Driver COM Interfaces
author: windows-driver-content
description: Implementing Printer Driver COM Interfaces
MS-HAID:
- 'custdrvr\_643cb933-1b70-4168-8d9a-5202d36fc6f3.xml'
- 'print.implementing\_printer\_driver\_com\_interfaces'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 39f873e9-7f72-420c-b6d6-dce31840aa16
keywords: ["printer driver customizing WDK , COM interfaces", "customizing printer drivers WDK , COM interfaces", "COM interfaces WDK print", "plug-ins WDK print"]
---

# Implementing Printer Driver COM Interfaces


## <a href="" id="ddk-implementing-printer-driver-com-interfaces-gg"></a>


This section explains how to construct a plug-in, based on WDK-supplied sample code. It also explains the calling sequences used for communication between the printer drivers and plug-ins. This section includes the following topics:

[Interface Identifiers for Printer Drivers](interface-identifiers-for-printer-drivers.md)

[Creating the Plug-In](creating-the-plug-in.md)

[Accessing Plug-In Interfaces from Printer Drivers](accessing-plug-in-interfaces-from-printer-drivers.md)

[Accessing Printer Driver Interfaces from Plug-Ins](accessing-printer-driver-interfaces-from-plug-ins.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Implementing%20Printer%20Driver%20COM%20Interfaces%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


