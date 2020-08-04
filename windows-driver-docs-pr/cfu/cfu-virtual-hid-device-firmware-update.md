---
title: CFU virtual HID device firmware update
description: Provides a walkthrough of updating firmware for the Component Firmware Update (CFU) virtual HID device sample.
ms.date: 07/28/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# CFU virtual HID device firmware update

This topic provides a walkthrough of updating firmware for the Component Firmware Update (CFU) virtual HID device sample.

## Prerequisites

1. Install Visual Studio 2019 and the Windows Driver Kit (WDK)

## Build and install Install a virtual CFU virtual HID device

1. Clone the Microsoft CFU repository located on GitHub

`git clone https://github.com/microsoft/CFU.git`

1. In your local CFU repository directory, at a command prompt, install the CFU git submodules:

`git submodule init`

`git submodule update`

1. Build the CfuVirtualHid device solution in Visual Studio

`C:\repo\CFU\Host\CFUFirmwareSimulation\CfuVirtualHid.sln'

1. Install the CfuVirtualHid device and driver

    1. At an administrative command prompt, TBD

    `devcon.exe install cfuvirtualhid.inf HID\CFU_VIRTUAL_DEVICE`

1. TBD

1. From Control Panel, open Device Manager, expand the Firmware node, and select the TBD

1. TBD

1. TBD

## Install a firmware update for thr CFU virtual HID device

TBD

![step 1](images/install-cfu-virtual-device-firmware-update-1.png)

TBD

![step 2](images/install-cfu-virtual-device-firmware-update-2.png)

TBD

![step 3](images/install-cfu-virtual-device-firmware-update-3.png)

TBD

![step 4](images/install-cfu-virtual-device-firmware-update-4.png)

## See also

TBD
