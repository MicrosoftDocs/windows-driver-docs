---
title: Component Firmware Update (CPU) host
description: Component Firmware Update (CPU) host TBD
ms.date: 09/10/2019
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# CFU host

This folder contains 
- A sample CFU driver and 
- Examples of adopting the driver to enable firmware update scenarios using the componentized and monolothic packaging techniques.

## CFU Driver Sample

The CFU driver sample sends firmware image file(s) to a device in need of an update. Before sending the firmware image, the driver sends several commands to the device with firmware offers. Only if the device accepts, the driver sends the firmware payload. The communication between the driver and the device is in accordance with the [CFU protocol](https://github.com/Microsoft/CFU/tree/master/Documentation/CFU-Protocol), an open source specification (included with CFU) based on the HID protocol.

The CFU driver sample is implemented using the [User-Mode Driver Framework](https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/overview-of-the-umdf) 2.0 model and based on the the [Microsoft Devices Driver Module Framework (DMF)](https://blogs.windows.com/buildingapps/2018/08/15/introducing-driver-module-framework/).
As a firmware developer, you can customize the driver for the purposes of adopting the CFU model to enable firmware updates for your component(s). For more information, see [Customizing the Component Firmware Update Driver](https://github.com/Microsoft/CFU/blob/master/Documentation/CFU-Driver/cfu-driver.md).

## Packaging Examples

Consider these example devices in need of firmware updates, a laptop and dock device. The laptop has a primary component - the MCU, and two sub-components FPGA and TCPM. The dock device with a primary component - the MCU and another sub-component for audio.

The sample can be deployed using one of two approaches:

- The componentized packages approach

    The base package contains the driver binary and the driver INF that is common for all your devices. The extension package contains the firmware image files and an INF that describes those firmware files for a device. Base package and extensions packages are serviced independently.

    [LaptopExample](https://github.com/Microsoft/CFU/tree/master/Host/ComponentizedPackageExample/LaptopMCUFWUpdate)<br>
    [DockExample](https://github.com/Microsoft/CFU/tree/master/Host/ComponentizedPackageExample/DockFWUpdate)<br>

- The monolithic package approach

    There is a single package for the driver and CFU capable device(s). The package includes: INF, the CFU driver binary, and firmware files for the device(s).

    [LaptopExample](https://github.com/Microsoft/CFU/tree/master/Host/MonolithicPackageExample/LaptopMCUFWUpdate)<br>
    [DockExample](https://github.com/Microsoft/CFU/tree/master/Host/MonolithicPackageExample/DockFWUpdate)<br>

## Build the sample

First, install Visual Studio and Windows Driver Kit (WDK) following the steps [here](https://docs.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk).

Then, run the following git commands to get the Driver Module Framework (DMF) submodule required to build the samples.
#### "git submodule init"
#### "git submodule update"

You can change the default configuration to build for your version of the operating system. To select a configuration and build a driver:

1. Choose your deployment approach.
  
   For componentized, open the project using these solutions:

    - ComponentizedPackageExample\DockFWUpdate\DockFirmwareUpdateWithExtension.sln
    - ComponentizedPackageExample\LaptopMCUFWUpdate\LaptopMCUFirmwareUpdateWithExtension.sln

   For monolithic, open the project using these solutions:
    - MonolithicPackageExample\DockFWUpdate\DockFirmwareUpdate.sln
    - MonolithicPackageExample\LaptopMCUFWUpdate\LaptopMCUFirmwareUpdate.sln

3. From the **Configuration Manager**, select the **Active Solution Configuration** (for example, **Debug**) and the Active Solution Platform (for example, **x86**) that correspond to the type of build you are interested in.
4. Each driver project in this iterative sample creates a binary ComponentFirmwareUpdateDriver.dll. 
5. From the Build menu, click **Build** Solution (Ctrl+Shift+B).

# See Also
[Customizing the Component Firmware Update Driver](https://github.com/Microsoft/CFU/blob/master/Documentation/CFU-Driver/cfu-driver.md)
