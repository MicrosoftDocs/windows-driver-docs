---
title: Storage Device Stacks
description: Storage Device Stacks
ms.assetid: dc2c532d-4ec6-4c97-bb94-429dd06f7b7c
keywords:
- filter drivers WDK file system , storage device stacks
- file system filter drivers WDK , storage device stacks
- storage device stacks WDK file system
- device stacks WDK file system
- device trees WDK file system
- PnP device trees WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Device Stacks


## <span id="ddk_storage_device_stacks_if"></span><span id="DDK_STORAGE_DEVICE_STACKS_IF"></span>


Most storage drivers are PnP device drivers, which are loaded and managed by the PnP Manager. Storage devices are represented in the PnP *device tree*, which contains a device node, or *devnode*, for every physical or logical device on the machine. It is important to note that file systems and file system filter drivers are not PnP device drivers; thus the PnP device tree contains no devnodes for them. For more information about the PnP device tree, see [Device Tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).

The devnode for a particular storage device contains the *storage device stack* for the device; this is the chain of attached device objects that represent the device's storage device drivers. Because a storage device, such as a disk, might contain one or more logical volumes (partitions or dynamic volumes), the storage device stack itself often looks more like a tree than a stack. The root of this tree is a functional device object (FDO) for a storage adapter or for another device stack that is integrated with the storage stack. The leaves of this tree are the physical device objects (PDO) for the logical volumes, also called storage volumes<em>,</em> on which file system volumes can be mounted.

For diagrams and descriptions of some typical storage device stacks, see the following sections of the Storage Devices Design Guide:

[Device Object Example for a SCSI HBA](https://msdn.microsoft.com/library/windows/hardware/ff552544)

[Device Object Example for an IEEE 1394 Controller](https://msdn.microsoft.com/library/windows/hardware/ff552532)

 

 




