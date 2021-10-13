---
title: How Windows selects a driver for a device
description: How Windows selects a driver for a device
keywords:
- driver selections WDK device installations , where Device setupsearches
ms.date: 03/02/2020
ms.localizationpriority: High
---

# How Windows selects a driver for a device


When a device is attached, Windows needs to find a corresponding device driver to install.

In Windows 10, this matching process happens in two phases. First, Windows 10 installs the best matching driver in the [driver store](driver-store.md), allowing the device to begin operation quickly. After that driver is installed, Windows 10 also:

* Downloads any matching [driver packages](driver-packages.md) from Windows Update and puts them in the [driver store](driver-store.md).
* Searches for driver packages that were preloaded in the locations specified by the **DevicePath** registry value.  The **DevicePath** registry value is located under the following subkey: `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion`.  By default, the **DevicePath** value specifies the %SystemRoot%\\INF directory.

If Windows 10 finds a better matching driver package in those locations than was initially installed, Windows replaces the driver it installed from the driver store with the better match.

In Windows versions before Windows 8, the driver matching process looks only in **DevicePath**, if one is specified, and defaults to Windows Update otherwise.

The following table provides a quick summary of the information above:

|Search phase|Windows 7 match order|Windows 8, Windows 10 match order|
|--- |--- |--- |
|Before a driver is installed|**DevicePath**; Windows Update; [Driver store](driver-store.md)|[Driver store](driver-store.md)|
|After initial driver is selected|Not applicable|**DevicePath**; Windows Update|


> [!NOTE]
> In Windows 10, version 1709 and greater, Windows offers the best matching driver, which is not necessarily the most recent. The driver selection process considers hardware ID, date/version, and critical/automatic/optional category. Windows prioritizes critical or automatic drivers highest. If a matching driver is not found, WU looks next for optional drivers. As a result, an older critical driver of otherwise equal value takes precedence over a newer optional driver.
> 
> Starting with Windows 10, version 2004, Windows automatically offers only the best automatic/critical matching driver, searching both the computer and Windows Update. To see matching drivers in the optional category, go to **Settings > Update & Security > Windows Update > View optional updates > Driver updates**. Windows still uses the same criteria to rank and select a driver.
