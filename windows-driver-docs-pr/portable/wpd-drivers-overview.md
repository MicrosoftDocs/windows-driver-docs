---
description: Introduction to Windows Portable Devices (WPD) Drivers 
title: Introduction to WPD Drivers 
ms.date: 12/09/2024
---

# Introduction to Windows Portable Devices (WPD) Drivers 

Microsoft Windows Portable Devices (WPD) enable computers to communicate with attached media and storage devices. This system supersedes both Windows Media Device Manager (WMDM) and Windows Image Acquisition (WIA) by providing a flexible, robust way for a computer to communicate with music players, storage devices, mobile phones, and many other types of connected devices.

WPD provide an infrastructure to enable multifunction devices that store various media and non-media content. An example of a multi-function device is a cellular phone that contains a built-in zoom camera (a digital camera function) and supports music synchronization and playback (a portable media player function). Additionally, WPD make these devices accessible from a Windows-based computer.

The object-based Device-Driver Interface (DDI) enables convergent devices, initially focused on smart storage devices such as portable media players, digital still cameras, and mobile phones. Along with a DDI, Microsoft WPD implements a class driver solution for the following standard protocols and transports:

- Picture Transfer Protocol (PTP) over USB, IP, and Bluetooth
- Media Transfer Protocol (MTP) over USB, IP, and Bluetooth
- Mass Storage Class (MSC) over USB

If your device supports a unique protocol, you might need to develop your own driver. Use the User-Mode Driver Framework (UMDF) to write this driver. For more information about this framework, see [Getting started with UMDF](../wdf/getting-started-with-umdf-version-2.md).

For more information about applications that are written for Windows Portable Devices, see the [WPD SDK documentation](/windows/win32/windows-portable-devices).

For more information about both WPD driver development and WPD application development, see the [WPD Blog (Archive)](/archive/blogs/wpdblog/), which is accurate for Windows 10.

 

 




