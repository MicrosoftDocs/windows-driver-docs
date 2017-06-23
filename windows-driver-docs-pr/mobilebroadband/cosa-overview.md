---
title: COSA Overview
description: COSA Overview
ms.assetid: 45D69B8D-69C1-488B-AC52-D8DEB337F878
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# COSA Overview

This topic presents an overview of COSA (Country and Operator Settings Asset), the new format MOs use in Windows 10 Version 1703 and later to provision Windows devices for mobile broadband. The existing apndatabase.xml (APN database) from Windows 8, Windows 8.1, and versions of Windows 10 before Windows 10, version 1703 has been converted to COSA, which is ingestible by the new provisioning framework. Note that these previous versions of Windows will continue to use the older APN database for provisioning.

For more information about the older APN database, see [APN database overview](apn-database-overview.md).

For more information about the submission process for COSA and the APN database, see [COSA/APN database submission](cosa-apn-database-submission.md).

- [What are the settings that MOs can specify in COSA?](#settings)
- [What events trigger the application of new MO settings?](#events)
- [What SIM information from modems does COSA use?](#SIMinfo)
- [Is there an algorithm to make the best APN match?](#APNmatch)
- [Where is the COSA database stored, and can it be visually inspected like apndatabase.xml?](#location)
- [What happens when a device updates from Windows 10 Version 1607 (or earlier) to Windows 10 Version 1703? Are custom or manually created APNs migrated? Do they still have priority over the defaults from the database?](#update)

## <a href="" id="settings"></a> What are the settings that MOs can specify in COSA?

The settings are the same as what MOs configured in apndatabase.xml, with a few exceptions. For details, see the table in [Planning your COSA/APN database submission](planning-your-cosa-apn-database-submission.md).

## <a href="" id="events"></a> What events trigger the application of new MO settings?

Three events trigger the Windows provisioning engine to look for a change in settings: 
1.	The insertion or removal of a physical SIM (change in ICCID)
2.	Reconfiguration of an eSIM (change in ICCID)
3.	When the device boots

## <a href="" id="SIMinfo"></a> What SIM information from modems does COSA use?

For MO/MVNO discovery, Windows tries to make the best match for an available profile in the COSA database using SPN from the SIM in the modem.

## <a href="" id="APNmatch"></a> Is there an algorithm to make the best APN match?

In versions of Windows before Windows 10 Version 1703, MOs could specify an auto-connect order. Windows 10 Version 1703 and later continue to use a round-robin approach through all available APNs, but there is no longer a specific order that the algorithm uses.

## <a href="" id="location"></a> Where is the COSA database stored, and can it be visually inspected like apndatabase.xml?

COSA is in the format of a Windows 10 provisioning package (.ppkg). It is in the Windows\Provisioning\COSA\Microsoft folder. You can use a third-party tool, such as 7-Zip File Manager ([www.7-Zip.org](https://go.microsoft.com/fwlink/p/?linkid=844795)), to visually inspect its contents.

Note that OEM extensions to COSA, if specified in the device image, are in the COSA\OEM folder. For more information, see [Customize the Country and Operator Settings Asset](https://msdn.microsoft.com/windows/hardware/commercialize/customize/desktop/customize-cosa).

## <a href="" id="update"></a> What happens when a device updates from Windows 10 Version 1607 (or earlier) to Windows 10 Version 1703? Are custom or manually created APNs migrated? Do they still have priority over the defaults from the database?

COSA replaces apndatabase.xml after the upgrade. If an APN was provisioned in the previous version, whether custom, manual, or device-provisioned via the database, it is migrated as a part of the upgrade to Version 1703 and the device continues to use it for connectivity without requiring any additional action. Manually provisioned APNs still have priority over the defaults from the database just as they did in Version 1607 and earlier.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
