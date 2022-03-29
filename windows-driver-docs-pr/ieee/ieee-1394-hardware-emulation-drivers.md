---
title: IEEE 1394 Hardware Emulation Drivers
description: IEEE 1394 Hardware Emulation Drivers
keywords:
- IEEE 1394 WDK buses , emulation drivers
- 1394 WDK buses , emulation drivers
- emulation drivers WDK IEEE 1394 bus
- hardware emulation drivers WDK IEEE 1394 bus
- PDOs WDK IEEE 1394 bus
- virtual PDOs WDK IEEE 1394 bus
ms.date: 04/20/2017
---

# IEEE 1394 Hardware Emulation Drivers





An emulation driver can emulate actual IEEE hardware by adding a unit directory to the system's Configuration ROM. The emulation driver then intercepts requests coming from external nodes and emulates the 1394 registers that are exposed by an actual hardware device.

Microsoft provides a virtual device mechanism that vendors can use to implement emulation drivers.

For information about how to create a virtual device, see [Creating IEEE 1394 Virtual Devices](./how-drivers-manage-ieee-1934-virtual-devices.md).

For information about how to remove a virtual device, see [Removing IEEE 1394 Virtual Devices](./how-drivers-manage-ieee-1934-virtual-devices.md).

With just a few exceptions, the emulation driver can use the complete 1394 DDI in the same way that a function driver for a real device would. For an explanation of differences in the way real and virtual devices use the 1394 DDI, see [Supporting Requests in IEEE 1394 Virtual Device Drivers](./supporting-requests-in-ieee-1394-virtual-device-drivers.md).