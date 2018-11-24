---
title: GPIO Interrupt Masks
description: General-purpose I/O (GPIO) pins that are configured as interrupt inputs can be masked and unmasked in addition to being enabled and disabled.
ms.assetid: FD6537DA-2AAA-4646-896D-D5BC834526B6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPIO Interrupt Masks


General-purpose I/O (GPIO) pins that are configured as interrupt inputs can be masked and unmasked in addition to being enabled and disabled.

If a level-triggered interrupt from a peripheral device is enabled and active, but the kernel trap handler cannot immediately run the device's interrupt service routine (ISR) to clear the interrupt, the handler masks the interrupt at the GPIO pin to prevent the pin from repeatedly causing more interrupts. Later, after the ISR runs and clears the interrupt, the interrupt can be safely unmasked.

Masking an interrupt does not clear or disable the interrupt. If a GPIO interrupt is enabled, active, and masked, unmasking this interrupt causes the GPIO controller device to signal an interrupt request to the processor.

A GPIO interrupt mask bit has no effect while the GPIO interrupt is disabled. The [*CLIENT\_EnableInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439377) callback function sets the mask bit for the interrupt to zero; that is, the interrupt is initially unmasked after it is enabled.

An important distinction between masking and disabling a GPIO interrupt pin is that masking preserves the pin's interrupt-configuration settings, whereas disabling the pin does not. While a GPIO interrupt pin is masked, it retains its previously programmed interrupt mode (edge-triggered or level-triggered), polarity (active-high, active-low, or active-both), and debounce settings. These settings take effect again as soon as the interrupt is unmasked. However, when an interrupt is disabled, all of the pin's interrupt-configuration settings are lost. After the pin is enabled, it must be programmed again with the required interrupt-configuration settings.

Some GPIO controllers implement, in hardware, interrupt-mask registers that are separate and distinct from interrupt-enable registers.

However, other GPIO controllers provide a single set of hardware registers that combine the interrupt-mask and interrupt-enable functions. The drivers for these controllers emulate separate interrupt-mask and interrupt-enable registers in software. To do so, these drivers track the logical states of the interrupt-enable bits and interrupt-mask bits and manipulate the corresponding bits in the hardware register to accurately reflect the behavior of the combined logical interrupt-enable and interrupt-mask bits for each GPIO interrupt.

 

 




