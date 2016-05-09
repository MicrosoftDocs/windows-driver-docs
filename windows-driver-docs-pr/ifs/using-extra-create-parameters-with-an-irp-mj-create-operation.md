---
title: Using Extra Create Parameters with an IRP\_MJ\_CREATE Operation
description: Using Extra Create Parameters with an IRP\_MJ\_CREATE Operation
ms.assetid: e32aeec6-1a0a-4d21-8358-89d9fc0a15eb
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Using%20Extra%20Create%20Parameters%20with%20an%20IRP_MJ_CREATE%20Operation%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




