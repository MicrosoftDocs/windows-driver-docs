---
title: How the Volume Is Mounted
author: windows-driver-content
description: How the Volume Is Mounted
ms.assetid: e8f39b06-9904-40e8-af52-eae310d11fa7
keywords: ["filter drivers WDK file system , volume mount process", "file system filter drivers WDK , volume mount process", "mounting volumes WDK file systems", "volumes WDK file system , mounting"]
---

# How the Volume Is Mounted


How the volume is mounted depends on the file system and whether it has previously mounted the volume.

When a file system receives the volume mount request for a new volume, it creates a volume device object (VDO) for the volume. The VDO consists of a DEVICE\_OBJECT plus an optional file-system-defined device extension. The newly created VDO forms the base of the file system volume stack for the new (or remounted) volume.

The file system mounts the volume by associating the VDO with the volume parameter block (VPB) for the corresponding storage device object and sets the VPB\_MOUNTED flag on the VPB.

After the volume is mounted by the file system, file system filter drivers can attach to the top of the new file system volume stack. Any I/O requests sent to the file system are automatically sent first to the file system filter device object at the top of the volume stack. However, file system filters should only detach from the volume stack when the I/O Manager sends a fast I/O detach request to notify drivers on the volume stack that the volume is about to be removed.

**Note**   The storage device object for the volume resides in the storage device stack, but it is not necessarily the topmost device object in the stack. Moreover, even after the volume is mounted, storage filter drivers can still attach to the top of the storage stack. It is important for driver writers to keep in mind that, when the file system sends an IRP from the VDO to the storage device stack, it sends it to the storage device object for the volume, not the topmost device object in the stack. (However, when the I/O Manager sends an IRP directly to the storage stack, bypassing the file system, that IRP is sent to the topmost device object in the stack.)

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20How%20the%20Volume%20Is%20Mounted%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


