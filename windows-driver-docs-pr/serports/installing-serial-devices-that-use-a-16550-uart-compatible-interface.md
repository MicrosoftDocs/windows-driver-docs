---
title: Install Serial Devices with a 16550 UART-Compatible Interface
description: Installing Serial Devices that Use a 16550 UART-Compatible Interface
ms.assetid: d80db651-b890-44dc-98ad-32e72e244d8c
keywords:
- Serial driver WDK , 16550 UART-compatible interfaces
- universal asynchronous receiver-transmitters WDK serial devices
- UART WDK serial devices
- 16550 UART-compatible interfaces WDK serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Serial Devices that Use a 16550 UART-Compatible Interface





To install a Plug and Play device that uses Serial as a lower-level device filter driver, do the following:

-   Specify Serial as a lower-level device filter driver in the device's INF file -- see [Installing a Filter Driver](https://msdn.microsoft.com/library/windows/hardware/ff547595).

-   Set the **SerialSkipExternalNaming** entry value for the device to a nonzero value -- see [Registry Settings for a Plug and Play Serial Device](registry-settings-for-a-plug-and-play-serial-device.md).

 

 




