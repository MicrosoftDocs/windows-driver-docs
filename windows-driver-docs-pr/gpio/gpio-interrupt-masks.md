---
title: GPIO Interrupt Masks
author: windows-driver-content
description: General-purpose I/O (GPIO) pins that are configured as interrupt inputs can be masked and unmasked in addition to being enabled and disabled.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: FD6537DA-2AAA-4646-896D-D5BC834526B6
---

# GPIO Interrupt Masks


General-purpose I/O (GPIO) pins that are configured as interrupt inputs can be masked and unmasked in addition to being enabled and disabled.

If a level-triggered interrupt from a peripheral device is enabled and active, but the kernel trap handler cannot immediately run the device's interrupt service routine (ISR) to clear the interrupt, the handler masks the interrupt at the GPIO pin to prevent the pin from repeatedly causing more interrupts. Later, after the ISR runs and clears the interrupt, the interrupt can be safely unmasked.

Masking an interrupt does not clear or disable the interrupt. If a GPIO interrupt is enabled, active, and masked, unmasking this interrupt causes the GPIO controller device to signal an interrupt request to the processor.

A GPIO interrupt mask bit has no effect while the GPIO interrupt is disabled. The [*CLIENT\_EnableInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439377) callback function sets the mask bit for the interrupt to zero; that is, the interrupt is initially unmasked after it is enabled.

An important distinction between masking and disabling a GPIO interrupt pin is that masking preserves the pin's interrupt-configuration settings, whereas disabling the pin does not. While a GPIO interrupt pin is masked, it retains its previously programmed interrupt mode (edge-triggered or level-triggered), polarity (active-high, active-low, or active-both), and debounce settings. These settings take effect again as soon as the interrupt is unmasked. However, when an interrupt is disabled, all of the pin's interrupt-configuration settings are lost. After the pin is enabled, it must be programmed again with the required interrupt-configuration settings.

Some GPIO controllers implement, in hardware, interrupt-mask registers that are separate and distinct from interrupt-enable registers.

However, other GPIO controllers provide a single set of hardware registers that combine the interrupt-mask and interrupt-enable functions. The drivers for these controllers emulate separate interrupt-mask and interrupt-enable registers in software. To do so, these drivers track the logical states of the interrupt-enable bits and interrupt-mask bits and manipulate the corresponding bits in the hardware register to accurately reflect the behavior of the combined logical interrupt-enable and interrupt-mask bits for each GPIO interrupt.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bgpio\parports%5D:%20GPIO%20Interrupt%20Masks%20%20RELEASE:%20%286/3/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


