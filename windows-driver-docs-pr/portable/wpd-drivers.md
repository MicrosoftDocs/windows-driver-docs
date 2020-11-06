---
description: WPD Drivers
title: WPD Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WPD Drivers

Microsoft Windows Portable Devices (WPD) enable computers to communicate with attached media and storage devices. This system supersedes both Windows Media Device Manager (WMDM) and Windows Image Acquisition (WIA) by providing a flexible, robust way for a computer to communicate with music players, storage devices, mobile phones, and many other types of connected devices.

Microsoft provides several drivers for standard protocols and devices, including Picture Transfer Protocol (PTP), Media Transfer Protocol (MTP) devices, and Mass Storage Class (MSC) devices. If your device supports a unique protocol, you might need to develop your own driver. Use the User-Mode Driver Framework (UMDF) to write this driver. For more information about this framework, see [Getting started with UMDF](../wdf/getting-started-with-umdf-version-2.md).

For more information about applications that are written for Windows Portable Devices, see the [WPD SDK documentation](/windows/win32/windows-portable-devices).

For more information about both WPD driver development and WPD application development, see the [WPD Blog (Archive)](/archive/blogs/wpdblog/), which is accurate for Windows 10.