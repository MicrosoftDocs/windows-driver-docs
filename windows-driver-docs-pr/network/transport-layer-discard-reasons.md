---
title: Transport layer discard reasons
description: This section describes Transport layer discard reasons for Windows Filtering Platform callout drivers.
ms.assetid: e2a9dcd1-87c6-4052-ae96-3a7994328dd0
keywords:
- Transport layer discard reasons network drivers
ms.date: 11/09/2017
ms.localizationpriority: medium
---

# Transport layer discard reasons

The identifiers for the possible reasons that data is discarded by one of the transport layers are as follows. These identifiers are constant values in the INET_DISCARD_REASON enumeration that is defined in Fwpsk.h.

| Discard reason identifier | Discard reason description |
| --- | --- |
| InetDiscardSourceUnspecified | The outgoing packet's source address is unspecified. |
| InetDiscardDestinationMulticast | The outgoing packet's destination address is an unspecified address, and the transport does not support multicast addresses. |
| InetDiscardHeaderInvalid | The packet's transport protocol header is invalid. |
| InetDiscardChecksumInvalid | The checksum in the packet's transport protocol header is invalid. |
| InetDiscardEndpointNotFound | The endpoint specified in the packet's header could not be found. |
| InetDiscardConnectedPath | The packet remote address does not match the remote address of a connected endpoint. |
| InetDiscardSessionState | The packet cannot be delivered based on network layer information. |
| InetDiscardReceiveInspection | The connection was closed due to a receive inspection failure. |
| InetDiscardAckInvalid | The packet is an invalid ACK segment. |
| InetDiscardExpectedSyn | A SYN segment was expected. |
| InetDiscardRst | The packet is an invalid RST segment. |
| InetDiscardSynRcvdSyn | A TCP connection in SYN_RCVD state received another SYN segment. |
| InetDiscardSimultaneousConnect | A TCP connection has encountered the simultaneous-connect condition. |
| InetDiscardPawsFailed | A TCP PAWS check failed. |
| InetDiscardLandAttack | The packet was detected as part of a Land Attack. |
| InetDiscardMissedReset | An SYN segment outside the receive window was received on a SYN_RCVD connection. An RST may have been missed. |
| InetDiscardOutsideWindow | A TCP segment was outside the receive window. |
| InetDiscardDuplicateSegment | A duplicate TCP segment was received. |
| InetDiscardClosedWindow | The TCP receive window was closed. |
| InetDiscardTcbRemoved | The TCP connection was closed. |
| InetDiscardFinWait2 | The TCP connection is closing. |
| InetDiscardReassemblyConflict | A TCP data reassembly conflict was encountered on reception of a FIN segment. |
| InetDiscardFinReceived | A FIN was already received on a TCP connection; no more data can be received. |
| InetDiscardListenerInvalidFlags | A segment with invalid flags was received by a listening TCP socket. |
| InetDiscardUrgentDeliveryAllocationFailure | There is insufficient memory for URG delivery on a TCP connection. |
| InetDiscardTcbNotInTcbTable | A TCP connection was closed due to urgent delivery. |
| InetDiscardTimeWaitTcbReceivedRstOutsideWindow | A TIME_WAIT state TCP connection received an RSP segment outside the window. |
| InetDiscardTimeWaitTcbSynAndOtherFlags | A TIME_WAIT state TCP connection received a segment with SYN and one or more incompatible flags. |
| InetDiscardTimeWaitTcb | A TIME_WAIT state TCP connection received an invalid segment. |

