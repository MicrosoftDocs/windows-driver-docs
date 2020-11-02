---
title: Using Windows Update to Install Drivers
description: This topic describes how you can control when Windows Update distributes your driver.
ms.date: 05/28/2019
ms.topic: article
ms.localizationpriority: medium
---

# Understanding Windows Update rules for driver distribution

This article describes how you can control when Windows Update distributes your driver.

When [submitting a driver to Windows Update](publish-a-driver-to-windows-update.md), the **Driver Delivery Options** section presents two radio buttons: **Automatic** and **Manual**

Under the **Automatic** option there are two checkboxes: **Automatically delivered during Windows Upgrades** and **Automatically delivered to all applicable systems**. **Automatic** is the default setting for all new shipping labels.

![Automatic driver promotions checkboxes](images/driver-delivery-options.png)

When the first checkbox is selected, the driver is classified as a **Dynamic Update** (a term that applies to *upgrade* scenarios). Windows automatically preloads drivers in this category when upgrading the OS.

When the second checkbox is selected, the driver is downloaded and installed automatically on all applicable systems once it is released. All **Automatic** drivers must first have been evaluated by Microsoft through [Driver Flighting](driver-flighting.md).

For more info about the **Manual** option, see [Publish a driver to Windows Update](publish-a-driver-to-windows-update.md).

## Connecting new devices

When a device is connected to a Windows system, [Plug and Play (PnP)](../kernel/introduction-to-plug-and-play.md) looks for a compatible driver already available on the computer. If one exists, Windows installs it on the device. Otherwise, Windows searches Windows Update for a compatible driver, first matching the highest-ranking **Automatic** driver on Windows Update.

In Windows 10, version 1909 and earlier, if no **Automatic** driver is available for the device, Windows proceeds to the highest-ranking **Manual** driver.

Starting with Windows 10, version 2004, Windows does not search for a **Manual** driver when an **Automatic** driver is not available.

## Device Manager

In Windows 10, version 1909 and earlier, when a user searches for updated drivers in Device Manager, Windows attempts to install the highest-ranking driver from Windows Update, regardless of whether it is classified as **Automatic** or **Manual**.

Starting with Windows 10 version 2004, when a user searches for updated drivers in Device Manager, Windows only searches the local computer.

## Windows Update scan

During a Windows Update scan (be it scheduled or user-initiated,) Windows Update distributes only the highest-ranking **Automatic** drivers that apply to the system's devices.

In all versions of Windows 10, upon failing to find a driver, Device Manager recommends the user to try Windows Update. In version 1909 and earlier, this recommendation merely helped making sure that the Windows Update agent is in working condition. Starting with version 2004, it has become a functional recommmendation for reaching the **Automatic**, and eventually, the **Manual** drivers.

## "Optional updates" page

In Windows 10, version 1909 and earlier, Windows Update automatically distributes **Manual** drivers in either of the following scenarios:

* A device has no applicable drivers available in the Driver Store (raising a "driver not found" error), and there is no applicable **Automatic** driver
* A device has only a generic driver in the Driver Store, which provides only basic device functionality, and there is no applicable **Automatic** driver

Starting with Windows 10, version 2004, the Windows Update agent page in the Settings app has an "Optional updates" sub-page. This page distributes **Manual** drivers.

## Summary

Here's a table that summarizes the information above. "WU" stands for "Windows Update"

|Driver delivery options|OS upgrades|Connecting new device|Device Manager|WU scan|"Optional updates" page|
|-|-|-|-|-|-|
|Automatic (both checkboxes)|Yes|Only if the local driver is generic or missing|Only in Windows 10, version 1909 and earlier|Yes|No|
|Automatic (to all applicable systems)|No|Only if the local driver is generic or missing|Only in Windows 10, version 1909 and earlier|Yes|No|
|Automatic (during Windows Upgrades)|Yes|Only if the local driver is generic or missing|Only in Windows 10, version 1909 and earlier|Only if the local driver is generic or missing|No|
|Manual in Windows 10, version 1909 and earlier|No|Only if the local driver is generic or missing, and WU has no applicable **Automatic** driver|Yes|Only if the local driver is generic or missing, and WU has no applicable **Automatic** driver|N/A|
|Manual in Windows 10, version 2004 and later|No|No|No|No|Yes|

