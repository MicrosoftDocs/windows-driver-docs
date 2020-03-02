---
title: How Windows selects a driver for a device
description: How Windows selects a driver for a device
ms.assetid: 4c193b97-7b70-425f-99f2-ba976a4cc40a
keywords:
- driver selections WDK device installations , where Device setupsearches
ms.date: 03/02/2020
ms.localizationpriority: High
---

# How Windows selects a driver for a device


When a device is attached, Windows needs to find a corresponding device driver to install.

In Windows 10, this matching process happens in two phases. First, Windows 10 installs the best matching driver in the driver store, allowing the device to begin operation quickly. While that driver is being installed, Windows 10 also:

* Downloads any matching [driver packages](driver-packages.md) from Windows Update and puts them in the [driver store](driver-store.md).
* Searches for driver packages that were preloaded in the locations specified by the **DevicePath** registry value.  The **DevicePath** registry value is located under the following subkey: `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion`.  By default, the **DevicePath** value specifies the %SystemRoot%\\INF directory.

If Windows 10 finds a better matching driver package than was initially installed, Windows replaces the driver it initially installed with the better match.

In Windows versions before Windows 8, the driver matching process looks only in **DevicePath**, if one is specified, and defaults to Windows Update otherwise.

The following table provides a quick summary of the information above:

|Search phase|Windows 7 match order|Windows 8, Windows 10 match order|
|--- |--- |--- |
|Before a driver is installed|**DevicePath**; Windows Update; [Driver store](driver-store.md)|[Driver store](driver-store.md)|
|After initial driver is selected|Not applicable|**DevicePath**; Windows Update|


> [!NOTE]
> In Windows 10 version 1709 and greater, Windows offers the best ranked driver, which is not necessarily the most recent. Driver ranking considers hardware ID, date/version, and critical/automatic/optional category. Windows ranks critical or automatic drivers highest. If a matching driver is not found, WU looks next for optional drivers. As a result, an older critical driver of otherwise equal rank takes precedence over a newer optional driver. In Windows versions earlier than 1709, Windows offers critical and optional updates with equal precedence.


