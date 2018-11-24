---
title: Supporting header-data split in protocol and filter drivers
description: Supporting Header-Data Split in Protocol Drivers and Filter Drivers
ms.assetid: ba1566f2-7da6-4472-b00b-e25bf7acc294
keywords:
- header-data split WDK , protocol drivers
- header-data split WDK , filter drivers
- protocol drivers WDK networking , header-data split
- filter drivers WDK networking , header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Header-Data Split in Protocol Drivers and Filter Drivers





NDIS 6.0 and later protocol drivers and filter drivers must support receive indications with the header and data in non-contiguous buffers.

You must not assume that there is only a single MDL in a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure. Protocol drivers and filter drivers are not required to do anything specific to support header-data split registration. But, the driver receive handling code must handle more than one MDL in the MDL chain and must use the following NDIS MDL macros to access the MDL chain:

-   [**NET\_BUFFER\_FIRST\_MDL**](https://msdn.microsoft.com/library/windows/hardware/ff568386)

-   [**NET\_BUFFER\_CURRENT\_MDL**](https://msdn.microsoft.com/library/windows/hardware/ff568379)

-   [**NET\_BUFFER\_CURRENT\_MDL\_OFFSET**](https://msdn.microsoft.com/library/windows/hardware/ff568380)

With split buffers, the data length that is associated with the NET\_BUFFER structure (in the **DataLength** member of the [**NET\_BUFFER\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568381) structure) is split across multiple MDLs. For example, if a protocol driver tried to access the entire data buffer in the first MDL, the driver could access invalid data.

**Note**  After the receive indication call returns to a miniport driver, the miniport driver can reclaim the header MDLs. The overlying drivers or their clients must not access the header MDLs after the receive indication call returns to the miniport driver. This restriction also applies even when the miniport driver is not indicating the received data with a status of NDIS\_RECEIVE\_FLAGS\_RESOURCES.

 

 

 





