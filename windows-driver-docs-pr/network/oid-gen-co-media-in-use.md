---
title: OID_GEN_CO_MEDIA_IN_USE
ms.topic: reference
description: This topic describes the OID_GEN_CO_MEDIA_IN_USE object identifier (OID).
keywords:
- OID_GEN_CO_MEDIA_IN_USE
ms.date: 11/02/2017
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

If the underlying miniport driver returns **NULL** for this query or if an experimental media type is used, the driver must indicate receives with [NdisMCoIndicateReceivePacket](/previous-versions/windows/hardware/network/ff553455(v=vs.85)).


## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)
