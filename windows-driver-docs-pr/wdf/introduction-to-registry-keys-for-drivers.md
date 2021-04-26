---
title: Introduction to Registry Keys for Drivers
description: Introduction to Registry Keys for Drivers
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

    The driver's **Parameters** key can contain configuration information for your driver and can be accessed by calling [**WdfDriverOpenParametersRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenparametersregistrykey). For Kernel-Mode Driver Framework (KMDF) drivers, this key is located in the appropriate **Services** tree for the driver. For User-Mode Driver Framework (UMDF) drivers, this key is located in the **HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF\\Services** tree, under the driver's service name. The subkey for the driver always uses the driver's service name, even if the driver binary's file name differs from the service name.

    When the system calls your driver's [**DriverEntry**](./driverentry-for-kmdf-drivers.md) routine, it passes the driver a path to the driver's key in the appropriate **Services** tree. Your driver must pass this path to [**WdfDriverCreate**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivercreate). Subsequently, the driver can obtain the path by calling [**WdfDriverGetRegistryPath**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivergetregistrypath).

-   Software key

    A driver's software key is also called its *driver key*. The system stores information about each driver under its software key.

    Your driver can call [**WdfFdoInitOpenRegistryKey**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey) and [**WdfDeviceOpenRegistryKey**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopenregistrykey) to open a device's software key.

    Your driver's INF file can contain [**INF AddReg directives**](../install/inf-addreg-directive.md) that set registry values under the software key using [**INF DDInstall sections**](../install/inf-ddinstall-section.md).

-   Hardware keys

    When a driver stack informs the Plug and Play (PnP) manager that a device is connected to the system, the PnP manager creates a hardware key for the device. This key is also called a *device key*. Settings related to the hardware (such as interrupt settings) can be stored here by drivers.

    Your driver can call [**WdfFdoInitOpenRegistryKey**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey) and [**WdfDeviceOpenRegistryKey**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopenregistrykey) to open a device's hardware key.

    Your driver's INF file can contain [**INF AddReg directives**](../install/inf-addreg-directive.md) that set registry values under the hardware key using [**INF DDInstall.HW sections**](../install/inf-ddinstall-hw-section.md).

To determine whether your driver type requires that you store information under specific registry keys, see the sections of this documentation that discuss your driver's device type by using the table of contents.

For more information about registry keys for drivers, see:

-   [Using the Registry in a Driver](../kernel/registry-key-object-routines.md)
