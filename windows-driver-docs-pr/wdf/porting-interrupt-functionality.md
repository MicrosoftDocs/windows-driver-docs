---
title: Porting Interrupts
description: Porting Interrupts
ms.assetid: E91B971D-044C-45A4-AD76-44AFB1213F8E
---

# Porting Interrupts


The code for supporting and servicing interrupts is similar in WDF and WDM drivers. There is one primary difference:

-   A WDF driver creates the WDFINTERRUPT object and registers its interrupt service routine (ISR) callback by calling [**WdfInterruptCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547345) from its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback.
-   A WDM driver creates a KINTERRUPT structure and connects it during [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) processing.

The [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback in a WDF driver performs the same tasks as the WDM driver’s [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine. The *EvtInterruptIsr* callback calls [**WdfInterruptQueueDpcForIsr**](https://msdn.microsoft.com/library/windows/hardware/ff547371) to queue the [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback for later processing at DISPATCH\_LEVEL. In response, the framework adds a DPC object to the system queue that runs this callback.

For more information about framework interrupt objects, see [Handling Hardware Interrupts](handling-hardware-interrupts.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Porting%20Interrupts%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




