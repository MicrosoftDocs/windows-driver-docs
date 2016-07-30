---
title: Best Practices for the Design of PC Cards and Card Drivers
description: Best Practices for the Design of PC Cards and Card Drivers
MS-HAID:
- 'mcch2\_f331b6fa-9e96-43e5-be44-8ebfb14b3fbb.xml'
- 'PCMCIA.best\_practices\_for\_the\_design\_of\_pc\_cards\_and\_card\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c3f31757-4063-4c68-ae19-1d8af98f81bc
keywords: ["IRQ routing WDK PCMCIA bus", "PCMCIA WDK buses , IRQ routing", "PC Cards WDK PCMCIA bus", "interrupts WDK PCMCIA bus", "PCI interrupts WDK PCMCIA bus", "ISA interrupts WDK PCMCIA bus"]
---

# Best Practices for the Design of PC Cards and Card Drivers


## <a href="" id="ddk-best-practices-for-the-design-of-pc-cards-and-card-drivers-kg"></a>


Vendors and developers should observe the following cautions in order to avoid problems related with interrupt sharing:

-   Driver developers should design drivers to support sharable PCI interrupts.

-   PC Card manufacturers should manufacture CardBus cards instead of 16-bit PC Cards, because they are PCI compliant.

-   All 16-bit PC Cards should support sharable PCI interrupts.

-   All 16-bit PC Cards should support the flexible allocation of I/O resources for devices that connect to them. In particular, cards should not request specific ranges of I/O space. Instead, they should request the amount of I/O space they require and allow the system to allocate the addresses flexibly.

-   Computer manufacturers should be aware that there are devices that require ISA IRQs, and should ensure that ISA IRQs are available to CardBus controllers in the system.

-   Computer manufacturers should ensure that the BIOS code sets CardBus controllers to PCIC mode.

 

 





