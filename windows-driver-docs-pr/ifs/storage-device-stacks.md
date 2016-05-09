---
title: Storage Device Stacks
author: windows-driver-content
description: Storage Device Stacks
ms.assetid: dc2c532d-4ec6-4c97-bb94-429dd06f7b7c
keywords: ["filter drivers WDK file system , storage device stacks", "file system filter drivers WDK , storage device stacks", "storage device stacks WDK file system", "device stacks WDK file system", "device trees WDK file system", "PnP device trees WDK file system"]
---

# Storage Device Stacks


## <span id="ddk_storage_device_stacks_if"></span><span id="DDK_STORAGE_DEVICE_STACKS_IF"></span>


Most storage drivers are PnP device drivers, which are loaded and managed by the PnP Manager. Storage devices are represented in the PnP *device tree*, which contains a device node, or *devnode*, for every physical or logical device on the machine. It is important to note that file systems and file system filter drivers are not PnP device drivers; thus the PnP device tree contains no devnodes for them. For more information about the PnP device tree, see [Device Tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).

The devnode for a particular storage device contains the *storage device stack* for the device; this is the chain of attached device objects that represent the device's storage device drivers. Because a storage device, such as a disk, might contain one or more logical volumes (partitions or dynamic volumes), the storage device stack itself often looks more like a tree than a stack. The root of this tree is a functional device object (FDO) for a storage adapter or for another device stack that is integrated with the storage stack. The leaves of this tree are the physical device objects (PDO) for the logical volumes, also called storage volumes*,* on which file system volumes can be mounted.

For diagrams and descriptions of some typical storage device stacks, see the following sections of the Storage Devices Design Guide:

[Device Object Example for a SCSI HBA](https://msdn.microsoft.com/library/windows/hardware/ff552544)

[Device Object Example for an IEEE 1394 Controller](https://msdn.microsoft.com/library/windows/hardware/ff552532)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Storage%20Device%20Stacks%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


