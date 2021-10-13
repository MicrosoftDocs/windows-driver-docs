---
title: Introduction to Extra Create Parameters
description: Introduction to Extra Create Parameters
ms.date: 09/09/2021
ms.localizationpriority: medium
---

# Introduction to Extra Create Parameters

Extra create parameters (ECPs) are structures that can contain additional information for file creates. A create operation can have any number of ECPs, which are attached to the operation using an [**ECP_LIST**](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)). There are two types of ECPs:

* System-defined ECPs. Operating system components use system-defined ECPs to associate additional information with the [**IRP_MJ_CREATE**](./irp-mj-create.md) operation on a file.

* User-defined (or driver-defined) ECPs. Drivers can also use ECPs to process or associate additional information with the IRP_MJ_CREATE operation on a file in the following situations:

  * When a kernel-mode driver calls the [**FltCreateFileEx2**](/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltcreatefileex2) or [**IoCreateFileEx**](/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-iocreatefileex) routine to create or open the file.

  * When a file system filter driver processes the [**IRP_MJ_CREATE**](./irp-mj-create.md) operation for the file

The following sections describe how to define, attach, and use ECPs, and list system-defined ECPs.

* [Attaching ECPs to IRP_MJ_CREATE operations that a kernel-mode driver originated](attaching-ecps-to-irp-mj-create-operations-that-a-kernel-mode-driver-o.md)

* [Using ECPs to process IRP_MJ_CREATE operations in a file system minifilter](using-ecps-to-process-irp-mj-create-operations-in-a-file-system-minifilter.md)

* [User-defined ECPs](user-defined-ecps.md)

* [System-defined ECPs](system-defined-ecps.md)
