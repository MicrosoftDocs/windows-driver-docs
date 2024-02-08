---
title: Windows 8 In-Box Graphics Drivers as Generic Drivers
description: Windows 8 in-box graphics drivers, including the MS Basic Display Driver (MSBDD), are all treated like generic drivers by Windows and Windows Update.
ms.date: 12/06/2018
---

# Windows 8 in-box graphics drivers treated as generic drivers

In this scenario, Windows 8 in-box graphics drivers, including the MS Basic Display Driver (MSBDD), are all treated like generic drivers by Windows and Windows Update.

This means that any newer matching graphics driver package on Windows Update is offered as an *Important* update.

If the default settings for Windows 8 Windows Update are being used, an Important driver update downloads and installs without user intervention, and often without the user noticing that this update occurred.

When Windows 8 ships, the in-box graphics drivers are significantly older than the latest driver updates on Windows Update. This behavior ensures that the user experiences Windows 8 by using the latest/best graphics driver available.

**Note**  
The Windows 8 certified OEM graphics drivers that is provided on new computers sold with Windows 8 pre-installed are not considered generic. A newer, matching graphics driver on Windows Update would be offered as an Optional update in these cases. The user must actively choose to install an Optional driver update.
