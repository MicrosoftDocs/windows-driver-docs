---
title: IRP-Based I/O Operations That use Neither Buffered Nor Direct I/O
description: IRP-Based I/O Operations That Always Use Neither Buffered Nor Direct I/O
ms.assetid: 2d757904-e46c-476d-896c-77beacfe4b7c
keywords:
- neither buffered nor direct I/O WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IRP-Based I/O Operations That Always Use Neither Buffered Nor Direct I/O


## <span id="ddk_irp_based_io_operations_that_always_use_neither_buffered_nor_direc"></span><span id="DDK_IRP_BASED_IO_OPERATIONS_THAT_ALWAYS_USE_NEITHER_BUFFERED_NOR_DIREC"></span>


The following IRP-based I/O operations always use neither buffered nor direct I/O, regardless of the value of the **Flags** member of the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure for the file system volume:

-   IRP\_MJ\_PNP

-   IRP\_MJ\_QUERY\_SECURITY

-   IRP\_MJ\_SET\_SECURITY

-   IRP\_MJ\_SYSTEM\_CONTROL

 

 




