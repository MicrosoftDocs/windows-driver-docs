---
title: OID_GEN_CO_MEDIA_IN_USE
description: This topic describes the OID_GEN_CO_MEDIA_IN_USE object identifier (OID).
ms.assetid: 59a2c981-87a5-4df9-af26-3c5a5eadc17a
keywords:
- OID_GEN_CO_MEDIA_IN_USE
ms.date: 11/02/2017
ms.localizationpriority: medium
---

# OID_GEN_CO_MEDIA_IN_USE

A complete list of the media types the NIC is currently supporting, defined as some, none (also called the NULL filter), or all of the following:

**NdisMedium802_3**  
Ethernet (802.3).

**NdisMedium802_5**  
Token Ring (802.5).

**NdisMediumFddi**  
FDDI.

**NdisMediumWan**  
WAN.

**NdisMediumLocalTalk**  
LocalTalk.

**NdisMediumDix**  
DIX.

**NdisMediumArcnetRaw**  
ARCNET (raw).

**NdisMediumArcnet878_2**  
ARCNET (878.2).

**NdisMediumWirelessWan**  
Various types of NdisWirelessXxx media.

**NdisMediumAtm**  
ATM.

If the underlying miniport driver returns **NULL** for this query or if an experimental media type is used, the driver must indicate receives with [NdisMCoIndicateReceivePacket](https://msdn.microsoft.com/library/windows/hardware/ff553455).


## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

