---
title: Requirements for Routing PC Card Interrupts
description: Requirements for Routing PC Card Interrupts
ms.assetid: dbe01864-f05b-4004-9b04-bdefc5055e78
keywords:
- IRQ routing WDK PCMCIA bus
- PCMCIA WDK buses , IRQ routing
- PC Cards WDK PCMCIA bus
- interrupts WDK PCMCIA bus
- PCI interrupts WDK PCMCIA bus
- ISA interrupts WDK PCMCIA bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requirements for Routing PC Card Interrupts





In order to use PCI interrupts instead of ISA interrupts, 16-bit PC Cards must meet the following two basic requirements.

-   Support for PCI level-triggered interrupt generation. Most 16-bit PC Cards comply with this requirement, because the PCMCIA standard specifies that PC Cards and CardBus cards must support level-triggered interrupts.

-   Support for interrupt sharing. Many 16-bit PC Cards do not comply with this requirement. PCI interrupts are sharable, so the system cannot assign a PCI interrupt number to a 16-bit PC Card if the card does not support sharable interrupts. Common reasons why a 16-bit PC Card cannot share interrupts include:
    -   **Failure of the interrupt service routine (ISR) to return the number of the interrupt.** On a PCI bus, an ISR must indicate which interrupt it is servicing by returning the number of the interrupt after it completes. ISRs for some 16-bit PC Cards do not do this.
    -   **Failure of the PC Card to indicate the interrupts it asserts in its hardware registers.** A PC Card must indicate the number of the interrupt it is asserting in its hardware registers to avoid contention for the same interrupt number with other devices. Some 16-bit PC Cards do not do this.
    -   **Generation of spurious interrupts when powering up.** PC Cards must not generate any interrupts other than those that are assigned to them by the system. Some 16-bit PC Cards generate spurious interrupts when powering up, before the system has assigned them interrupts.

A PC Card that does not fulfill these requirements can cause an interrupt storm that provokes a system crash.

 

 





