---
title: Source and Destination Page Break
description: Source and Destination Page Break
ms.assetid: 11e3c064-96e8-40b8-8824-e32a5ce637e4
keywords:
- memory-to-memory data transfers WDK NetDMA , page breaks
- data transfers WDK NetDMA , page breaks
- transferring data WDK NetDMA , page breaks
- DMA transfers WDK NetDMA , page breaks
- NetDMA WDK networking , page breaks
- source page breaks WDK NetDMA
- destination page breaks WDK NetDMA
- page breaks WDK NetDMA
- NetDMA 2.0 WDK networking , page breaks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Source and Destination Page Break


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface before version 2.0 supports one physical address per descriptor for the source or destination of the DMA transfer. Because there is one address in each descriptor in NetDMA 1.0, even when the total length of DMA transfer is less than a 4 KB page or the total length that the DMA engine supports (typically 4 KB), if the source or destination spans multiple non-contiguous pages, the NetDMA interface must break the DMA transfer into multiple descriptors.

NetDMA 2.0 provides two physical addresses per descriptor for either the source or destination or both. In NetDMA 2.0, the **NextSourceAddress** and **NextDestinationAddress** members in the [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure specify the physical addresses of the second page of the source or destination address, or both respectively.

The NetDMA interface sets the NET\_DMA\_SOURCE\_PAGE\_BREAK bit in the **ControlFlags** member of NET\_DMA\_DESCRIPTOR when the DMA's transfer source physical address spans a non-contiguous 4 KB page break. When the NET\_DMA\_SOURCE\_PAGE\_BREAK bit is set, a NetDMA version 2.0 or later provider starts the copy from the source physical address that is specified in the **SourceAddress** member. And when the copy operation reaches the end of the first page, it continues the copy from the physical address that is specified in the **NextSourceAddress** member.

The NetDMA interface sets the NET\_DMA\_DESTINATION\_PAGE\_BREAK bit in the **ControlFlags** member when the DMA's transfer destination physical address spans a non-contiguous 4 KB page break. When the NET\_DMA\_DESTINATION\_PAGE\_BREAK bit is set, a NetDMA version 2.0 or later provider starts the copy to the destination physical address that is specified in the **DestinationAddress** member. And when the copy operation reaches the end of the first page, it continues the copy to the physical address that is specified in the **NextDestinationAddress** member.

The second part of the source or destination must start on a page boundary. Therefore, the least significant 12 bits of the addresses that are specified in the **NextSourceAddress** and **NextDestinationAddress** members must be zero.

Note that the source and destination page breaks are specified separately. And, if both exist, they might break at different points.

 

 





