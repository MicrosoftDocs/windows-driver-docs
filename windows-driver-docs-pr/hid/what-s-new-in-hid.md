---
title: What's New in HID
description: This topic summarizes the new features and improvements for Human Interface Devices (HID) in Windows 10.
Search.SourceType: Video
ms.assetid: AA8590B4-AAEA-4D41-972F-38149CE328E2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What's New in HID


This topic summarizes the new features and improvements for Human Interface Devices (HID) in Windows 10.

## HID WinRT API


The [Windows.Devices.HumanInterfaceDevice](https://msdn.microsoft.com/library/windows/apps/xaml/dn263140) API lets a UWP app access devices that support the Human Interface Device (HID) protocol.

The following short video describes an end-to-end sample solution for HID that's available for download on the MSDN samples gallery. (This solution includes a sample app created using the new HID WinRT API.)

>[!VIDEO https://www.microsoft.com/videoplayer/embed/2d4da9fc-c2ea-4933-949d-eb0cff3c9c4e]

## Design Guide

The [Design Guide](index.md) has been updated to include some new topics. And also, existing content has been revised where relevant, to show improved HID support in Windows 10. Here are some of the new, and updated topics:

**New topic**

-   [ACPI button device](acpi-button-device.md)

**Updated topics**

-   [HID Transports](hid-transports.md)

-   [HID button drivers](buttons.md)

-   [HID Clients Supported in Windows](hid-clients-supported-in-windows.md)

## HID Over I²C


The HID protocol originally targeted human interface devices like: keyboards, mice, and joysticks. It was originally developed to run over USB. For Windows 8, Microsoft created a new HID miniport driver that allows devices to communicate over an Inter-Integrated Circuit (I²C) bus.

## Related topics
[Design Guide](index.md)  
[HID Over I2C](hid-over-i2c-guide.md)  



