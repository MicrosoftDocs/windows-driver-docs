---
title: OID_GEN_CO_NETCARD_LOAD
ms.topic: reference
description: This topic describes the OID_GEN_CO_NETCARD_LOAD object identifier (OID).
keywords:
- OID_GEN_CO_NETCARD_LOAD
ms.date: 11/02/2017
---

# OID_GEN_CO_NETCARD_LOAD

> [!NOTE]
> OID_GEN_CO_NETCARD_LOAD is the same as OID_GEN_NETCARD_LOAD.

The OID_GEN_CO_NETCARD_LOAD OID returns the relative load on the transmit system of a connection-oriented miniport driver. The miniport driver derives this number by calculating the difference between the amount of data delivered for transmission from protocols and the amount of data actually sent, as indicated by the packets returned to protocols with [NdisMCoSendComplete](/previous-versions/windows/hardware/network/ff553475(v=vs.85)). The result is the amount of outstanding transmit data in the miniport driver at any time.

Because this statistic changes at a very high frequency, the miniport driver port should filter it. The simplest filtering method is to maintain a running average of samples of the outstanding transmit data. For example, each time [MiniportCoSendPackets](/previous-versions/windows/hardware/network/ff549426(v=vs.85)) is called, the miniport driver could add the submitted packet size to a miniport driver-defined variable called *OutstandingBytes*. Each time the miniport driver calls [NdisMCoSendComplete](/previous-versions/windows/hardware/network/ff553475(v=vs.85)), the miniport driver would then subtract the returned packet size from *OutstandingBytes*. The miniport driver must also maintain a running average, which is the value that the miniport driver should return in response to the OID_GEN_CO_NETCARD_LOAD query. This variable, which could be called *RunningAverage*, must be updated on each *MiniportCoSendPackets*, as follows:

```c++
RunningAverage = [(RunningAverage * C) + (OutstandingBytes * (128 - C))] / 128;
```
In this case, 1 \< *C* \< 128. Larger values of *C* produce smoother filtering.

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)
