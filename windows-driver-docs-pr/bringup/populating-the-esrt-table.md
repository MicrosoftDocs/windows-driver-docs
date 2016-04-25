---
title: Populating the ESRT table
description: The EFI System Resource Table (ESRT) provides a mechanism for identifying integrated device and system firmware resources for the purposes of targeting firmware updates to those resources.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8C1FF785-7A05-4E10-9E38-C6AC597E3FA8
---

# Populating the ESRT table


The EFI System Resource Table (ESRT) provides a mechanism for identifying integrated device and system firmware resources for the purposes of targeting firmware updates to those resources. Each entry in the ESRT describes a device or system firmware resource that can be targeted by a firmware update driver package. Each firmware resource that can be updated by a firmware update driver package must be described by exactly one entry in the ESRT to enable firmware updates to be deployed and installed. For more details on the layout and implementation of the ESRT, see [ESRT table definition](esrt-table-definition.md).

The following diagram shows a high level block diagram of a typical SoC system.

![updatable firmware on a soc system](images/updatablefirmwareonsoc.png)

In this example, each system device containing updatable firmware is represented by a single block. Each block is capable of receiving and installing a targeted, independent firmware update for the device. As such, each block has a unique entry in the ESRT representing that device, as shown in the following diagram.

![soc system firmware resources](images/socfirmwareresources.png)

It is also possible for a device to have its firmware updated as part of a single, monolithic system firmware update driver package. In this case, the device would not have an ESRT entry since it is updated with the system firmware. More generally, a device can only have its firmware update targeted by one entry in the ESRT.

For simplicity, the previous diagram describes the model where each device has its firmware update targeted separately with a unique entry. Each GUID in the table identifies an updatable device or the UEFI system firmware within this SoC system. Each GUID in the table is unique (i.e. no two devices/system firmware share the same GUID value) and the table is unique to a single SoC system. Hardware revisions of a SoC system must define new GUID values for devices/system firmware. This ensures that firmware is targetable to each component in the revised hardware, as subtle differences in device hardware across revisions may require different firmware.

## Related topics
[System and device firmware updates via a firmware driver package](system-and-device-firmware-updates-via-a-firmware-driver-package.md)  
[Customizing firmware for different geographic regions](customizing-firmware-for-different-geographic-regions.md)  
[Authoring a firmware update package](authoring-a-firmware-update-package.md)  
[Certifying and signing the update package](certifying-and-signing-the-update-package.md)  
[Installing the update](installing-the-update.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Populating%20the%20ESRT%20table%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


