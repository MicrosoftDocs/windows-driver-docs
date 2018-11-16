---
title: Creating an INF File
description: Creating an INF File
ms.assetid: c45fb42c-f0d6-4ab8-9a19-4bbf98c4cf8c
keywords:
- joysticks WDK HID , INF files
- virtual joystick drivers WDK HID , INF files
- VJoyD WDK HID , INF files
- INF files WDK joysticks
- INF files WDK joysticks , creating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating an INF File





All minidrivers and OEM-defined joysticks should be installed using an INF file to provide all the necessary information to the system. An INF file describes a device installation in terms of the class of the device, the files that need to be copied, any compatible devices, any system resources the device requires, and changes to the registry. INF files for customizing the standard analog driver do not need to copy any files, state compatible devices, or specify system resources. The INF file can specify other actions, such as modifying the Autoexec.bat file, but this is not usually necessary for a joystick minidriver.

The INF file contains the elements described in the following topics:

[Setting the Device Class](setting-the-device-class.md)

[Selecting Source Files](selecting-source-files.md)

[Setting the Manufacturer-Specific Data](setting-the-manufacturer-specific-data.md)

[Setting Up LogConfig Entries](setting-up-logconfig-entries.md)

[Setting Up AddReg Entries](setting-up-addreg-entries.md)

 

 




