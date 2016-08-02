---
title: PCMCIA IRQ Routing on Windows XP
description: PCMCIA IRQ Routing on Windows XP
MS-HAID:
- 'mcch2\_23c4454b-bc1f-4887-9b95-3da6f186f9be.xml'
- 'PCMCIA.pcmcia\_irq\_routing\_on\_windows\_xp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9b3501ce-c536-4ec7-bb01-c449d3900fee
keywords: ["PCIC bridges WDK PCMCIA bus", "PCI-to-PCMCIA bridges WDK PCMCIA bus", "IRQ routing WDK PCMCIA bus", "PCMCIA WDK buses , IRQ routing", "PC Cards WDK PCMCIA bus", "ISA-to-PCI interrupt routing WDK PCMCIA bus", "PCI interrupts WDK PCMCIA bus", "ISA interrupts WDK PCMCIA bus"]
---

# PCMCIA IRQ Routing on Windows XP


## <a href="" id="ddk-pcmcia-irq-routing-on-windowsxp-kg"></a>


There are two classes of PCMCIA cards which are supported by CardBus controllers:

-   32-bit PCI-compliant CardBus

-   16-bit PC Cards, which are basically ISA devices

CardBus cards behave like PCI devices in most respects, including the manner in which they define and manage their interrupts. The system assigns them IRQ numbers taken from the range of numbers that are allocated to devices on the PCI bus.

But the architecture of 16-bit PC Cards is older than the PCI bus, and so many of these cards require ISA interrupt numbers. In order to accommodate these cards in a system where the card has no access to an ISA interrupt request (IRQ) number, CardBus controller architecture makes use of a technique called "ISA-to-PCI interrupt routing." Controllers that support this technique are able to assign a PCI interrupt number to a 16-bit card that was designed to use an ISA interrupt number.

This section discusses ISA-to-PCI interrupt routing and the problems associated with 16-bit cards that do not support ISA-to-PCI interrupt routing.

Prior to the invention of CardBus controllers, most systems used a PCI-to-PCMCIA bridge, known as a "PCIC bridge," in order to connect 16-bit PC Cards to the computer. These bridges do not support CardBus cards, nor do they support ISA-to-PCI interrupt routing. Therefore, the information in this section does not apply to PCIC bridges.

 

 





