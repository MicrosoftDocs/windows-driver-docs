---
title: COSA Database Overview and Frequently Asked Questions
description: The Country and Operator Settings Asset (COSA) database is used by mobile operators to provision Windows devices for mobile broadband.
ms.date: 05/21/2024
author: mhopkins-msft
ms.author: mhopkins
---

# COSA database overview and frequently asked questions

The Country and Operator Settings Asset (COSA) database is used by mobile operators (MOs) to provision Windows devices for mobile broadband.

To see a list of available settings MOs can configure in desktop COSA, see [Desktop COSA database settings](desktop-cosa-database-settings.md).

Here are some frequently asked questions about COSA:

## What are the settings that mobile operators can specify in COSA?

The settings are largely the same as what MOs configured in apndatabase.xml, with a few exceptions and new additions. For details, see the tables in [Planning your desktop COSA database submission](planning-your-desktop-cosa-database-submission.md).

## What events trigger the application of new mobile operator settings?

These events trigger the Windows provisioning engine to look for a change in settings:

1. The insertion or removal of a physical SIM (change in ICCID)
1. Reconfiguration of an eSIM (change in ICCID)
1. When the device boots

## What SIM information from modems does COSA use?

For MO/MVNO discovery, Windows tries to make the best match for an available profile in the COSA database using SPN from the SIM in the modem.

## Is there an algorithm to make the best APN match?

In versions of Windows before Windows 10, version 1703, MOs could specify an auto-connect order. Windows 10, version 1703 and later continue to use a round-robin approach through all available APNs, but there is no longer a specific order that the algorithm uses.

## Where is the COSA database stored, and can it be visually inspected like apndatabase.xml?

COSA is in the format of a Windows 10 provisioning package (.ppkg). It is in the Windows\Provisioning\COSA\Microsoft folder. You can use a third-party tool, such as [7-Zip File Manager](https://www.7-zip.org/), to visually inspect its contents.

Extensions to COSA, if specified in the device image, are in the COSA\OEM folder. For more information, see [Customize the Country and Operator Settings Asset](/windows-hardware/customize/desktop/customize-cosa).

## Are custom or manually created APNs migrated to the COSA database?

When upgrading to Windows 10, version 1703 or later, COSA replaces *apndatabase.xml* after the upgrade. If an APN was provisioned in the previous version, whether custom, manual, or device-provisioned via the database, it is migrated as a part of the upgrade to version 1703 and the device continues to use it for connectivity without requiring any additional action.

## Do custom or manually created APNs still have priority over the defaults from the database?

When upgrading to Windows 10, version 1703 or later, manually provisioned APNs still have priority over the defaults from the database just as they did in version 1607 and earlier.

## Why does the "Set as metered connection" setting sometimes change from Off to On?

Updates to the Windows operating system may include updates to the COSA database. If the database is updated, the provisioning engine may remove the cellular profiles. When the system restarts after database updates are installed, the provisioning engine reinstalls the cellular profiles. This operation resets user settings to their default values. For example, **Set as metered connection** changes from **Off** to **On**. This behavior is by design.
