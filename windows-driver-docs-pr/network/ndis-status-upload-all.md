---
title: NDIS_STATUS_UPLOAD_ALL
description: This topic describes the NDIS_STATUS_UPLOAD_ALL status indication.
ms.assetid: 88a756a6-04a0-410b-9bc7-50e7a67b3685
keywords:
- NDIS_STATUS_UPLOAD_ALL, TCP chimney offload NDIS status indications, NDIS_STATUS_UPLOAD_ALL WDK, NDIS_STATUS_UPLOAD_ALL networking
ms.date: 11/10/2017
ms.localizationpriority: medium
---

# NDIS_STATUS_UPLOAD_ALL

\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target makes this indication to request that the host stack terminate the offload of all the TCP connections that are offloaded to the offload target. This functionality might be used by an 802.3ad-capable intermediate driver when failing over from one NIC to another NIC.

In response to an NDIS_STATUS_UPLOAD_ALL indication, the host stack stops offloading state objects to the offload target and calls the offload target's [MiniportTerminateOffload](https://msdn.microsoft.com/library/windows/hardware/ff559468) function one or more times. The host stack might terminate all the offloaded TCP connections in a single call to the *MiniportTerminateOffload* function, or it might call the *MiniportTerminateOffload* function multiple times.

The host stack also terminates the offload of all of the offload target's path and neighbor state objects. The host stack might terminate the offload of the path neighbor state objects in the same call(s) used to terminate the TCP connections, or it might terminate the path and neighbor state objects in subsequent calls.

After completing the offload termination with a call to [NdisMTerminateOffloadComplete](https://msdn.microsoft.com/library/windows/hardware/ff563685), the offload target can request the host stack to resume offloading state objects. For more information on such a request, see the [NDIS_STATUS_OFFLOAD_RESUME](ndis-status-offload-resume.md) status indication.

