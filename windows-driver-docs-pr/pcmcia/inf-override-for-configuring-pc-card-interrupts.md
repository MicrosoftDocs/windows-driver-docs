---
title: INF Override for Configuring PC Card Interrupts
description: INF Override for Configuring PC Card Interrupts
ms.assetid: 90c951c4-0106-426a-b650-aeb93b893206
keywords:
- IRQ routing WDK PCMCIA bus
- PCMCIA WDK buses , IRQ routing
- PC Cards WDK PCMCIA bus
- interrupts WDK PCMCIA bus
- PCI interrupts WDK PCMCIA bus
- ISA interrupts WDK PCMCIA bus
- INF files WDK PCMCIA bus
- PcmciaExclusiveIrq
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF Override for Configuring PC Card Interrupts





If the operating system routes an interrupt from a 16-bit PC Card that does not support sharable PCI interrupts, then the system might stop working. To prevent this from happening, you should indicate that the card does not support sharable interrupts by placing a PcmciaExclusiveIrq directive in the card's INF file.

For example, assume you have a modem whose driver contains an interrupt service routine (ISR) that was not designed to support interrupt sharing. You can direct the operating system to assign a fixed ISA interrupt to the modem by adding the following line to an AddReg section in the modem's INF file:

`HKR,,PcmciaExclusiveIrq,0x00010001,1`

Note, however, that once you put the PcmciaExclusiveIrq directive in a device's INF file, the device will not function with any controller or bridge that does not have access to ISA interrupt.

 

 





