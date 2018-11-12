---
title: WDI general datapath interfaces
description: This section describes general WDI datapath interfaces
ms.assetid: 5B40171C-4E5F-4C35-A6E7-1EA5181C02E8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI general datapath interfaces


## 802.11 frame handling and frame metadata


802.11 frames are passed between WDI and the TAL in the form of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) (NBL) chains. Each NBL represents one MSDU. Through macros, the NBL structure provides operations on the data buffers and access to metadata, including operating system populated Wi-Fi TX metadata. The structure is extensible through its context and **MiniportReserved** members. **MiniportReserved\[0\]** points to a buffer of type [**WDI\_FRAME\_METADATA**](https://msdn.microsoft.com/library/windows/hardware/dn897827). This buffer is allocated by WDI in the TX path, and by the TAL in the RX path via the callback [*NdisWdiAllocateWiFiFrameMetaData*](https://msdn.microsoft.com/library/windows/hardware/mt297597). The TAL uses MiniportReserved\[1\] to store any additional frame metadata.

## Datapath management requests and indications


For datapath management request and indication function reference, see [WDI Datapath Management Functions](https://msdn.microsoft.com/library/windows/hardware/mt297634).

## Related topics


[**NDIS\_WDI\_DATA\_API**](https://msdn.microsoft.com/library/windows/hardware/mt297620)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

[*NdisWdiAllocateWiFiFrameMetaData*](https://msdn.microsoft.com/library/windows/hardware/mt297597)

[**WDI\_FRAME\_METADATA**](https://msdn.microsoft.com/library/windows/hardware/dn897827)

 

 






