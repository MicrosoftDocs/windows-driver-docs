---
title: OID_GEN_CO_GET_NETCARD_TIME
description: This topic describes the OID_GEN_CO_GET_NETCARD_TIME object identifier (OID).
ms.assetid: 4dfa0f02-2b37-4b9f-95fe-dd33774dedbc
keywords:
- OID_GEN_CO_GET_NETCARD_TIME
ms.date: 11/02/2017
ms.localizationpriority: medium
---

# OID_GEN_CO_GET_NETCARD_TIME

> [!NOTE]
> OID_GEN_CO_GET_NETCARD_TIME is the same as OID_GEN_GET_NETCARD_TIME.

The OID_GEN_CO_GET_NETCARD_TIME OID requests the miniport driver to return a NIC's local time, as derived from a clock on the NIC or from the network. The time is formatted as a GEN_GET_NETCARD_TIME structure, defined as follows:

```c++
typedef struct _GEN_GET_NETCARD_TIME{
    ULONGLONG   ReadTime;
} GEN_GET_NETCARD_TIME, *PGEN_GET_NETCARD_TIME;
```

The member of this structure contains the following information:

**ReadTime**  
    The NIC's local time.

## Remarks

The miniport driver specified the units for its local time in the **ClockPrecision** element of the GEN_GET_TIME_CAPS structure that the miniport driver returned in response to a previous OID_GEN_CO_GET_TIME_CAPS query.

If the miniport driver set the READABLE_LOCAL_CLOCK flag in its response to an OID_GEN_CO_GET_TIME_CAPS query, the NIC derives its local time from an onboard clock. If the miniport driver set the CLOCK_NETWORK_DERIVED flag in its response to an OID_GEN_CO_GET_TIME_CAPS query, the NIC derives its local time from the network.

If the local time is derived from an onboard clock, the miniport driver should be able to report the clock precision in parts per million. In general, a network-derived clock is preferable, because it is likely to be more precise and can be used to synchronize many machines attached to the same network or switch.

The miniport driver must return its local time synchronously in its response to the OID_GEN_CO_GET_NETCARD_TIME query since this query synchronizes protocol drivers with the NIC's local time. Protocol drivers should send the OID_GEN_CO_GET_NETCARD_TIME query several times in succession to filter out response-time latencies.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

