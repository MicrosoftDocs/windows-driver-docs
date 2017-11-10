---
title: OID_GEN_CO_GET_NETCARD_TIME
author: windows-driver-content
description: This topic describes the OID_GEN_CO_GET_NETCARD_TIME object identifier (OID).
ms.assetid: 4dfa0f02-2b37-4b9f-95fe-dd33774dedbc
keywords:
- OID_GEN_CO_GET_NETCARD_TIME
ms.author: windowsdriverdev
ms.date: 11/02/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")