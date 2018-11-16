---
title: Color Management for Still Image Devices
description: Color Management for Still Image Devices
ms.assetid: dfc4afad-221a-436c-9124-981a74f70ee3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Color Management for Still Image Devices





Vendors should provide one or more color profiles for each still image device. Color profile file names should be included in the vendor-supplied INF file. If your device generates sRGB data, you can specify the system-supplied standard color profile, *sRGB Color Space Profile.icm*. The installer copies the supplied file names to one of the [registry entries for still image devices](registry-entries-for-still-image-devices.md).

If the device generates images using another color space, you will need to use a different color profile. Whether your device generates sRGB data or data in another color space, you will obtain the best results if you use a single color space consistently.

A still-image device must be made aware of the color space it sends its data to. For example, suppose that a user resets the gamma level (on a system that allows modification of the data source). The application will not be aware of this change.

For more information about color management, see the Microsoft Windows SDK documentation.

 

 




