---
title: Device I/O from the UEFI environment
description: When the Windows OS loader calls the UpdateCapsule function, each capsule contained in the CapsuleHeaderArray is executed.
ms.assetid: 843B177F-CD1F-47E6-8F35-0A0FFA8FA192
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device I/O from the UEFI environment


When the Windows OS loader calls the UpdateCapsule function, each capsule contained in the CapsuleHeaderArray is executed. The order of capsule execution is dependent on the UEFI firmware implementation, and a capsule cannot make any assumption as to the order of its execution relative to other capsules or take any dependencies on other capsules. Each capsule is a self-contained payload, comprising both the executable UEFI code to manage the update and the firmware image.

When the capsule is called, the executable code contained in the capsule is responsible for opening a communication channel with the target device. The appropriate channel will depend on the system’s device topology, the capabilities of the target device, and the UEFI boot services and drivers provided by the particular UEFI implementation. Capsule implementers may need to consult with the UEFI BIOS vendor regarding the options available in the targeted UEFI environment. Typically, communication is established by utilizing a UEFI device driver for the given device. This driver enables the capsule update code to bind to the device via a well-known device path using the appropriate protocol.

After communication is established, the update management code writes the firmware image to the targeted device. After completing the update, an appropriate return status code is written to the device’s Firmware Resource Entry in the ESRT. The update management code then returns control to the UpdateCapsule function.

For details on the UpdateCapsule function, the structure of a capsule, and UEFI boot services drivers and protocols, refer to the [UEFI specification](http://go.microsoft.com/fwlink/p/?LinkId=218221).

## Related topics
[ESRT table definition](esrt-table-definition.md)  
[Plug and play device](plug-and-play-device.md)  
[Authoring an update driver package](authoring-an-update-driver-package.md)  
[Processing updates](processing-updates.md)  
[Seamless crisis prevention and recovery](seamless-crisis-prevention-and-recovery.md)  
[Firmware update status](firmware-update-status.md)  



