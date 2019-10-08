---
title: Component Firmware Update (CPU) host driver
description: Component Firmware Update (CPU) host driver TBD
ms.date: 10/07/2019
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# CFU Driver Sample

The CFU driver sample sends firmware image file(s) to a device in need of an update. Before sending the firmware image, the driver sends several commands to the device with firmware offers. Only if the device accepts, the driver sends the firmware payload. The communication between the driver and the device is in accordance with the [CFU protocol](https://github.com/Microsoft/CFU/tree/master/Documentation/CFU-Protocol), an open source specification (included with CFU) based on the HID protocol.

The CFU driver sample is implemented using the [User-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/overview-of-the-umdf) 2.0 model and based on the the [Microsoft Devices Driver Module Framework (DMF)](https://blogs.windows.com/buildingapps/2018/08/15/introducing-driver-module-framework/).
As a firmware developer, you can customize the driver for the purposes of adopting the CFU model to enable firmware updates for your component(s). For more information, see [Customizing the Component Firmware Update Driver](https://github.com/Microsoft/CFU/blob/master/Documentation/CFU-Driver/cfu-driver.md).

## File manifest

| File | Description |
| --- | --- |
| ComponentFirmwareUpdateDriver | The folder that contains the source files for the CFU driver sample. |
| ComponentizedPackageExample | An example deployment package that includes the INF and payload files for the componentized packages approach. |
| MonolithicPackageExample | An example deployment package that includes INF and the payload files for the monolithic package approach. |
| DMF| Contains the DMF source code. Use `git submodule update` to pull the DMF contents. |
| ComponentFirmwareUpdateDriver/Common.h | All includes for this driver |
| ComponentFirmwareUpdateDriver/Device.h | Definition of device context for this driver |
| ComponentFirmwareUpdateDriver/DmfInterface.c | Instantiate Dmf Library Modules used by this driver |
| ComponentFirmwareUpdateDriver/Firmware.c | Firmware files (offer/payload) related functions |
| ComponentFirmwareUpdateDriver/Firmware.h | Companion file to Firmware.c |
| ComponentFirmwareUpdateDriver/Registry.c | Contains the registry related utilities |
| ComponentFirmwareUpdateDriver/Registry.h | Companion file to Registry.c |
| ComponentFirmwareUpdateDriver/Trace.h | Debug tracing related definitions and macros |

## Build the sample

First, install Visual Studio and Windows Driver Kit (WDK) as outlined at [Download the Windows Driver Kit (WDK)](https://docs.microsoft.com/windows-hardware/drivers/download-the-wdk).

Then, run the following git commands to get the Driver Module Framework (DMF) submodule required to build the samples.

`git submodule init`

`git submodule update`

You can change the default configuration to build for your version of the operating system. To select a configuration and build a driver:

1. Choose your deployment approach.
  
   For componentized, open the project using these solutions:

    - ComponentizedPackageExample\DockFWUpdate\DockFirmwareUpdateWithExtension.sln

    - ComponentizedPackageExample\LaptopMCUFWUpdate\LaptopMCUFirmwareUpdateWithExtension.sln

   For monolithic, open the project using these solutions:

    - MonolithicPackageExample\DockFWUpdate\DockFirmwareUpdate.sln

    - MonolithicPackageExample\LaptopMCUFWUpdate\LaptopMCUFirmwareUpdate.sln

1. From **Configuration Manager**, select **Active Solution Configuration** (for example, **Debug**) and the Active Solution Platform (for example, **x86**) that correspond to the type of build you are interested in.

1. Each driver project in this iterative sample creates a binary ComponentFirmwareUpdateDriver.dll.

1. From the Build menu, click **Build** Solution (Ctrl+Shift+B).

## See also

[Customizing the Component Firmware Update Driver](https://github.com/Microsoft/CFU/blob/master/Documentation/CFU-Driver/cfu-driver.md)
