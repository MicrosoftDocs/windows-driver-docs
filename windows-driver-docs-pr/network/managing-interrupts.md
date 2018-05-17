---
title: Managing Interrupts
description: Managing Interrupts
ms.assetid: 9a2dea43-844d-4c87-9c20-610972d7a3a4
keywords:
- miniport drivers WDK networking , interrupts
- NDIS miniport drivers WDK , interrupts
- interrupts WDK networking , managing
- NICs WDK networking , interrupts
- network interface cards WDK networking , interrupts
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Managing Interrupts


## <a href="" id="ddk-managing-interrupts-ng"></a>


Miniport drivers that manage interrupts for a network interface card (NIC) must register the interrupt and *MiniportXxx* functions for the interrupt.

The following topics provide information about managing interrupt resources and handling interrupts:

[Registering and Deregistering Interrupts](registering-and-deregistering-interrupts.md)

[Handling Interrupts](handling-interrupts.md)

[Synchronizing with Interrupts](synchronizing-with-interrupts.md)

[Interrupt Moderation](interrupt-moderation.md)

 

 





