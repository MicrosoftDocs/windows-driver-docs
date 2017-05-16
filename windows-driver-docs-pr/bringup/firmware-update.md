---
title: Firmware update
description: Describes supports for delivering system and device firmware updates using Microsoft Windows Update( WU) and the UEFI UpdateCapsule function.
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# Firmware update

Windows supports a platform for delivering system and device firmware updates wrapped in driver packages that are delivered using Microsoft Windows Update(WU) and then handed off to and processed in UEFI UpdateCapsule function. This platform provides a consistent, reliable firmware update experience, and it improves the discoverability of important system firmware updates for end-users.

This ability has been available as early as Windows 8, however, Microsoft is now requiring that firmware providers combine Computer Hardware ID (CHID) targeting along with a model unique EFI System Resource Table(ESRT) UEFI\_RES\\ {UNIQUE ID} to more accurately target specific systems or range of systems.


A unique model {UNIQUE ID} in the ESRT is critical. The purpose of the UNIQUE ID+CHID is so the firmware provider will be able to create a firmware update package/BIOS that will be deployed via Windows Update(WU) to all the systems that match the UNIQUE ID +CHID. Microsoft does not have a mechanism to validate the firmware package, and is dependent on the firmware provider (creator of package) to verify the payload has not been tampered with. It should be cryptographically verified; Checksum or other CRCs are not validation. If payload fails validation it should fail and record status in ESRT as described in [ESRT table definition](https://msdn.microsoft.com/en-us/windows/hardware/drivers/bringup/esrt-table-definition)

**Note** If OEM/ODM or person tasked with populating the ESRT {UNIQUE ID} were to discover that the ESRT was pre-populated with a {Unique ID}, do not assume that this is unique. Populate the ESRT with your {UNIQUE ID} and record this for later use. Microsoft has guidance on how to create a UNIQUE ID, for these scenarios. This guidance is in the downloadable document for [Driver Publishing Workflow for Windows 10](http://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx)



## In this section

[Build and submit a firmware package to Windows Update (WU)](build-and-submit-a-firmware-package-to-windows-update.md)

[Target a system using CHID](target-a-system-using-chid.md)

[Firmware user experience (UX) best practices](firmware-user-experience-best-practices.md)

[Firmware update validation testing](firmware-update-validation-testing.md)




--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


