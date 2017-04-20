---
title: Maintaining an Operation Region Memory Buffer
author: windows-driver-content
description: Maintaining an Operation Region Memory Buffer
ms.assetid: 4abe82ec-d8c4-43c1-a72f-5114ba07160e
keywords:
- ACPI devices WDK , operation regions
- operation regions WDK ACPI
- function drivers WDK ACPI , operation regions
- WDM function drivers WDK ACPI , operation regions
- operation region memory buffer WDK ACPI
- memory buffers WDK ACPI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Maintaining an Operation Region Memory Buffer


## <a href="" id="ddk-maintaining-an-operation-region-memory-buffer-kg"></a>


The driver maintains an operation region memory buffer. The memory buffer contains the data fields associated with an operation region. The ACPI driver calls an operation region handler to access the data fields in an operation region memory buffer.

The operation region memory buffer must comply with the following:

-   The memory buffer must be allocated from nonpageable system memory.

-   The buffer size must be greater than or equal to the size of the operation region defined for the ACPI device.

-   The buffer must be allocated before the driver registers an operation region handler that accesses it, and maintained as long as the handler is registered.

For detailed information about constraints on operation regions, see the [Advanced Configuration and Power Interface Specification](http://go.microsoft.com/fwlink/p/?linkid=57185).

 

 


--------------------


