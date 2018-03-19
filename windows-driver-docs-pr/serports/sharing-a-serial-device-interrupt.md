---
title: Sharing a Serial Device Interrupt
author: windows-driver-content
description: Sharing a Serial Device Interrupt
ms.assetid: 1d35fbc0-7031-42f3-bb22-52d2bcdcfa92
keywords:
- COM ports WDK serial devices
- serial devices WDK , COM ports
- legacy COM ports WDK serial devices
- sharing serial device interrupts
- serial devices WDK , interrupts
- interrupts WDK serial devices
- shared interrupts WDK serial devices
- Serial driver WDK , interrupts
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sharing a Serial Device Interrupt


## <a href="" id="ddk-sharing-a-serial-device-interrupt-kg"></a>


Legacy COM ports on the same multiport board share a single interrupt. COM ports on a multiport board are identified by an index or a mask that associates a port with its corresponding device object.

Stand-alone serial devices can also share interrupts. However, a shared interrupt can only be used by one device at a time. When a device is opened, Serial allocates the interrupt to the device. When a device is closed, the driver releases the interrupt for use by another device.

 

 




