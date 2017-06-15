---
title: Windows Kernel-Mode DMA Library
author: windows-driver-content
description: Windows Kernel-Mode DMA Library
MS-HAID:
- 'dmalib\_6b1c8717-1554-46e9-9156-1afbee9380b2.xml'
- 'kernel.windows\_kernel\_mode\_dma\_library'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: db6cc33a-474b-44a2-bd55-769ff31abae7
---

# Windows Kernel-Mode DMA Library


To enhance performance, a device may need direct access to memory in a way that bypasses the central processing unit (CPU). This technology is called direct memory access (DMA). Windows provides a DMA library for device driver developers.

For more information about DMA for drivers, see [DMA](https://msdn.microsoft.com/library/windows/hardware/ff544058).

For a listing of DMA routines, see [Direct Memory Access (DMA) Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff544068).

Note that DMA is a technology for communicating directly between device and memory and is not the same as [Device Memory Access](https://msdn.microsoft.com/library/windows/hardware/ff543138), which is a set of macros provided to read and write to I/O ports and CPU registers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20Kernel-Mode%20DMA%20Library%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


