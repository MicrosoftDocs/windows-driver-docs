---
title: Device I/O from the UEFI environment
description: When the Windows OS loader calls the UpdateCapsule function, each capsule contained in the CapsuleHeaderArray is executed.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 843B177F-CD1F-47E6-8F35-0A0FFA8FA192
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Device%20I/O%20from%20the%20UEFI%20environment%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


