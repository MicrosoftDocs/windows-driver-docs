---
title: Porting Interrupts
description: Porting Interrupts
ms.assetid: E91B971D-044C-45A4-AD76-44AFB1213F8E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Interrupts


The code for supporting and servicing interrupts is similar in WDF and WDM drivers. There is one primary difference:

-   A WDF driver creates the WDFINTERRUPT object and registers its interrupt service routine (ISR) callback by calling [**WdfInterruptCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547345) from its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback.
-   A WDM driver creates a KINTERRUPT structure and connects it during [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) processing.

The [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback in a WDF driver performs the same tasks as the WDM driver’s [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine. The *EvtInterruptIsr* callback calls [**WdfInterruptQueueDpcForIsr**](https://msdn.microsoft.com/library/windows/hardware/ff547371) to queue the [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback for later processing at DISPATCH\_LEVEL. In response, the framework adds a DPC object to the system queue that runs this callback.

For more information about framework interrupt objects, see [Handling Hardware Interrupts](handling-hardware-interrupts.md).

 

 





