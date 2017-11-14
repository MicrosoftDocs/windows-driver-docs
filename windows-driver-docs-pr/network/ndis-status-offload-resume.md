---
title: NDIS_STATUS_OFFLOAD_RESUME
author: windows-driver-content
description: This topic describes the NDIS_STATUS_OFFLOAD_RESUME status indication.
ms.assetid: 5b7b9056-4f3a-4469-b73a-0bbf3608207a
keywords:
- NDIS_STATUS_OFFLOAD_RESUME, TCP chimney offload NDIS status indications, NDIS_STATUS_OFFLOAD_RESUME WDK, NDIS_STATUS_OFFLOAD_RESUME networking
ms.author: windowsdriverdev
ms.date: 11/10/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NDIS_STATUS_OFFLOAD_RESUME

\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target makes this status indication to request that the host stack resume offloading state objects to it. After an offload target makes this indication, the host stack queries [OID_TCP_TASK_OFFLOAD](oid-tcp-task-offload.md) to obtain the offload target's TCP offload capabilities. The offload target can use this opportunity to report a different set of offload capabilities than it reported during initialization. An offload target can thus use the pause/resume offload mechanism to change its reported TCP offload capabilities.

Note that an offload target does not have to request that the host stack resume offloads. In this case, the offload target keeps processing segments on offloaded TCP connections. However, the host stack will not offload any more state objects to the offload target until the offload target makes the resume offload indication.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")