---
title: OID_GEN_CO_MEDIA_CONNECT_STATUS
description: This topic describes the OID_GEN_CO_MEDIA_CONNECT_STATUS object identifier (OID).
ms.assetid: d49ebdfb-1c41-40dc-86bf-01db50a73607
keywords:
- OID_GEN_CO_MEDIA_CONNECT_STATUS
ms.date: 11/02/2017
ms.localizationpriority: medium
---

# OID_GEN_CO_MEDIA_CONNECT_STATUS

The OID_GEN_CO_MEDIA_CONNECT_STATUS OID requests the miniport driver to return the connection status of the NIC on the network as one of the following system-defined values:

**NdisMediaStateConnected**

**NdisMediaStateDisconnected**

When a miniport driver senses that the network connection has been lost, it should call [NdisMCoIndicateStatus](https://msdn.microsoft.com/library/windows/hardware/ff563562) with NDIS_STATUS_MEDIA_DISCONNECT. When the connection is restored, it should call NdisMCoIndicateStatus with NDIS_STATUS_MEDIA_CONNECT.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

