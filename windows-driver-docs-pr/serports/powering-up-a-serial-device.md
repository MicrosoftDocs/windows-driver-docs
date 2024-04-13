---
title: Powering Up a Serial Device
description: Powering Up a Serial Device
keywords:
- Serial driver WDK , device power
- powering up serial devices WDK
- turning on serial devices WDK
- serial devices WDK , powering up
ms.date: 04/20/2017
---

# Powering Up a Serial Device

A serial device must be turned on (in the device power state **PowerDeviceD0**) for Serial to communicate with the device hardware. If the device is not turned on, Serial will attempt to turn on the device before the driver completes a request.
