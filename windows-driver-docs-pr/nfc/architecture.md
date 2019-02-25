---
title: NFC class extension architecture
description: The NFC driver is implemented as a class extension and the underlying transport driver is implemented as the client driver.
ms.assetid: 9C68B3F7-CD83-4BDB-A4DD-11B7C1448301
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFC class extension architecture


The NFC driver is implemented as a class extension and the underlying transport driver is implemented as the client driver. The main advantage over a monolithic driver is that the client transport driver can be replaced in the future to support additional transports or to support specific needs of chip manufacturers for functionality that has not yet been standardized through the NFC Forum.

Support for the class extension is included in UMDF 2.0. Because the NFC stack has no dependency on core system components that are available in kernel mode and the performance requirements implied by a technology that is capped at 424Kbps, there is no reason for this driver to function in kernel mode.

| File          | Description                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NfcCx.dll     | This DLL contains the NFC class driver implementation. It has a dependency on UMDF and is installed via a component manifest. The DLL is a core system-compliant binary without any dependency above what is available in the core system. The DLL is indirectly linked to by the client driver via the NfcCxStub library that enables the client driver to load it and start its initialization. |
| NfcCxStub.lib | This file is the stub library that enables the client driver to perform load-time linking to NfcCx.dll without directly linking to NfcCx.lib.                                                                                                                                                                                                                                                     |

 

The NFC class extension driver is not expected to run in Update OS context. However, the driver is expected to run in Microsoft Manufacturing OS (MMOS) to perform end-of-line testing. The NFC client driver supplied by a chipset manufacturer can implement additional DDI support for manufacturing and end-of-line testing purposes, but that is outside the scope of this documentation.

 
 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  

