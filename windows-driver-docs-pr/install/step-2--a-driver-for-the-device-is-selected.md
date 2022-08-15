---
title: Step 2 A Driver for the Device is Selected
description: Step 2 A Driver for the Device is Selected
ms.date: 11/18/2021
---

# Step 2: A Driver Package for the Device is Selected


After a [new device is detected and identified](step-1--the-new-device-is-identified.md), Windows and its device installation components follow these steps:

1.  Windows searches for matching [driver package](driver-packages.md) for the device. For more information about this step, see [Searching for a Driver Package](#searching-for-the-driver).
2.  Windows selects the most appropriate driver package(s) for the device from one or more driver packages. For more information about this step, see [Selecting the Driver](#selecting-the-driver).

### <a href="" id="searching-for-the-driver"></a>Searching for a Driver Package

Using the [hardware identifiers (IDs)](hardware-ids.md) and [compatible IDs](compatible-ids.md) that are reported by the [bus driver](../kernel/bus-drivers.md) for the device, Windows searches for [driver packages](driver-packages.md) that match that device. A driver package matches a device if a hardware ID or compatible ID on the device matches an ID in an [**INF *Models* section**](inf-models-section.md) entry of the driver package's [INF file](overview-of-inf-files.md).

As an example, on Windows 8 and later, if a user plugs a WLAN adapter into a port of a USB hub, the following steps occur:

-   After the USB hub driver creates a list of hardware IDs and compatible IDs for the WLAN adapter, Windows first searches the [Driver Store](driver-store.md) for a matching [driver package](driver-packages.md) for the device. If a driver package is found in the Driver Store, Windows installs it on the device. This allows the device to begin working quickly.

-   In a separate process, Windows searches Windows Update and the DevicePath for a better matching driver than what was installed from the Driver Store. If one is found, the driver is staged into the driver store, and then installed onto the device.

For more information about the [driver package](driver-packages.md) search process, see [Where Windows Searches for Drivers](./how-windows-selects-a-driver-for-a-device.md).

**Note**  Starting with Windows Vista, the operating system always installs a [driver package](driver-packages.md) from the [driver store](driver-store.md). If a matching driver package is found in another location, Windows first stages the package to the driver store before it installs the driver package on a device.

### Selecting the Driver

As soon as Windows has found one or more matching [driver packages](driver-packages.md) for the device, Windows selects the best driver package by following these steps:

1.  If Windows has found only one matching driver package, it installs that driver package on the device.

2.  If Windows has found multiple matching driver packages, Windows first assigns a ranking value to each match from each driver package. If only one driver has the lowest rank value, it installs that driver package on the device.

    For more information about the ranking process, see [How Windows Ranks Drivers](how-setup-ranks-drivers--windows-vista-and-later-.md).

3.  If multiple driver packages have the same lowest rank value, Windows uses the driver date and version to select the best driver package for the device. The date and version are specified by the [**INF DriverVer directive**](inf-driverver-directive.md) that is contained in the driver package's [INF file](overview-of-inf-files.md).

Once Windows has selected a driver package for the device, Windows installs the driver package as described in [Step 3: The Driver for the Device is Installed](step-3--the-driver-for-the-device-is-installed.md).
