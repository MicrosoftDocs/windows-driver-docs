---
title: Step 2 A Driver for the Device is Selected
description: Step 2 A Driver for the Device is Selected
ms.assetid: 2134cab6-58ea-4258-9a45-09bf54156e0a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Step 2: A Driver for the Device is Selected


After a new device is detected and identified, Windows and its [device installation components](https://msdn.microsoft.com/library/windows/hardware/ff541277) follow these steps:

1.  Windows searches for an appropriate [driver package](driver-packages.md) for the device. For more information about this step, see [Searching for the Driver Package](#searching-for-the-driver).
2.  Windows selects the most appropriate driver for the device from one or more driver packages. For more information about this step, see [Selecting the Driver](#selecting-the-driver).

### <a href="" id="searching-for-the-driver"></a>Searching for the Driver Package

Using the [hardware identifier (ID)](hardware-ids.md) that is reported by the bus or hub driver, Windows searches for [driver packages](driver-packages.md) that match a device. A driver package matches a device if the hardware ID matches a hardware ID or [compatible ID](compatible-ids.md) in an [**INF *Models* section**](inf-models-section.md) entry of the driver package's [INF file](inf-files.md).

Depending on the operating system version, Windows searches for matching driver packages in various locations as described in the following table.

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

 

For example, if a user plugs a wireless local area network (WLAN) adapter into a port of a USB hub on a computer that is running Windows 7, the following steps occur:

-   After the USB hub driver creates a list of hardware IDs for the WLAN adapter, Windows first searches the [driver store](driver-store.md) for a matching [driver package](driver-packages.md) for the device.

-   The device installation process searches for a matching driver package from one of the following locations:

    -   The Universal Naming Convention (*UNC*) paths that are identified by the **DevicePath** registry value of **HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion**.

    -   Windows Update

    -   The distribution medium that the independent hardware vendor (IHV) provided for the device.

    If a driver package is found, Windows stages the package into the driver store from which the driver for the device will be installed.

**Note**  Starting with Windows Vista, the operating system always installs a [driver package](driver-packages.md) from the [driver store](driver-store.md). If a matching driver package is found in another location, Windows first stages the package to the driver store before it installs the driver for the device.

 

As another example, if a user plugs a WLAN adapter into a port of a USB hub on a computer that is running Windows 8, the following steps occur:

-   After the USB hub driver creates a hardware ID for the WLAN adapter, Windows first searches the driver store for a matching [driver package](driver-packages.md) for the device. If a driver package is found in the driver store, Windows installs it on the device. This allows the device to begin working quickly.

-   In a separate process, Windows searches Windows Update and the DevicePath for a better matching driver than was installed. If one is found, the driver is staged into the driver store, and then installed onto the device.

For more information about the [driver package](driver-packages.md) search process, see [Where Windows Searches for Drivers](where-setup-searches-for-drivers.md).

### Selecting the Driver

As soon as Windows has found one or more matching [driver packages](driver-packages.md) for the device, Windows selects the best driver by following these steps:

1.  If Windows has found only one matching driver package, it installs the driver from that package for the device.

2.  If Windows has found multiple matching driver packages, Windows first assigns a ranking value to the driver from each driver package. If only one driver has the lowest rank value, it installs the driver from that package for the device.

    For more information about the ranking process, see [How Windows Ranks Drivers](how-setup-ranks-drivers.md).

3.  If multiple drivers have the same lowest rank value, Windows uses the following criteria to select the best driver for the device:

    -   Whether the driver is digitally signed. Starting with Windows Vista, Windows always selects a signed driver instead of an unsigned driver regardless of other selection criteria. For more information about digital signatures for drivers, see [Driver Signing](driver-signing.md).

    -   The driver date and version, where the date and version are specified by the [**INF DriverVer directive**](inf-driverver-directive.md) that is contained in the driver package's [INF file](inf-files.md).

Once Windows has selected a driver for the device, Windows installs the driver as described in [Step 3: The Driver for the Device is Installed](step-3--the-driver-for-the-device-is-installed.md).

For more information about how drivers are selected for a device, see [How Windows Selects Drivers](how-setup-selects-drivers.md).

 

 





