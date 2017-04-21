---
title: CM_PROB_NORMAL_CONFLICT
description: CM_PROB_NORMAL_CONFLICT
ms.assetid: 18c5ca02-0a4c-4a0e-8b33-5c685a73d4c8
keywords:
- CM_PROB_NORMAL_CONFLICT
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CM_PROB_NORMAL_CONFLICT


## <a href="" id="ddk-cm-prob-normal-conflict-dg"></a>


Two devices have been assigned the same I/O ports, the same interrupt, or the same DMA channel (either by the BIOS, the operating system, or a combination of the two).

### Error Code

12

### Display Message (Windows 2000 and later versions of Windows)

"This device cannot find enough free resources that it can use. (Code 12)

"If you want to use this device, you will need to disable one of the other devices on this system."

### Recommended Resolution - Windows Vista and later versions of Windows

[Use Device Manager](using-device-manager.md) to determine the source of the conflict and to resolve the conflict. For more information about how to resolve device conflicts, see the Help information about how to use Device Manager.

This error message can also appear if the BIOS did not allocate sufficient resources to a device. For example, this message will be displayed if the BIOS does not allocate an interrupt to a USB controller because of an invalid multiprocessor specification (MPS) table.

### Recommended Resolution − Windows Server 2003, Windows XP, and Windows 2000

To troubleshoot a device conflict, follow these steps:

1.  [Open Device Manager](using-device-manager.md).

2.  Double-click the icon that represents the device in the Device Manager window.

3.  On the device property sheet that appears, click **Troubleshoot** to start the hardware troubleshooter for the device.

This error message can also appear if the BIOS did not allocate sufficient resources to a device. For example, this message will be displayed if the BIOS does not allocate an interrupt to a USB controller because of an invalid multiprocessor specification (MPS) table.

For more information about how to resolve device conflicts, see the Help information about how to use Device Manager.

 

 





