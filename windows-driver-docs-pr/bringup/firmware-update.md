---
title: Firmware update
description: Describes supports for delivering system and device firmware updates using Microsoft Windows Update( WU) and the UEFI UpdateCapsule function.
ms.date: 05/15/2018
ms.localizationpriority: medium
---


# Firmware update

Windows supports a platform for delivering system and device firmware updates wrapped in driver packages that are delivered using Microsoft Windows Update (WU) and then handed off to and processed in the UEFI **UpdateCapsule** function. This platform provides a consistent, reliable firmware update experience, and it improves the ability to deliver important system firmware updates for end-users.

This ability has been available as early as Windows 8.1. However, some recent changes require that firmware providers combine Computer Hardware ID (CHID) targeting along with a model unique EFI System Resource Table (ESRT) UEFI\_RES\\{UNIQUE ID} to more accurately target specific systems or range of systems.

A unique ID {UNIQUE ID} in the ESRT is critical. The purpose of the UNIQUE ID+CHID is so the firmware provider will be able to create a firmware update package/BIOS that will be deployed via Windows Update (WU) to all the systems that match the UNIQUE ID+CHID. Microsoft does not have a mechanism to validate the firmware package, and is dependent on the firmware provider (creator of package) to verify the payload has not been tampered with. It should be cryptographically verified; Checksum or other CRCs are not validation. If the payload fails validation it should fail and record status in ESRT as described in [ESRT table definition](https://docs.microsoft.com/windows-hardware/drivers/bringup/esrt-table-definition).

> [!NOTE]
> If the OEM, ODM, or persons tasked with populating the ESRT {UNIQUE ID} were to discover that the ESRT was pre-populated with a {Unique ID}, do not assume that this is unique. Populate the ESRT with your {UNIQUE ID} and record this for later use. Microsoft has guidance on how to create a UNIQUE ID, for these scenarios. This guidance is in the downloadable document for [Driver Publishing Workflow for Windows 10](http://download.microsoft.com/download/B/A/8/BA89DCE0-DB25-4425-9EFF-1037E0BA06F9/windows10_driver_publishing_workflow.docx).



## In this section

[Build and submit a firmware package to Windows Update (WU)](build-and-submit-a-firmware-package-to-windows-update.md)

[Target a system using CHID](target-a-system-using-chid.md)

[Firmware user experience (UX) best practices](firmware-user-experience-best-practices.md)

[Firmware update validation testing](firmware-update-validation-testing.md)






