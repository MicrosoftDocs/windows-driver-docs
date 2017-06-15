---
title: PIO Techniques
author: windows-driver-content
description: PIO Techniques
MS-HAID:
- 'ioprogpio\_ce9436ca-d4ca-4d17-be3e-8d06218c114f.xml'
- 'kernel.pio\_techniques'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bd673e43-c864-416b-b0d0-23c4ba1b870c
---

# PIO Techniques


On some computer hardware architectures, the transfer of data from the CPU (central processing unit) to devices is done by Programmed Input/Output (PIO). Using PIO requires that the CPU wait for the data to be transferred, which can become very inefficient. This technology has been replaced in most instances by Direct Memory Access (DMA) because DMA can assign the transfer of the data to a hardware controller, letting the CPU perform other tasks.

For information on using caches with PIO, see [Flushing Cached Data during PIO Operations](flushing-cached-data-during-pio-operations.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20PIO%20Techniques%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


