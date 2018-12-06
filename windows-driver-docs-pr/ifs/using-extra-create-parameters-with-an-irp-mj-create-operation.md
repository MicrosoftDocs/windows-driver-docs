---
title: Using Extra Create Parameters with an IRP_MJ_CREATE Operation
description: Using Extra Create Parameters with an IRP_MJ_CREATE Operation
ms.assetid: e32aeec6-1a0a-4d21-8358-89d9fc0a15eb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Extra Create Parameters with an IRP\_MJ\_CREATE Operation


Components of the operating system use extra create parameters (ECPs) to associate additional information with the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operation on a file. Drivers can also use ECPs to process or associate additional information with the IRP\_MJ\_CREATE operation on a file in the following situations:

-   When a kernel-mode driver calls the [**FltCreateFileEx2**](https://msdn.microsoft.com/library/windows/hardware/ff541939) or [**IoCreateFileEx**](https://msdn.microsoft.com/library/windows/hardware/ff548283) routine to create or open the file

-   When a file system filter driver processes the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operation for the file

The following sections describe how to define, attach, and use ECPs. The following sections also describe operating system-defined ECPs.

[Attaching ECPs to IRP\_MJ\_CREATE Operations that a Kernel-Mode Driver Originated](attaching-ecps-to-irp-mj-create-operations-that-a-kernel-mode-driver-o.md)

[Using ECPs to Process IRP\_MJ\_CREATE Operations in a File System Filter Driver](using-ecps-to-process-irp-mj-create-operations-in-a-file-system-filter.md)

[User-Defined ECPs](user-defined-ecps.md)

[System-Defined ECPs](system-defined-ecps.md)

 

 




