---
title: Introduction to Registry Keys for Drivers
description: Introduction to Registry Keys for Drivers
ms.assetid: ec1a21db-1a31-4041-941d-31156884ffae
keywords:
- registry WDK KMDF
- registry-key objects WDK KMDF
- framework-based drivers WDK KMDF , registry
- kernel-mode drivers WDK KMDF , registry
- KMDF WDK , registry
- Kernel-Mode Driver Framework WDK , registry
- Parameters key WDK KMDF
- software keys WDK KMDF
- driver keys WDK KMDF
- hardware keys WDK KMDF
- keys WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Registry Keys for Drivers


Drivers typically use a set of system-defined registry keys to store or access driver-specific or device-specific information. Your driver might access the following registry keys:

-   **Parameters** key

    The driver's **Parameters** key can contain configuration information for your driver. For Kernel-Mode Driver Framework (KMDF) drivers, this key is located in the [**HKLM\\SYSTEM\\CurrentControlSet\\Services**](https://msdn.microsoft.com/library/windows/hardware/ff546188) tree, under the driver's service name. For User-Mode Driver Framework (UMDF) drivers, this key is located in the **HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF\\Services** tree, under the driver's service name. The subkey for the driver always uses the driver's service name, even if the driver binary's file name differs from the service name.

    When the system calls your driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine, it passes the driver a path to the driver's **Services** tree. Your driver must pass this path to [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175). Subsequently, the driver can obtain the path by calling [**WdfDriverGetRegistryPath**](https://msdn.microsoft.com/library/windows/hardware/ff547187), and the driver can open its **Parameters** key by calling [**WdfDriverOpenParametersRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff547202).

    For more information about the **Parameters** key, see [The HKLM\\SYSTEM\\CurrentControlSet\\Services Tree](https://msdn.microsoft.com/library/windows/hardware/ff546188).

-   Software key

    A driver's software key is also called its *driver key* because the registry contains a software key for each driver. The registry contains a list of all of the device classes, and each driver's software key resides under its device class entry. The system stores information about each driver under its software key.

    Your driver can call [**WdfFdoInitOpenRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff547249) and [**WdfDeviceOpenRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff546804) to open its software key.

    For more information about software keys, see [The HKLM\\SYSTEM\\CurrentControlSet\\Control Tree](https://msdn.microsoft.com/library/windows/hardware/ff546165).

-   Hardware keys

    When a driver stack informs the Plug and Play (PnP) manager that a device is connected to the system, the PnP manager creates a hardware key for the device. This key is also called a *device key*. The PnP manager stores each device's unique identification information under the device's hardware key.

    Your driver can call [**WdfFdoInitOpenRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff547249) and [**WdfDeviceOpenRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff546804) to open a device's hardware key.

    For more information about hardware keys, see [The HKLM\\SYSTEM\\CurrentControlSet\\Enum Tree](https://msdn.microsoft.com/library/windows/hardware/ff546173).

Your driver's INF file can contain [**INF AddReg directives**](https://msdn.microsoft.com/library/windows/hardware/ff546320) that set registry values. INF files typically use [**INF DDInstall.HW sections**](https://msdn.microsoft.com/library/windows/hardware/ff547330) to set information under a device's hardware key.

To determine whether your driver type requires that you store information under specific registry keys, see the sections of this documentation that discuss your driver's device type by using the table of contents.

For more information about registry keys for drivers, see:

-   [Overview of Registry Trees and Keys](https://msdn.microsoft.com/library/windows/hardware/ff549538)

-   [Using the Registry in a Driver](https://msdn.microsoft.com/library/windows/hardware/ff565537)

 

 





