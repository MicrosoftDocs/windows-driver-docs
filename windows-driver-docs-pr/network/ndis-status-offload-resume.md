---
title: NDIS_STATUS_OFFLOAD_RESUME
description: This topic describes the NDIS_STATUS_OFFLOAD_RESUME status indication.
ms.assetid: 5b7b9056-4f3a-4469-b73a-0bbf3608207a
keywords:
- NDIS_STATUS_OFFLOAD_RESUME, TCP chimney offload NDIS status indications, NDIS_STATUS_OFFLOAD_RESUME WDK, NDIS_STATUS_OFFLOAD_RESUME networking
ms.date: 11/10/2017
ms.localizationpriority: medium
---

# NDIS_STATUS_OFFLOAD_RESUME

\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target makes this status indication to request that the host stack resume offloading state objects to it. After an offload target makes this indication, the host stack queries [OID_TCP_TASK_OFFLOAD](oid-tcp-task-offload.md) to obtain the offload target's TCP offload capabilities. The offload target can use this opportunity to report a different set of offload capabilities than it reported during initialization. An offload target can thus use the pause/resume offload mechanism to change its reported TCP offload capabilities.

Note that an offload target does not have to request that the host stack resume offloads. In this case, the offload target keeps processing segments on offloaded TCP connections. However, the host stack will not offload any more state objects to the offload target until the offload target makes the resume offload indication.

