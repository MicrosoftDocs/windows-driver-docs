---
title: Configure Non-PnP Devices to an RS-232 Port
description: Configuration of Non-Plug and Play Serial Device Connected to an RS-232 Port
keywords:
- Plug and Play serial devices WDK
- serial devices WDK , non-Plug and Play
- non-Plug and Play serial devices WDK
- RS-232 ports WDK serial devices
ms.date: 04/20/2017
---

# Configuration of Non-Plug and Play Serial Device Connected to an RS-232 Port

This topic describes the typical configuration of hardware, drivers, and device stacks for legacy serial devices that are connected to an RS-232 port.

The following diagram shows the typical configuration for a non-Plug and Play Toaster device.

:::image type="content" source="images/ser1.png" alt-text="Diagram showing hardware, drivers, and device stacks configurations for a non-Plug and Play Toaster device connected to an RS-232 port.":::

Serenum is not used to install a non-Plug and Play serial device. The installation of the Toaster device stack is device-specific. To communicate with the Toaster device, the Toaster driver opens the [COM port](configuration-of-com-ports.md) that is associated with the RS-232 port.
