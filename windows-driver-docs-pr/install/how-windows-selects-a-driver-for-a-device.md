---
title: How Windows selects a driver package for a device
description: How Windows selects a driver package for a device
keywords:
- driver selections WDK device installations , where Device setupsearches
ms.date: 07/19/2023
---

# How Windows selects a driver package for a device

When a device is attached, Windows needs to find a matching [driver package](driver-packages.md) to install.

In Windows 10, this matching process happens in two phases. First, Windows 10 installs the best matching driver package in the [driver store](driver-store.md), allowing the device to begin operation quickly. After that driver package is installed, Windows 10 also:

* Downloads any matching [driver packages](driver-packages.md) from Windows Update that are a better match for the device than what is currently on the system and puts them in the [driver store](driver-store.md).
  * Starting in Windows 10 version 1703, when you plug in a device, if there is already a matching driver package for the device in the driver store, the system does not search Windows Update until the next regularly scheduled daily scan, which could be up to 24 hours from when the device is plugged in.
* Searches for driver packages that were preloaded in the locations specified by the **DevicePath** registry value.  The **DevicePath** registry value is located under the following subkey: `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion`.  By default, the **DevicePath** value specifies the %SystemRoot%\\INF directory.

If Windows 10 finds a better matching driver package in those locations than was initially installed, Windows replaces the driver package it installed from the driver store with the better match.

In Windows versions before Windows 8, the driver package matching process looks only in **DevicePath**, if one is specified, and defaults to Windows Update otherwise.

The following table provides a quick summary of the information above:

|Search phase|Windows 7 search order|Windows 8, Windows 10 search order|
|--- |--- |--- |
|Initial driver package installation|**DevicePath**; Windows Update; [Driver store](driver-store.md)|[Driver store](driver-store.md)|
|After initial driver package is installed|Not applicable|**DevicePath**; Windows Update|


> [!NOTE]
> In Windows 10, version 1709 and greater, Windows Update (WU) offers the best matching driver package, which is not necessarily the most recent. The WU driver package selection process considers hardware ID, date/version, and critical/automatic/optional category. WU prioritizes critical or automatic driver packages highest. If a matching critical/automatic driver package is not found, WU looks next for optional driver packages. As a result, an older critical driver package of otherwise equal value takes precedence over a newer optional driver package.
> 
> Starting with Windows 10, version 2004, Windows Update (WU) automatically offers only the best automatic/critical matching driver package, searching both the computer and WU. To see matching driver packages in the optional category, go to **Settings > Update & Security > Windows Update > View optional updates > Driver updates**. WU still uses the same criteria to rank and select a driver.
