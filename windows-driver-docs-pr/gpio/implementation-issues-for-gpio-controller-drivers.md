---
title: Implementation Issues for GPIO Controller Drivers
author: windows-driver-content
description: The GPIO framework extension (GpioClx) provides a flexible device driver interface (DDI).
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 303A6034-7ED7-4C21-86E5-076383AF3A5B
---

# Implementation Issues for GPIO Controller Drivers


The GPIO framework extension (GpioClx) provides a flexible device driver interface (DDI). This DDI enables developers to choose among alternative callback interfaces. A driver developer should implement the set of event callback functions that is best suited to the hardware architecture of the target GPIO controller device.

For example, if the GPIO controller driver supports reading from and writing to GPIO I/O pins, the developer can choose to implement one of the following pairs of callback functions:

[*CLIENT\_ReadGpioPins*](https://msdn.microsoft.com/library/windows/hardware/hh439404) and [*CLIENT\_WriteGpioPins*](https://msdn.microsoft.com/library/windows/hardware/hh439439)
[*CLIENT\_ReadGpioPinsUsingMask*](https://msdn.microsoft.com/library/windows/hardware/hh439406) and [*CLIENT\_WriteGpioPinsUsingMask*](https://msdn.microsoft.com/library/windows/hardware/hh439445)
The *CLIENT\_ReadGpioPins* and *CLIENT\_WriteGpioPins* functions receive a bank number, an array of GPIO pin numbers, and a data buffer for the bit values to be read from or written to these pins. If only a small number of GPIO pins is typically accessed in a read or write operation, this pair of callbacks might produce the best implementation. This implementation is typically used for GPIO controllers whose hardware registers are not memory-mapped. However, if several GPIO pins are likely to be accessed during a read or write operation, or if the GPIO controller hardware can efficiently access multiple GPIO pins in parallel, the other pair of callback functions might produce a better implementation.

The *CLIENT\_ReadGpioPinsUsingMask* and *CLIENT\_WriteGpioPinsUsingMask* callback functions can read or write a bank of up to 64 pins in one call. The *CLIENT\_ReadGpioPinsUsingMask* function reads the GPIO pin values into a 64-bit mask. The *CLIENT\_WriteGpioPinsUsingMask* function uses two 64-bit masks. One mask indicates which GPIO pins to set, and the other mask indicates which GPIO pins to clear. This implementation is typically used for memory-mapped GPIO controllers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bgpio\parports%5D:%20Implementation%20Issues%20for%20GPIO%20Controller%20Drivers%20%20RELEASE:%20%286/3/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


