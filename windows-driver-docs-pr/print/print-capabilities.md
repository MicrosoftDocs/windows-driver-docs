---
title: Print capabilities
description: Using print capabilities technology, a print driver can return its capabilities as a set of elements in an XML document.
keywords:
- Print Capabilities WDK , about Print Capabilities
- XML PrintCapabilities WDK print
- PrintCapabilities document WDK print
- IPrintTicketProvider
ms.date: 09/07/2022
---

# Print capabilities

By using print capabilities technology, a print driver can return its capabilities as a set of elements in an XML document. Earlier versions of print drivers returned their capabilities information when the application called the **DeviceCapabilities** or **GetDeviceCaps** functions. These Microsoft Win32 functions, however, are limited because they return only information about a fixed set of printer features and settings and can return information about only one feature or setting for each function call.

In contrast, the XML **PrintCapabilities** document is much more flexible and is designed to support new printer features. The **PrintCapabilities** function also returns the entire XML **PrintCapabilities** document in one function call.

This section covers the following aspects of print capabilities:

[Print capabilities architecture](print-capabilities-architecture.md)

[Win32 API support for print capabilities](win32-api-support-for-print-capabilities.md)

[Print capabilities in Unidrv and PScript5 print drivers](print-capabilities-in-unidrv-and-pscript5-print-drivers.md)

[Print driver plug-in support](print-driver-plug-in-support.md)

[Print capabilities support in GDI-based monolithic print drivers](print-capabilities-support-in-gdi-based--monolithic-print-drivers.md)
