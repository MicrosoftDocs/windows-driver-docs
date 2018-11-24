---
title: Using Windows Update to Install Drivers
description: This topic describes how you can control when Windows Update distributes your driver.
ms.date: 06/15/2018
ms.topic: article
ms.localizationpriority: medium
---

# Understanding Windows Update Automatic and Optional Rules for Driver Distribution

> [!NOTE]
> The behaviors listed below apply to Windows 10 version 1709 and above.

This article describes how you can control when Windows Update distributes your driver.

When [submitting a driver to Windows Update](publish-a-driver-to-windows-update.md), the **Driver promotions** section presents two checkboxes: **Automatically deliver and install this driver during Windows Upgrade** and **Automatically deliver and install this driver on all applicable systems**.

![Automatic driver promotions checkboxes](images/automatic-driver-promotion-options.png)

If you select the first checkbox, the driver is classified as **Dynamic Update** (a term that applies to *upgrade* scenarios). Windows will then automatically preload this driver when upgrading the OS.

If you select the second checkbox, the driver is classified as **Automatic** (formerly known as **Critical update**); if you don't, the driver is classified as **Optional**.  In order to be published to Windows Update as **Automatic**, the driver must first have been evaluated by Microsoft through [Driver Flighting](driver-flighting.md).

## Automatic updates

During a scheduled update or when a user clicks **Check for updates** in the **Updates & Security** settings menu, Windows Update distributes only the highest-ranking **Automatic** drivers that apply to the system's devices.  Windows Update will only distribute **Optional** drivers in these scenarios if a device has no applicable drivers available in the Driver Store ("Driver Not Found") or if the only locally available driver is *generic*, i.e. a system-provided driver that provides only basic device functionality.

## Device plug-in ("Plug and Play")

When a device is connected to a Windows system, [Plug and Play (PnP)](../kernel/introduction-to-plug-and-play.md) looks for a compatible driver already available locally on the system. If one exists, Windows installs it on the device. Otherwise, Windows looks on Windows Update for a compatible driver, first matching the highest ranking **Automatic** driver on Windows Update. If no **Automatic** driver is available for the device, Windows proceeds to the highest ranking **Optional** driver.

The same logic applies when a plugged-in device has no applicable drivers available in the Driver Store ("Driver Not Found") or if the only locally available driver is *generic*.

## Device manager

When a user searches for updated drivers in Device Manager, Windows attempts to install the highest-ranking driver from Windows Update, regardless of whether it is classified as **Automatic** or **Optional**.

## Summary

Here's a table that summarizes the information above.

The first column indicates which of the two checkboxes in the **Driver promotions** section are checked. 
The first checkbox (**Automatically deliver and install this driver during Windows Upgrade**) is indicated by Dynamic Update, and the second (**Automatically deliver and install this driver on all applicable systems**) is indicated by Automatic. Windows Update is abbreviated WU.

|Driver promotions boxes checked|Windows Update (scheduled or via Updates & Security|OS Upgrades|Connect New Device|Device Manager|
|-|-|-|-|-|
|Automatic only|Yes|No|Only if the local driver is generic/ missing.|Yes|
|Dynamic Update only|Only if the local driver is generic/ missing, and WU has no applicable **Automatic** driver|Yes|Only if the local driver is generic/ missing, and WU has no applicable **Automatic** driver|Yes|
|Both|Yes|Yes|Only if the local driver is generic/ missing.|Yes|
|Neither|Only if the local driver is generic/ missing, and WU has no applicable **Automatic** driver|No|Only if the local driver is generic/ missing, and WU has no applicable **Automatic** driver|Yes|

<!--use word generic? or just condense descriptive text?-->
