---
title: Where Windows Searches for Drivers
description: Where Windows Searches for Drivers
ms.assetid: 4c193b97-7b70-425f-99f2-ba976a4cc40a
keywords:
- driver selections WDK device installations , where Device setupsearches
- locating drivers for device installation WDK device installations , where Device setupsearches
- searching for drivers during device installation WDK device installations , where Device setupsearches
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Where Windows Searches for Drivers


After a device is attached, Windows attempts to locate a matching [driver package](driver-packages.md) from which it can install a driver for the device. Windows searches for driver packages from various locations and performs this search in two phases, as described in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Search phase</th>
<th align="left">Windows 7</th>
<th align="left">Windows 8 and later versions of Windows</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Before a driver is installed</td>
<td align="left"><p>DevicePath</p>
<p>Windows Update</p>
<p><a href="driver-store.md" data-raw-source="[Driver store](driver-store.md)">Driver store</a></p></td>
<td align="left"><a href="driver-store.md" data-raw-source="[Driver store](driver-store.md)">Driver store</a></td>
</tr>
<tr class="even">
<td align="left">After initial driver is selected</td>
<td align="left"><p>Not applicable</p></td>
<td align="left"><p>DevicePath</p>
<p>Windows Update</p></td>
</tr>
</tbody>
</table>

 

### Searching for driver packages

After a device is attached, Windows first attempts to locate and install a driver in a trusted system context without user interaction, as follows:

-   The best matching driver that already exists in the driver store is first installed onto the device, allowing the device to begin operation quickly. In parallel and in a different process, the following will happen:

-   Windows automatically downloads matching [driver packages](driver-packages.md) from Windows Update. If a matching driver package is found, Windows downloads the package and stages it to the [driver store](driver-store.md). In Windows 10 version 1709 and greater, Windows offers the best ranked driver, which is not necessarily the most recent. Driver ranking considers HWID, date/version, and critical/automatic/optional category. Windows ranks critical or automatic drivers highest. If a matching driver is not found, WU looks next for optional drivers. As a result, an older critical driver of otherwise equal rank takes precedence over a newer optional driver. In Windows versions earlier than 1709, Windows offers critical and optional updates with equal precedence.

    Windows also searches for driver packages that were preloaded in the locations that are specified by the **DevicePath** registry value. This value is under the following subkey of the registry.

    ```cpp
    HKEY_LOCAL_MACHINE
       Software
          Microsoft
             Windows
                CurrentVersion
    ```

    By default, the **DevicePath** value specifies the %SystemRoot%\\INF directory.

    If a better matching driver package than was initially installed is found either on Windows Update or in a location that is specified by the **DevicePath** value, Windows first stages the driver package to the [driver store](driver-store.md) before the driver is installed. In this way, Windows always installs drivers from the driver store.

 

 





