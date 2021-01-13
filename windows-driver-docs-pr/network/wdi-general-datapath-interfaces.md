---
title: WDI general datapath interfaces
description: This section describes general WDI datapath interfaces
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI general datapath interfaces


## 802.11 frame handling and frame metadata


802.11 frames are passed between WDI and the TAL in the form of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) (NBL) chains. Each NBL represents one MSDU. Through macros, the NBL structure provides operations on the data buffers and access to metadata, including operating system populated Wi-Fi TX metadata. The structure is extensible through its context and **MiniportReserved** members. **MiniportReserved\[0\]** points to a buffer of type [**WDI\_FRAME\_METADATA**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_frame_metadata). This buffer is allocated by WDI in the TX path, and by the TAL in the RX path via the callback [*NdisWdiAllocateWiFiFrameMetaData*](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_allocate_wdi_frame_metadata). The TAL uses MiniportReserved\[1\] to store any additional frame metadata.

## Datapath management requests and indications


For datapath management request and indication function reference, see [WDI Datapath Management Functions](/windows-hardware/drivers/ddi/_netvista/).

## Related topics


[**NDIS\_WDI\_DATA\_API**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_wdi_data_api)

[**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list)

[*NdisWdiAllocateWiFiFrameMetaData*](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_allocate_wdi_frame_metadata)

[**WDI\_FRAME\_METADATA**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_frame_metadata)

 

