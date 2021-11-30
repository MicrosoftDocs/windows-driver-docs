---
title: Step 3 The Driver for the Device is Installed
description: Step 3 The Driver for the Device is Installed
ms.date: 11/18/2021
ms.localizationpriority: medium
---

# Step 3: The Driver Package for the Device is Installed

After Windows has selected the best driver package for the new device, Windows installs the driver package by following these steps:

1.  Based on directives within the [driver package's](driver-packages.md) [INF file](overview-of-inf-files.md), Windows installs the driver package on the device.  For example, it:

    -   Copies the driver binaries and other associated files to locations on the hard disk as specified by any relevant [**INF CopyFiles directive**](inf-copyfiles-directive.md).

    -   Performs registry operations as specified by any relevant [**INF AddReg directive**](inf-addreg-directive.md).

    -   Assigns a [device setup class](./overview-of-device-setup-classes.md) to the device from the **Class** and **ClassGuid** entries in the [**INF Version section**](inf-version-section.md).

2.  Once the driver package is installed on the device, the device will be restarted.

3.  As part of processing the device again due to the restart, the [Plug and Play (PnP) manager](pnp-manager.md) identifies the appropriate function driver and any optional filter drivers for the device and attempts to build the device stack and start the device. 

    The PnP manager calls the [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine for any required driver that is not yet loaded. The PnP manager then calls the [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine for each driver, starting with lower-filter drivers, then the function driver, and, finally, any upper filter drivers. The PnP manager assigns resources to the device, if required, and sends an [**IRP_MN_START_DEVICE**](../kernel/irp-mn-start-device.md) to the device's drivers.

As soon as this step is complete, the device is installed and ready to be used.

 

