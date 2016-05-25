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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20PCMCIA%20IRQ%20Routing%20on%20Windows%20XP%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




