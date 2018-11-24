---
title: Modifying the 1394 Configuration ROM
description: Modifying the 1394 Configuration ROM
ms.assetid: 3dc4fe53-a26b-44c7-96ef-e7bb6181c958
keywords:
- IEEE 1394 WDK buses , modifying Configuration ROMs
- 1394 WDK buses , modifying Configuration ROMs
- Configuration ROMs WDK IEEE 1394 bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying the 1394 Configuration ROM





A Microsoft Windows system connected to the 1394 bus exposes a Configuration ROM that describes the functional units supported by the node. For further information about 1394 Configuration ROMs, see the IEEE 1394-1995 and IEEE-1212-2000 specifications. In Windows XP and later operating systems, the contents of the Configuration ROM can be dynamically defined in two ways:

1.  Drivers can dynamically modify the Configuration ROM to expose hardware designed for non-1394 buses on the 1394 bus.

    For example, consider a general purpose system that has an internal DVD drive connected to the system's IDE bus. A driver that maps 1394 requests into the protocol used by the DVD drive could expose the DVD drive on the 1394 bus to other 1394 nodes. To do this, it would have to add a new unit directory to the 1394 Configuration ROM of the system. Other systems connected on the 1394 bus will then be able to enumerate the general purpose system as though it were a 1394 DVD device.

2.  Drivers can use virtual physical device objects (PDOs) to emulate hardware in ways that facilitate the testing of device drivers.

    Device emulation allows developers to test drivers for devices that they have not yet received. Hardware emulation drivers can expose a virtual 1394 device on the 1394 bus. Developers can then debug a driver for the new hardware on another system. For more information about device emulations, see [IEEE 1394 Hardware Emulation Drivers](https://msdn.microsoft.com/library/windows/hardware/ff537214).

## Related topics
[Retrieving the Contents of a IEEE 1394 Node's Configuration ROM](https://msdn.microsoft.com/library/windows/hardware/gg266408)  



