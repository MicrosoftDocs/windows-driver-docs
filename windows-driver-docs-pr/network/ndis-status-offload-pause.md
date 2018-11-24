---
title: NDIS_STATUS_OFFLOAD_PAUSE
description: This topic describes the NDIS_STATUS_OFFLOAD_PAUSE status indication.
ms.assetid: 1ccb6b72-97fb-4b1c-ac61-5d5dad903a30
keywords:
- NDIS_STATUS_OFFLOAD_PAUSE, TCP chimney offload NDIS status indications, NDIS_STATUS_OFFLOAD_PAUSE WDK, NDIS_STATUS_OFFLOAD_PAUSE networking
ms.date: 11/10/2017
ms.localizationpriority: medium
---

# NDIS_STATUS_OFFLOAD_PAUSE

\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target makes this status indication to request that the host stack stop offloading state objects to it. An 802.3ad-capable offload target might do this, for example, before failing over from one NIC to another NIC. In this case, the temporary halt in the offloading of state objects makes it easier for the offload target to accomplish the failover.

A pause request does not affect an offload target's TCP chimney offload processing. The offload target continues such processing as normal. The pause request simply causes the host stack to stop offloading state objects to the offload target.

Note that, after requesting a pause, an offload target must still be prepared to handle calls to its [MiniportInitiateOffload](https://msdn.microsoft.com/library/windows/hardware/ff559393) function. When the offload target requests a pause, there can be offload operations in progress that have not yet reached the offload target. The offload pause indication does not stop offload operations that are in progress. After requesting a pause, an offload target should queue any offload requests that it receives and process them later.

When in the paused state, an offload target might request the host stack to upload all offloaded TCP connections. An 802.3ad-capable offload target might do this, for example, before failing over from one NIC to another NIC. If the offload target receives a send request in this case, it should not complete the request with a status of NDIS_STATUS_PAUSED. Instead, it should complete the request with NDIS_STATUS_UPLOAD_IN_PROGRESS.

