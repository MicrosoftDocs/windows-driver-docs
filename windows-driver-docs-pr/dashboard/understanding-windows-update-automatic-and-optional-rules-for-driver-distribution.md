---
title: Using Windows Update to Install Drivers
description: This topic describes how you can control when Windows Update distributes your driver.
ms.date: 05/28/2019
ms.topic: article
ms.localizationpriority: medium
---

# Understanding Windows Update Automatic and Optional Rules for Driver Distribution

> [!NOTE]
> The behaviors listed below apply to Windows 10 Version 1709 and above. Please note the change in behavior for **Optional/Manual** driver updates in Windows 10 Version 2004 and above.

This article describes how you can control when Windows Update distributes your driver.

When [submitting a driver to Windows Update](publish-a-driver-to-windows-update.md), the **Driver Delivery Options** section presents two radio buttons: **Automatic** and **Manual**

Under the **Automatic** option there are two checkboxes: **Automatically delivered during Windows Updates** and **Automatically delivered to all applicable systems**. **Automatic** is the default setting for all new shipping labels.

![Automatic driver promotions checkboxes](images/driver-delivery-options.png)

When the first checkbox is selected, the driver is classified as **Dynamic Update** (a term that applies to *upgrade* scenarios). Windows will then automatically preload this driver when upgrading the OS.

When the second checkbox is selected, the driver will be downloaded and installed automatically on all applicable systems once it is released. All **Automatic** drivers must first have been evaluated by Microsoft through [Driver Flighting](driver-flighting.md).

If you like to publish the driver as **Optional/Manual**, you should select the **Manual** radio button.

## Automatic updates

During a scheduled update or when a user selects **Check for updates** in the **Updates & Security** settings menu, Windows Update distributes only the highest-ranking **Automatic drivers** that apply to the system's devices.

## Optional/Manual updates

In Windows Version 1909 and below, Windows Update will automatically distribute **Optional/Manual** drivers in the following scenarios:
* A device has no applicable drivers available in the Driver Store ("Driver Not Found"), and there is no applicable **Automatic** driver
* Or *if the only locally available driver is generic*. That is, the only locally available driver is a system-provided driver that provides only basic device functionality, and there is no applicable **Automatic** driver

## Device plug-in ("Plug and Play")

When a device is connected to a Windows system, [Plug and Play (PnP)](../kernel/introduction-to-plug-and-play.md) looks for a compatible driver already available locally on the system. If one exists, Windows installs it on the device. Otherwise, Windows looks on Windows Update for a compatible driver, first matching the highest-ranking **Automatic** driver on Windows Update.

In Windows Version 1909 and below, if no **Automatic** driver is available for the device, Windows proceeds to the highest-ranking **Optional/Manual** driver.

In Windows 10 Version 2004 and above, Windows will not search for an **Optional/Manual** driver when an **Automatic** driver is not available. **Optional/Manual** drivers could be access manually by a user by going to: *‘Settings > Update & Security > Windows Update > View optional updates > Driver updates’*.

## Device manager

In Windows Version 1909 and below, when a user searches for updated drivers in Device Manager, Windows attempts to install the highest-ranking driver from Windows Update, regardless of whether it is classified as **Automatic** or **Optional/Manual**.

In Windows 10 Version 2004 and above, a user could only search for driver updates locally from Device Manager. Any online search are done from the *Windows Update Settings page*.

## Summary

Here's a table that summarizes the information above.

The first column indicates the selection state in the **Driver Delivery Options** section. The first checkbox (**Automatically delivered during Windows Updates**) is indicated by Dynamic Update, and the second (**Automatically delivered to all applicable systems**) is indicated by Regular **Automatic** Update. **Manual** indicates **Optional/Manual** drivers, and Windows Update is abbreviated WU.

|Driver Delivery Options|OS Upgrades|Connect New Device|Device Manager|Windows Update daily scan or ‘Check for Updates’ button|Windows Update Optional page|
|-|-|-|-|-|-|
|Automatic (default)|Yes|Only if the local driver is generic or missing|Only in Windows Version 1909 and below|Yes|No|
|Regular Automatic Update only|No|Only if the local driver is generic or missing|Only in Windows Version 1909 and below|Yes|No|
|Dynamic Update only|Yes|Only if the local driver is generic or missing, and WU has no applicable **Automatic** driver|Only in Windows Version 1909 and below|Only if the local driver is generic or missing, and WU has no applicable **Automatic** driver|No|
| | | | | | |
|Manual in Windows Version 1909 and below|No|Only if the local driver is generic or missing, and WU has no applicable **Automatic** driver|Yes|Only if the local driver is generic or missing, and WU has no applicable **Automatic** driver|No|
|Manual in Windows 10 Version 2004 and above|No|No|No|No|No|

<!--use word generic? or just condense descriptive text?-->
