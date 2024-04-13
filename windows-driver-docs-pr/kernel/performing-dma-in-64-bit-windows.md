---
title: Performing DMA in 64-Bit Windows
description: Performing DMA in 64-Bit Windows
keywords: ["64-bit WDK kernel , porting drivers to", "porting drivers to 64-bit Windows", "DMA transfers WDK kernel , 64-bit Windows", "double-buffering WDK 64-bit", "Direct Memory Access WDK kernel", "polymorphism WDK 64-bit", "data structures WDK 64-bit", "unsigned operations WDK 64-bit", "signed operations WDK 64-bit", "pointer arithmetic WDK 64-bit"]
ms.date: 06/16/2017
---

# Performing DMA in 64-Bit Windows





Adding 64-bit addressing support to your driver can significantly improve overall system performance. This is particularly important for device drivers that perform direct memory access (DMA). In 64-bit Microsoft Windows, device drivers that perform DMA but do not support 64-bit addressing are double-buffered, which results in lower relative performance.

Although double-buffering usually has a relatively small impact (single percentage points) on 8 GB systems, this is enough to impact I/O-intensive tasks, such as database activity. As the amount of physical memory increases, this negative performance impact increases as well.

To support 64-bit DMA, drivers should observe the following guidelines:

1.  Use **PHYSICAL\_ADDRESS** structures for physical address calculations.

2.  Treat the entire 64-bit address as a valid physical address. For example, drivers should not call [**MmGetPhysicalAddress**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmgetphysicaladdress) on a locked buffer, discard the high 32 bits, and pass the truncated address to a 32-bit component adapter. This results in corrupted memory, lost I/O, and system failure.

3.  Use the high-performance scatter/gather routines ([**GetScatterGatherList**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pget_scatter_gather_list) and [**PutScatterGatherList**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pput_scatter_gather_list)) that were added in Windows 2000.

4.  Check the value of the [**Mm64BitPhysicalAddress**](mm64bitphysicaladdress.md) global system variable. If it is **TRUE**, the system supports 64-bit physical addressing.

5.  Set the **Dma64BitAddresses** member of the [**DEVICE\_DESCRIPTION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_description) structure to **TRUE** to indicate that your driver supports 64-bit DMA addresses.

The DMA routines in 32-bit Windows are 64-bit-ready. If your device driver uses these routines correctly, your DMA code should work without modification on 64-bit Windows.

 

