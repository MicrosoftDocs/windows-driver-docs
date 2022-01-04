---
title: Enabling and Disabling Shared GPIO Interrupts
description: In some cases, interrupt request lines from two or more peripheral devices might connect to the same physical general-purpose I/O (GPIO) pin. The GPIO pin for a shared interrupt line is typically configured for level-triggered interrupts.
ms.date: 04/20/2017
---

# Enabling and Disabling Shared GPIO Interrupts


In some cases, interrupt request lines from two or more peripheral devices might connect to the same physical general-purpose I/O (GPIO) pin. The GPIO pin for a shared interrupt line is typically configured for level-triggered interrupts.

If the drivers for these devices register their interrupt service routines (ISRs) to be triggered when an interrupt is asserted on this GPIO pin, GPIO framework extension (GpioClx) calls the [*CLIENT\_EnableInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_enable_interrupt) callback function only when the first driver registers for this interrupt. When other drivers register to use a GPIO interrupt that is already enabled, GpioClx internally tracks these registrations, but does not redundantly call the *CLIENT\_EnableInterrupt* callback function to enable this interrupt. Similarly, GpioClx calls the [*CLIENT\_DisableInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_disable_interrupt) callback function only when the last of these registered drivers releases the interrupt.

 

