---
title: Porting DMA
description: Porting DMA
ms.assetid: 457B6459-EE02-4A2C-8D25-81CE1D9265DC
---

# Porting DMA


\[Applies to KMDF only\]

Performing DMA (Direct Memory Access) in a KMDF driver is simpler than in a WDM driver because the framework handles many of the details on behalf of the driver.

Basically, the framework-based driver creates a DMA enabler object, specifies the DMA capabilities of the device, and supplies a callback function that manipulates the hardware to perform the transfer.

The framework determines the number of map registers that are required for the transfer, allocates the map registers, builds a scatter/gather list (if the device supports scatter/gather DMA), and flushes the processor cache and the buffers whenever necessary.

For implementation details, see [Handling DMA Operations in KMDF Drivers](handling-dma-operations-in-kmdf-drivers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Porting%20DMA%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




