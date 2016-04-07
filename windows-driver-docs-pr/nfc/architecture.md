---
title: NFC class extension architecture
author: windows-driver-content
description: The NFC driver is implemented as a class extension and the underlying transport driver is implemented as the client driver.
ms.assetid: 9C68B3F7-CD83-4BDB-A4DD-11B7C1448301
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# NFC class extension architecture


The NFC driver is implemented as a class extension and the underlying transport driver is implemented as the client driver. The main advantage over a monolithic driver is that the client transport driver can be replaced in the future to support additional transports or to support specific needs of chip manufacturers for functionality that has not yet been standardized through the NFC Forum.

Support for the class extension is included in UMDF 2.0. Because the NFC stack has no dependency on core system components that are available in kernel mode and the performance requirements implied by a technology that is capped at 424Kbps, there is no reason for this driver to function in kernel mode.

| File          | Description                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NfcCx.dll     | This DLL contains the NFC class driver implementation. It has a dependency on UMDF and is installed via a component manifest. The DLL is a core system-compliant binary without any dependency above what is available in the core system. The DLL is indirectly linked to by the client driver via the NfcCxStub library that enables the client driver to load it and start its initialization. |
| NfcCxStub.lib | This file is the stub library that enables the client driver to perform load-time linking to NfcCx.dll without directly linking to NfcCx.lib.                                                                                                                                                                                                                                                     |

 

The NFC class extension driver is not expected to run in Update OS context. However, the driver is expected to run in Microsoft Manufacturing OS (MMOS) to perform end-of-line testing. The NFC client driver supplied by a chipset manufacturer can implement additional DDI support for manufacturing and end-of-line testing purposes, but that is outside the scope of this documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFC%20class%20extension%20architecture%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




