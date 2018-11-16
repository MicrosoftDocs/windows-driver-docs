---
title: Performing DMA in 64-Bit Windows
description: Performing DMA in 64-Bit Windows
ms.assetid: 3ef00c05-356d-488a-8422-503d8132344d
keywords: ["64-bit WDK kernel , porting drivers to", "porting drivers to 64-bit Windows", "DMA transfers WDK kernel , 64-bit Windows", "double-buffering WDK 64-bit", "Direct Memory Access WDK kernel", "polymorphism WDK 64-bit", "data structures WDK 64-bit", "unsigned operations WDK 64-bit", "signed operations WDK 64-bit", "pointer arithmetic WDK 64-bit"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Performing DMA in 64-Bit Windows





Adding 64-bit addressing support to your driver can significantly improve overall system performance. This is particularly important for device drivers that perform direct memory access (DMA). In 64-bit Microsoft Windows, device drivers that perform DMA but do not support 64-bit addressing are double-buffered, which results in lower relative performance.

Although double-buffering usually has a relatively small impact (single percentage points) on 8 GB systems, this is enough to impact I/O-intensive tasks, such as database activity. As the amount of physical memory increases, this negative performance impact increases as well.

To support 64-bit DMA, drivers should observe the following guidelines:

1.  Use **PHYSICAL\_ADDRESS** structures for physical address calculations.

2.  Treat the entire 64-bit address as a valid physical address. For example, drivers should not call [**MmGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554547) on a locked buffer, discard the high 32 bits, and pass the truncated address to a 32-bit component adapter. This results in corrupted memory, lost I/O, and system failure.

3.  Use the high-performance scatter/gather routines ([**GetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff546531) and [**PutScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff559967)) that were added in Windows 2000.

4.  Check the value of the [**Mm64BitPhysicalAddress**](mm64bitphysicaladdress.md) global system variable. If it is **TRUE**, the system supports 64-bit physical addressing.

5.  Set the **Dma64BitAddresses** member of the [**DEVICE\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff543107) structure to **TRUE** to indicate that your driver supports 64-bit DMA addresses.

The DMA routines in 32-bit Windows are 64-bit-ready. If your device driver uses these routines correctly, your DMA code should work without modification on 64-bit Windows.

 

 




