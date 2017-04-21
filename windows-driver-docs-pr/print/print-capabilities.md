---
title: Print Capabilities
author: windows-driver-content
description: Print Capabilities
ms.assetid: 8ccbdab3-5be4-4ee1-9798-3b90e8b5b4d4
keywords:
- Print Capabilities WDK , about Print Capabilities
- XML PrintCapabilities WDK print
- PrintCapabilities document WDK print
- IPrintTicketProvider
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Print Capabilities


By using the Print Capabilities technology, a print driver can return its capabilities as a set of elements in an XML document. Earlier versions of print drivers returned their capabilities information when the application called the **DeviceCapabilities** or **GetDeviceCaps** functions. These Microsoft Win32 functions, however, are limited because they return only information about a fixed set of printer features and settings and can return information about only one feature or setting for each function call.

In contrast, the XML PrintCapabilities document is much more flexible and is designed to support new printer features. The PrintCapabilities function also returns the entire XML PrintCapabilities document in one function call.

This section covers the following aspects of Print Capabilities:

[Print Capabilities Architecture](print-capabilities-architecture.md)

[Win32 API Support for Print Capabilities](win32-api-support-for-print-capabilities.md)

[Print Capabilities in Unidrv and PScript5 Print Drivers](print-capabilities-in-unidrv-and-pscript5-print-drivers.md)

[Print Driver Plug-in Support](print-driver-plug-in-support.md)

[Print Capabilities Support in GDI-based, Monolithic Print Drivers](print-capabilities-support-in-gdi-based--monolithic-print-drivers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Capabilities%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


