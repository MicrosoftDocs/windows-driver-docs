---
title: Primary and Secondary Interrupts
author: windows-driver-content
description: GPIO interrupt handling is inherently a two-stage process.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 731B0E36-4480-4B69-931E-1F7B40B18911
---

# Primary and Secondary Interrupts


GPIO interrupt handling is inherently a two-stage process. The interrupt from the general-purpose I/O (GPIO) controller, which causes the GPIO framework extension (GpioClx) interrupt service routine (ISR) to run, is called the *primary interrupt*. This ISR maps the interrupting GPIO pin to a global system interrupt (GSI), and passes this GSI to the hardware abstraction layer (HAL). The HAL generates a *secondary interrupt* to run a second ISR that is logically connected to the GPIO pin through this GSI. This process is shown in the diagram in [GPIO Driver Support Overview](https://msdn.microsoft.com/library/windows/hardware/hh439512#gpio-block-diagram).

GpioClx implements an ISR to service interrupt requests that the GPIO controller receives through GPIO pins that are configured as interrupt inputs. When a peripheral device asserts an interrupt on a GPIO pin, and the interrupt is enabled and unmasked in the GPIO controller, the GPIO controller hardware asserts an interrupt to the processor. In response to this interrupt, the ISR in GpioClx queries the GPIO controller to identify the GPIO pin that generated the interrupt, and then determines which GSI is assigned to this pin. The GpioClx ISR passes this GSI to the HAL, and the HAL calls the ISR that is logically connected to the GSI.

Typically, this second ISR belongs to the driver for the peripheral device that asserted the interrupt on the GPIO pin. For information about how a peripheral device driver logically connects its ISR to a GPIO interrupt pin, see [GPIO-Based Interrupt Resources](https://msdn.microsoft.com/library/windows/hardware/hh698246).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bgpio\parports%5D:%20Primary%20and%20Secondary%20Interrupts%20%20RELEASE:%20%286/3/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


