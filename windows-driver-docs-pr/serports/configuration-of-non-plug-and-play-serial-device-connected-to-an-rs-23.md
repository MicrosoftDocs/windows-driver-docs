---
title: Configure Non-PnP devices to an RS-232 Port
description: Configuration of Non-Plug and Play Serial Device Connected to an RS-232 Port
ms.assetid: 5106e42e-4f87-47c3-a0ec-f70e77daabd3
keywords:
- Plug and Play serial devices WDK
- serial devices WDK , non-Plug and Play
- non-Plug and Play serial devices WDK
- RS-232 ports WDK serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuration of Non-Plug and Play Serial Device Connected to an RS-232 Port





This topic describes the typical configuration of hardware, drivers, and device stacks for legacy serial devices that are connected to an RS-232 port.

The following diagram shows the typical configuration for a non-Plug and Play Toaster device.

![diagram illustrating hardware and drivers-and-device-stacks configurations for a non-plug and play toaster device](images/ser1.png)

Serenum is not used to install a non-Plug and Play serial device. The installation of the Toaster device stack is device-specific. To communicate with the Toaster device, the Toaster driver opens the [COM port](configuration-of-com-ports.md) that is associated with the RS-232 port.

 

 




