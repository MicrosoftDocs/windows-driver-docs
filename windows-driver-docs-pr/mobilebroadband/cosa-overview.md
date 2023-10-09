---
title: COSA overview
description: COSA overview
ms.date: 04/20/2017
---

# COSA overview

COSA, or Country and Operator Settings Asset, is the data format that mobile operators (MOs) use in Windows 10, version 1703 and later to provision Windows devices for mobile broadband. The existing Access Point Name (APN) database (apndatabase.xml) from Windows 8, Windows 8.1, and versions of Windows 10 before 1703 has been converted to COSA, which is ingestible by the new provisioning framework. These previous versions of Windows continue to use the older APN database for provisioning desktop devices.

For more information about the older APN database, see [APN database overview](apn-database-overview.md).

To see a list of available settings MOs can configure in desktop COSA, see [Desktop COSA database settings](desktop-cosa-database-settings.md).

## FAQ

- [What are the settings that MOs can specify in COSA?](#settings)
- [What events trigger the application of new MO settings?](#events)
- [What SIM information from modems does COSA use?](#SIMinfo)
- [Is there an algorithm to make the best APN match?](#APNmatch)
- [Where is the COSA database stored, and can it be visually inspected like apndatabase.xml?](#location)
- [What happens when a device updates from Windows 10, version 1607 (or earlier) to Windows 10, version 1703? Are custom or manually created APNs migrated? Do they still have priority over the defaults from the database?](#update)
- [Why does the **Set as metered connection** setting sometimes change from **Off** to **On**?](#metered)

### <a href="" id="settings"></a> What are the settings that MOs can specify in COSA?

The settings are largely the same as what MOs configured in apndatabase.xml, with a few exceptions and new additions. For details, see the tables in [Planning your desktop COSA/APN database submission](planning-your-desktop-cosa-apn-database-submission.md).

### <a href="" id="events"></a> What events trigger the application of new MO settings?

Three events trigger the Windows provisioning engine to look for a change in settings: 

1.	The insertion or removal of a physical SIM (change in ICCID)
2.	Reconfiguration of an eSIM (change in ICCID)
3.	When the device boots

### <a href="" id="SIMinfo"></a> What SIM information from modems does COSA use?

For MO/MVNO discovery, Windows tries to make the best match for an available profile in the COSA database using SPN from the SIM in the modem.

### <a href="" id="APNmatch"></a> Is there an algorithm to make the best APN match?

In versions of Windows before Windows 10, version 1703, MOs could specify an auto-connect order. Windows 10, version 1703 and later continue to use a round-robin approach through all available APNs, but there is no longer a specific order that the algorithm uses.

### <a href="" id="location"></a> Where is the COSA database stored, and can it be visually inspected like apndatabase.xml?

COSA is in the format of a Windows 10 provisioning package (.ppkg). It is in the Windows\Provisioning\COSA\Microsoft folder. You can use a third-party tool, such as 7-Zip File Manager ([www.7-Zip.org](https://go.microsoft.com/fwlink/p/?linkid=844795)), to visually inspect its contents.

Note that OEM extensions to COSA, if specified in the device image, are in the COSA\OEM folder. For more information, see [Customize the Country and Operator Settings Asset](/windows-hardware/customize/desktop/customize-cosa).

### <a href="" id="update"></a> What happens when a device updates from Windows 10, version 1607 or earlier to Windows 10, version 1703 or later? Are custom or manually created APNs migrated? Do they still have priority over the defaults from the database?

COSA replaces apndatabase.xml after the upgrade. If an APN was provisioned in the previous version, whether custom, manual, or device-provisioned via the database, it is migrated as a part of the upgrade to version 1703 and the device continues to use it for connectivity without requiring any additional action. Manually provisioned APNs still have priority over the defaults from the database just as they did in version 1607 and earlier.

### <a href="" id="metered"></a>Why does the "Set as metered connection" setting sometimes change from **Off** to **On**?

Updates to the Windows operating system may include updates for the COSA database. If the database is updated, the provisioning engine may remove the cellular profiles. When the system restarts after database updates are installed, the provisioning engine reinstalls the cellular profiles. This operation resets user settings to their default values. For example, **Set as metered connection** changes from **Off** to **On**. This behavior is by design.
