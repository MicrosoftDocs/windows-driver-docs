---
title: Receive Indications with Header-Data Split
description: Receive Indications with Header-Data Split
keywords:
- header-data split WDK , receive indications
- received data formats WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receive Indications with Header-Data Split





A miniport driver that supports header-data split must indicate received data in the format that header-data split requires. For example, the header buffers should all be in a contiguous block of storage and the data buffers must include backfill space.

The header information in split frames must never include virtual LAN (VLAN) tags. Header-data split requires support for VLAN in hardware and requires removing VLAN tags from the incoming frames and placing them in the **Ieee8021QNetBufferListInfo** OOB information in the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure. The miniport driver must specify support for VLAN in the **MacOptions** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure and in response to the [OID\_GEN\_MAC\_OPTIONS](./oid-gen-mac-options.md) OID query.

NDIS and overlying drivers or user-mode applications use the [OID\_GEN\_HD\_SPLIT\_PARAMETERS](./oid-gen-hd-split-parameters.md) OID to set the current header-data split settings of a miniport adapter. If the NDIS\_HD\_SPLIT\_COMBINE\_ALL\_HEADERS flag in the **HDSplitCombineFlags** member of the [**NDIS\_HD\_SPLIT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_hd_split_parameters) structure is set, the miniport adapter must combine all split frames. If header-data split is enabled in the hardware, the miniport driver must combine the header and data before indicating the frame to NDIS. For more information about OID\_GEN\_HD\_SPLIT\_PARAMETERS and other administrative and configuration issues, see [Header-Data Split Administration and Configuration](setting-the-current-header-data-split-configuration.md).

This section includes:

[Allocating the Header Buffer](allocating-the-header-buffer.md)

[Allocating Backfill for the Data Buffer](allocating-backfill-for-the-data-buffer.md)

[Setting NET\_BUFFER\_LIST Information](setting-net-buffer-list-information.md)

 

