---
title: Enabling and Disabling Shared GPIO Interrupts
author: windows-driver-content
description: In some cases, interrupt request lines from two or more peripheral devices might connect to the same physical general-purpose I/O (GPIO) pin. The GPIO pin for a shared interrupt line is typically configured for level-triggered interrupts.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: F3C8F2B1-54BC-46A1-8AC2-50006E1156FF
---

# Enabling and Disabling Shared GPIO Interrupts


In some cases, interrupt request lines from two or more peripheral devices might connect to the same physical general-purpose I/O (GPIO) pin. The GPIO pin for a shared interrupt line is typically configured for level-triggered interrupts.

If the drivers for these devices register their interrupt service routines (ISRs) to be triggered when an interrupt is asserted on this GPIO pin, GPIO framework extension (GpioClx) calls the [*CLIENT\_EnableInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439377) callback function only when the first driver registers for this interrupt. When other drivers register to use a GPIO interrupt that is already enabled, GpioClx internally tracks these registrations, but does not redundantly call the *CLIENT\_EnableInterrupt* callback function to enable this interrupt. Similarly, GpioClx calls the [*CLIENT\_DisableInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439371) callback function only when the last of these registered drivers releases the interrupt.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bgpio\parports%5D:%20Enabling%20and%20Disabling%20Shared%20GPIO%20Interrupts%20%20RELEASE:%20%286/3/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


