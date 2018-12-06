---
title: OID_GEN_CO_LINK_SPEED
description: This topic describes the OID_GEN_CO_LINK_SPEED object identifier (OID).
ms.assetid: a88ef1b9-b3f0-403e-8188-85aead46663f
keywords:
- OID_GEN_CO_LINK_SPEED
ms.date: 11/02/2017
ms.localizationpriority: medium
---

# OID_GEN_CO_LINK_SPEED

The OID_GEN_CO_LINK_SPEED OID requests the miniport driver to return its current transmit and receive speeds formatted as an NDIS_CO_LINK_SPEED structure, which is defined as follows:

```c++
typedef struct _NDIS_CO_LINK_SPEED{
    ULONG   Outbound;
    ULONG   Inbound;
} NDIS_CO_LINK_SPEED, *PNDIS_CO_LINK_SPEED;
```

The members of this structure contain the following information:

**Outbound**  
The current transmit speed of the NIC. The unit of measurement is 100bps, so a value of 100,000 represents a hardware bit rate of 10 Mbps.

**Inbound**  
The current receive speed of the NIC. The unit of measurement is 100bps, so a value of 100,000 represents a hardware bit rate of 10 Mbps.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

