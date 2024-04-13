---
title: Transport Minidriver Overview
description: This section contains details for vendors who need to create their own HID minidrivers. 
ms.date: 04/20/2017
---

# Transport Minidriver Overview

This section contains details for vendors who need to create their own HID minidrivers. If your device requires USB, Bluetooth, Bluetooth LE, I²C, GPIO as the transport, use the Microsoft-provided in-box driver. To see the list of in-box transport minidrivers, see [**HID Transports**](hid-transports.md).

For other transports, you will need to write transport minidrivers.

HID minidrivers can be written by using one of the following frameworks:

1.  UMDF – User Mode Driver Framework
2.  KMDF – Kernel Mode Driver Framework
3.  WDM – Legacy Windows Driver Model

**Note**  Microsoft encourages hardware vendors to use the in-box transport-minidrivers whenever possible. However, if your device requires an unsupported transport, Microsoft recommends using the Windows Driver Framework (UMDF or KMDF) as the driver model for your minidriver. You should only create a WDM minidriver if a specific transport is not supported by the Windows Driver Framework.

Microsoft recommends that developers use the UMDF framework as a starting point. Only if a functionality is not available to UMDF, consider writing a KMDF driver. For information about functionality comparison in the two driver frameworks, see Comparing UMDF 2 Functionality to KMDF.

With regard to HID Transport minidrivers, the KMDF model has the following caveats:

* Advantage: KMDF support is available in all Windows platforms that supports WDF. Required for all keyboard and mouse filter drivers.
* Challenge: Poorly written KMDF HID transport minidrivers can crash the system.

Here are HID-specific caveats for the UMDF model:

*  Advantage: UMDF is easier to develop and recommended for most vertical device classes. Errors in this driver do not bug check the whole system. For more information, see [**Advantages of Writing UMDF Drivers**](../wdf/advantages-of-writing-umdf-drivers.md).   
* Challenge: UMDF HID transport minidrivers are not supported on versions of Windows prior to Windows 8. A UMDF driver can receive I/O requests from a kernel-mode driver. Those transitions can have a slight performance impact.


## See Also
[**Getting Started with UMDF**](../wdf/getting-started-with-umdf-version-2.md) 


 




