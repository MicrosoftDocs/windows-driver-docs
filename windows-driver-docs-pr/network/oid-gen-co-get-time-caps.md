---
title: OID_GEN_CO_GET_TIME_CAPS
description: This topic describes the OID_GEN_CO_GET_TIME_CAPS object identifier (OID).
ms.assetid: 6381cfc4-b070-4bd4-90de-6de8a4656cbb
keywords:
- OID_GEN_CO_GET_TIME_CAPS
ms.date: 11/02/2017
ms.localizationpriority: medium
---

# OID_GEN_CO_GET_TIME_CAPS

> [!NOTE]
> OID_GEN_CO_GET_TIME_CAPS is the same as OID_GEN_GET_TIME_CAPS.

The OID_GEN_CO_GET_TIME_CAPS OID requests a miniport driver to return its capabilities for reporting a NIC's local time formatted as a GEN_GET_TIME_CAPS structure, which is defined as follows:

```c++
typedef struct _GEN_GET_TIME_CAPS{
    ULONG   Flags;
    ULONG   ClockPrecision;
} GEN_GET_TIME_CAPS, *PGEN_GET_TIME_CAPS;
```

The members of this structure contain the following information:

**Flags**  
The following flags can be ORed together. All unspecified flags must be set to zero. 

READABLE_LOCAL_CLOCK  
When set, indicates the presence of a readable clock on the NIC. Even without such a hardware clock, a miniport driver can use the system clock by calling NdisGetCurrentSystemTime, so long as it reports the correct precision in the ClockPrecision member.

CLOCK_NETWORK_DERIVED  
When set, indicates that the NIC's local time is derived from the network connection, as opposed to a free-running, onboard clock.

CLOCK_PRECISION  
When set, indicates that the ClockPrecision member contains valid information.

RECEIVE_TIME_INDICATION_CAPABLE  
When set, indicates that the NIC hardware can note the local time at which it receives the first cell of a received PDU and that the miniport driver propagates this receive time for each PDU when indicating the packet to a protocol.

TIMED_SEND_CAPABLE  
When set, indicates that the NIC can schedule a packet for transmission according to its local time. Protocols can use NDIS_SET_PACKET_TIME_TO_SEND to set the TimeToSend timestamp in the out-of-band data block of a packet descriptor. Setting the timestamp does not affect when the packet is actually transmitted; instead, the timestamp is used for recordkeeping. A protocol driver can use the timestamp to determine how long it takes to complete the sending of a paket.

TIME_STAMP_CAPABLE  
When set, indicates that the NIC can stamp (in the appropriate field of the outgoing packet) the time at which the first byte of the packet is transmitted and that the NIC can retrieve this time from the same field of an inbound packet.

**ClockPrecision**  
Specifies the clock precision in parts per million. For this information to be considered valid, the CLOCK_PRECISION flag must be set.

## Remarks

A miniport driver can provide support for certain timing parameters even in the absence of a local or network clock. In particular, a miniport driver can use the system clock for receive time indications, timed sends, and even time stamping. A NIC-based clock is better since it is likely to provide higher precision and to be accessible with lower latencies than the system clock. In all cases, the miniport driver must specify the precision of the clock that it uses. This allows protocols to determine how to best use the miniport driver's timing support.

If the miniport driver reports the presence of a readable clock, it must be prepared to immediately respond to an OID_GEN_GET_NETCARD_TIME query. The miniport driver's response to this call is time-critical and therefore must be synchronous.


## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

