---
title: Implementation Issues for GPIO Controller Drivers
description: The GPIO framework extension (GpioClx) provides a flexible device driver interface (DDI).
ms.date: 04/20/2017
---

# Implementation Issues for GPIO Controller Drivers


The GPIO framework extension (GpioClx) provides a flexible device driver interface (DDI). This DDI enables developers to choose among alternative callback interfaces. A driver developer should implement the set of event callback functions that is best suited to the hardware architecture of the target GPIO controller device.

For example, if the GPIO controller driver supports reading from and writing to GPIO I/O pins, the developer can choose to implement one of the following pairs of callback functions:

[*CLIENT\_ReadGpioPins*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_read_pins) and [*CLIENT\_WriteGpioPins*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_write_pins)
[*CLIENT\_ReadGpioPinsUsingMask*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_read_pins_mask) and [*CLIENT\_WriteGpioPinsUsingMask*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_write_pins_mask)
The *CLIENT\_ReadGpioPins* and *CLIENT\_WriteGpioPins* functions receive a bank number, an array of GPIO pin numbers, and a data buffer for the bit values to be read from or written to these pins. If only a small number of GPIO pins is typically accessed in a read or write operation, this pair of callbacks might produce the best implementation. This implementation is typically used for GPIO controllers whose hardware registers are not memory-mapped. However, if several GPIO pins are likely to be accessed during a read or write operation, or if the GPIO controller hardware can efficiently access multiple GPIO pins in parallel, the other pair of callback functions might produce a better implementation.

The *CLIENT\_ReadGpioPinsUsingMask* and *CLIENT\_WriteGpioPinsUsingMask* callback functions can read or write a bank of up to 64 pins in one call. The *CLIENT\_ReadGpioPinsUsingMask* function reads the GPIO pin values into a 64-bit mask. The *CLIENT\_WriteGpioPinsUsingMask* function uses two 64-bit masks. One mask indicates which GPIO pins to set, and the other mask indicates which GPIO pins to clear. This implementation is typically used for memory-mapped GPIO controllers.

 

