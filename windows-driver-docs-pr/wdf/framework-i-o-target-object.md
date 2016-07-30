---
title: Framework I/O Target Object
author: windows-driver-content
description: Framework I/O Target Object
ms.assetid: 355a1818-88c9-4989-9141-8445f511f501
keywords: ["UMDF objects WDK , I/O target objects", "framework objects WDK UMDF , I/O target objects", "I/O target objects WDK UMDF", "IWDFIoTarget", "targets WDK UMDF"]
---

# Framework I/O Target Object


\[This topic applies to UMDF 1.*x*.\]

The framework I/O target object is exposed to drivers by the [IWDFIoTarget](https://msdn.microsoft.com/library/windows/hardware/ff559170) interface. It retrieves information about an I/O target, which typically represents a lower driver in the stack but can also represent another UMDF driver or the kernel-mode portion of the stack. The I/O target object provides UMDF drivers a way to send requests to another device.

UMDF drivers can also use the [IWDFIoTargetStateManagement](https://msdn.microsoft.com/library/windows/hardware/ff559198) interface to manage and monitor the state of an I/O target object.

 

 





