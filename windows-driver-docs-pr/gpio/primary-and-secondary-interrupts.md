---
title: Primary and Secondary Interrupts
description: GPIO interrupt handling is inherently a two-stage process.
ms.assetid: 731B0E36-4480-4B69-931E-1F7B40B18911
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Primary and Secondary Interrupts


GPIO interrupt handling is inherently a two-stage process. The interrupt from the general-purpose I/O (GPIO) controller, which causes the GPIO framework extension (GpioClx) interrupt service routine (ISR) to run, is called the *primary interrupt*. This ISR maps the interrupting GPIO pin to a global system interrupt (GSI), and passes this GSI to the hardware abstraction layer (HAL). The HAL generates a *secondary interrupt* to run a second ISR that is logically connected to the GPIO pin through this GSI. This process is shown in the diagram in [GPIO Driver Support Overview](https://msdn.microsoft.com/library/windows/hardware/hh439512#gpio-block-diagram).

GpioClx implements an ISR to service interrupt requests that the GPIO controller receives through GPIO pins that are configured as interrupt inputs. When a peripheral device asserts an interrupt on a GPIO pin, and the interrupt is enabled and unmasked in the GPIO controller, the GPIO controller hardware asserts an interrupt to the processor. In response to this interrupt, the ISR in GpioClx queries the GPIO controller to identify the GPIO pin that generated the interrupt, and then determines which GSI is assigned to this pin. The GpioClx ISR passes this GSI to the HAL, and the HAL calls the ISR that is logically connected to the GSI.

Typically, this second ISR belongs to the driver for the peripheral device that asserted the interrupt on the GPIO pin. For information about how a peripheral device driver logically connects its ISR to a GPIO interrupt pin, see [GPIO-Based Interrupt Resources](https://msdn.microsoft.com/library/windows/hardware/hh698246).

 

 




