---
title: IEEE 1394 Hardware Emulation Drivers
description: IEEE 1394 Hardware Emulation Drivers
ms.assetid: 44141072-e425-4983-9234-3ad79daa2017
keywords:
- IEEE 1394 WDK buses , emulation drivers
- 1394 WDK buses , emulation drivers
- emulation drivers WDK IEEE 1394 bus
- hardware emulation drivers WDK IEEE 1394 bus
- PDOs WDK IEEE 1394 bus
- virtual PDOs WDK IEEE 1394 bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IEEE 1394 Hardware Emulation Drivers





An emulation driver can emulate actual IEEE hardware by adding a unit directory to the system's Configuration ROM. The emulation driver then intercepts requests coming from external nodes and emulates the 1394 registers that are exposed by an actual hardware device.

Microsoft provides a virtual device mechanism that vendors can use to implement emulation drivers.

For information about how to create a virtual device, see [Creating IEEE 1394 Virtual Devices](https://msdn.microsoft.com/library/windows/hardware/ff537065).

For information about how to remove a virtual device, see [Removing IEEE 1394 Virtual Devices](https://msdn.microsoft.com/library/windows/hardware/ff537630).

With just a few exceptions, the emulation driver can use the complete 1394 DDI in the same way that a function driver for a real device would. For an explanation of differences in the way real and virtual devices use the 1394 DDI, see [Supporting Requests in IEEE 1394 Virtual Device Drivers](https://msdn.microsoft.com/library/windows/hardware/ff538825).

 

 




