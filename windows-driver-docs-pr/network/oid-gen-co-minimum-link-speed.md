---
title: OID_GEN_CO_MINIMUM_LINK_SPEED
description: This topic describes the OID_GEN_CO_MINIMUM_LINK_SPEED object identifier (OID).
ms.assetid: 2ed27ec7-b773-4751-96d3-42d839f35a97
keywords:
- OID_GEN_CO_MINIMUM_LINK_SPEED
ms.date: 11/02/2017
ms.localizationpriority: medium
---

# OID_GEN_CO_MINIMUM_LINK_SPEED

The OID_GEN_CO_MINIMUM_LINK_SPEED OID requests the miniport driver to return its minimum transmit and receive speeds formatted as an NDIS_CO_LINK_SPEED structure, which is defined as follows:

```c++
typedef struct _NDIS_CO_LINK_SPEED{
    ULONG   Outbound;
    ULONG   Inbound;
} NDIS_CO_LINK_SPEED, *PNDIS_CO_LINK_SPEED;
```

The members of this structure contain the following information:

**Outbound**  
The minimum transmit speed of the NIC. The unit of measurement is 100bps, so a value of 100,000 represents a hardware bit rate of 10 Mbps.

**Inbound**  
The minimum receive speed of the NIC. The unit of measurement is 100bps, so a value of 100,000 represents a hardware bit rate of 10 Mbps.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

