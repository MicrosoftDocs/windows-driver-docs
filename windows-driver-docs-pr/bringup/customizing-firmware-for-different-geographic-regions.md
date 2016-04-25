---
title: Customizing firmware for different geographic regions
description: Systems will be sold in a variety of markets and geographies worldwide. To enable this, OEMs must define unique GUID values for those devices/system firmware which may require region-specific firmware.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 47E1C9EC-ED6E-4626-B61F-A19D1546FA08
---

# Customizing firmware for different geographic regions


Systems will be sold in a variety of markets and geographies worldwide. To enable this, OEMs must define unique GUID values for those devices/system firmware which may require region-specific firmware.

For example, region-specific firmware is frequently required for the Mobile Broadband (MBB) device. MBB device firmware is often customized for a specific Mobile Network Operator (MNO) in a particular region, to comply with local MNO and government regulations. To allow targeting of firmware to such devices, the OEM must assign a unique GUID to that device in the ESRT at the time of manufacture.

![two hardware-identical soc systems destined for different geographic locales](images/socsfordifferentlocales.png)

In the previous diagram, note that the system is identical in all respects, with the exception that the systems are destined for resale in different geographies. Therefore, the MBB device firmware in each system must be independently targetable and assigned a different GUID in the ESRT. This enables the MNO to target firmware updates to the system that is sold by them in their operating area. Similar consideration must be given to any device which may require custom firmware by geography or resale channel.

## Related topics


[System and device firmware updates via a firmware driver package](system-and-device-firmware-updates-via-a-firmware-driver-package.md)

[Populating the ESRT table](populating-the-esrt-table.md)

[Authoring a firmware update package](authoring-a-firmware-update-package.md)

[Certifying and signing the update package](certifying-and-signing-the-update-package.md)

[Installing the update](installing-the-update.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Customizing%20firmware%20for%20different%20geographic%20regions%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





