---
title: NetworkDirect Disconnect Scheme
description: This section describes the NetworkDirect disconnect scheme
ms.assetid: A7973588-5AED-494E-92CA-D5EFB2C7950A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NetworkDirect Disconnect Scheme


The scheme described here applies to both [NDSPI](https://msdn.microsoft.com/library/cc904391) version 2 and [NDKPI](network-direct-kernel-programming-interface--ndkpi-.md). The following terms are used:

-   ND is used to refer to NDSPI or NDK.
-   *NdDisconnect* is used to refer to the function call that an ND consumer makes in order to initiate a graceful disconnect. For NDSPI, this is [**INDConnector::Disconnect**](https://msdn.microsoft.com/library/cc904364). For NDKPI, it is *NdkDisconnect* ([*NDK\_FN\_DISCONNECT*](https://msdn.microsoft.com/library/windows/hardware/hh439885)).
-   *NdDisconnectIndication* is used to refer to the indication delivered by an ND provider to an ND consumer when the ND provider receives a graceful disconnect from the peer or detects that the connection was aborted due to any reason (other than the local NDK consumer's own initiation such as issuing *NdDisconnect* or *NdCloseConnector*).

Below, A and B refer to the two sides of an ND connection. Consumer A refers to the ND consumer on side A, provider A refers to the ND provider on side A, and similarly Consumer B/Provider B refers to those same entities on side B.
When consumer A calls *NdDisconnect*, provider A must send a graceful disconnect notification to side B and complete consumer A's *NdDisconnect* request only when both of the following conditions occur:

-   Either:
    -   A graceful disconnect notification is received from B (which leads to successful completion of consumer A's *NdDisconnect*), or
    -   An error such as connection abortion or time-out occurred (which leads to consumer A's *NdDisconnect* to be completed with a failure).
-   All DMA activity on the QP is finished (including DMA activity for work requests that were posted with silent-success flag).

When provider B receives a graceful disconnect notification from A or detects that the connection is aborted, provider B must deliver *NdDisconnectIndication* to consumer B if consumer B has not called *NdDisconnect* to provider B already. Since an incoming graceful disconnect notification or an abort event can race with the local consumer initiating *NdDisconnect*, local consumer must be prepared to handle an *NdDisconnectIndication* arriving after local consumer calls *NdDisconnect*. Note that an *NdDisconnectIndication* does not provide any guarantees in terms of work request completions.

A disconnected QP or connector cannot be reused by the consumer.

NetworkDirect does not have any notion of half-closed connections. Once *NdDisconnect* is completed (with success or failure), the connection is fully closed.

A consumer should typically call *NdDisconnect* only after it gets completions for all work requests it posted to the initiator queue. Otherwise, the *NdDisconnect* may not lead to a true graceful disconnect. Providers are not required to support graceful disconnect in the case where a consumer leaves such work requests outstanding.

## Related topics


[Network Direct Kernel Provider Interface (NDKPI)](network-direct-kernel-programming-interface--ndkpi-.md)

 

 






