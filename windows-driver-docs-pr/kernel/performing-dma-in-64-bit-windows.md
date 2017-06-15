---
title: Performing DMA in 64-Bit Windows
author: windows-driver-content
description: Performing DMA in 64-Bit Windows
MS-HAID:
- 'Other\_6279194e-aa7d-404a-abbc-bec8cbeb9070.xml'
- 'kernel.performing\_dma\_in\_64\_bit\_windows'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3ef00c05-356d-488a-8422-503d8132344d
keywords: ["64-bit WDK kernel , porting drivers to", "porting drivers to 64-bit Windows", "DMA transfers WDK kernel , 64-bit Windows", "double-buffering WDK 64-bit", "Direct Memory Access WDK kernel", "polymorphism WDK 64-bit", "data structures WDK 64-bit", "unsigned operations WDK 64-bit", "signed operations WDK 64-bit", "pointer arithmetic WDK 64-bit"]
---

# Performing DMA in 64-Bit Windows


## <a href="" id="ddk-performing-dma-in-64-bit-windows-kg"></a>


Adding 64-bit addressing support to your driver can significantly improve overall system performance. This is particularly important for device drivers that perform direct memory access (DMA). In 64-bit Microsoft Windows, device drivers that perform DMA but do not support 64-bit addressing are double-buffered, which results in lower relative performance.

Although double-buffering usually has a relatively small impact (single percentage points) on 8 GB systems, this is enough to impact I/O-intensive tasks, such as database activity. As the amount of physical memory increases, this negative performance impact increases as well.

To support 64-bit DMA, drivers should observe the following guidelines:

1.  Use **PHYSICAL\_ADDRESS** structures for physical address calculations.

2.  Treat the entire 64-bit address as a valid physical address. For example, drivers should not call [**MmGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554547) on a locked buffer, discard the high 32 bits, and pass the truncated address to a 32-bit component adapter. This results in corrupted memory, lost I/O, and system failure.

3.  Use the high-performance scatter/gather routines ([**GetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff546531) and [**PutScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff559967)) that were added in Windows 2000.

4.  Check the value of the [**Mm64BitPhysicalAddress**](mm64bitphysicaladdress.md) global system variable. If it is **TRUE**, the system supports 64-bit physical addressing.

5.  Set the **Dma64BitAddresses** member of the [**DEVICE\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff543107) structure to **TRUE** to indicate that your driver supports 64-bit DMA addresses.

The DMA routines in 32-bit Windows are 64-bit-ready. If your device driver uses these routines correctly, your DMA code should work without modification on 64-bit Windows.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Performing%20DMA%20in%2064-Bit%20Windows%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


