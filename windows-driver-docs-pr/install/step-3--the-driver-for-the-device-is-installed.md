---
title: Step 3 The Driver for the Device is Installed
description: Step 3 The Driver for the Device is Installed
ms.assetid: 292c5ffe-fbdf-42b8-9642-024c78709843
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Step 3: The Driver for the Device is Installed


After Windows has selected the best driver for the new device, it saves information about the device and driver in the following way:

-   Multiple devices of the same model and version can be connected to the computer. Each device connection is known as a [*device instance*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-instance).

    Windows represents each device instance as a unique device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)). A devnode contains information about the device, such as whether the device was started and which drivers have registered for notification on the device.

-   Windows represents a driver for the device as a [*driver node*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-node). A driver node is based on the information from a matching device entry within the [**INF *Models* section**](inf-models-section.md) of the [driver package's](driver-packages.md) [INF file](inf-files.md). A driver node includes all the software support for a device, such as any services, device-specific co-installers, and registry entries.

As soon as the device and driver are instantiated, Windows installs the driver by following these steps:

1.  Based on directives within the [driver package's](driver-packages.md) [INF file](inf-files.md), Windows does the following:

    -   Copies the driver binaries and other associated files to locations on the hard disk as specified by the [**INF CopyFiles directive**](inf-copyfiles-directive.md).

    -   Performs any device-instance related configuration, such as registry key writes.

2.  Windows determines the [device setup class](device-setup-classes.md) from the **Class** and **ClassGuid** entries in the [**INF Version section**](inf-version-section.md) of the [driver package's](driver-packages.md) [INF file](inf-files.md). To optimize device installation, devices that are set up and configured in the same manner are grouped into the same device setup class.

3.  As soon as the driver files are copied, Windows transfers control to the [Plug and Play (PnP) manager](pnp-manager.md). The PnP manager loads the drivers and starts the device.

4.  The PnP manager loads the appropriate function driver and any optional filter drivers for the device.

    The PnP manager calls the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine for any required driver that is not yet loaded. The PnP manager then calls the [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine for each driver, starting with lower-filter drivers, then the function driver, and, finally, any upper filter drivers. The PnP manager assigns resources to the device, if required, and sends an [**IRP_MN_START_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) to the device's drivers.

As soon as this step is complete, the device is installed and ready to be used.

 

 





