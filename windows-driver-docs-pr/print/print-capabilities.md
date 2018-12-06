---
title: Print Capabilities
description: Print Capabilities
ms.assetid: 8ccbdab3-5be4-4ee1-9798-3b90e8b5b4d4
keywords:
- Print Capabilities WDK , about Print Capabilities
- XML PrintCapabilities WDK print
- PrintCapabilities document WDK print
- IPrintTicketProvider
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




