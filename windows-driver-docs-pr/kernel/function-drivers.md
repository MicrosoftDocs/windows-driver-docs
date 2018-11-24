---
title: Function Drivers
description: Function Drivers
ms.assetid: a6ac329b-ffb0-4bd3-9d54-195fa025d532
keywords: ["function drivers WDK WDM", "raw mode WDK WDM", "WDM function drivers WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Function Drivers





A *function driver* is the main driver for a device (see the [Possible Driver Layers](types-of-wdm-drivers.md#possible-driver-layers) figure). A function driver is typically written by the device vendor and is required (unless the device is being used in [*raw mode*](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raw-mode)). The PnP manager loads at most one function driver for a device. A function driver can service one or more devices.

A function driver provides the operational interface for its device. Typically the function driver handles reads and writes to the device and manages device power policy.

The function driver for a device can be implemented as a driver/minidriver pair, such as a port/miniport driver pair or a class/miniclass driver pair. In such driver pairs, the minidriver is linked to the second driver, which is a DLL.

If a device is being driven in raw mode, it has no function driver and no upper or lower-level filter drivers. All raw-mode I/O is done by the bus driver and optional bus filter drivers.

 

 




