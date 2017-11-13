---
title: NDIS_STATUS_OFFLOAD_PAUSE
author: windows-driver-content
description: This topic describes the NDIS_STATUS_OFFLOAD_PAUSE status indication.
ms.assetid: 1ccb6b72-97fb-4b1c-ac61-5d5dad903a30
keywords:
- NDIS_STATUS_OFFLOAD_PAUSE, TCP chimney offload NDIS status indications, NDIS_STATUS_OFFLOAD_PAUSE WDK, NDIS_STATUS_OFFLOAD_PAUSE networking
ms.author: windowsdriverdev
ms.date: 11/10/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NDIS_STATUS_OFFLOAD_PAUSE

\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target makes this status indication to request that the host stack stop offloading state objects to it. An 802.3ad-capable offload target might do this, for example, before failing over from one NIC to another NIC. In this case, the temporary halt in the offloading of state objects makes it easier for the offload target to accomplish the failover.

A pause request does not affect an offload target's TCP chimney offload processing. The offload target continues such processing as normal. The pause request simply causes the host stack to stop offloading state objects to the offload target.

Note that, after requesting a pause, an offload target must still be prepared to handle calls to its [MiniportInitiateOffload](https://msdn.microsoft.com/library/windows/hardware/ff559393) function. When the offload target requests a pause, there can be offload operations in progress that have not yet reached the offload target. The offload pause indication does not stop offload operations that are in progress. After requesting a pause, an offload target should queue any offload requests that it receives and process them later.

When in the paused state, an offload target might request the host stack to upload all offloaded TCP connections. An 802.3ad-capable offload target might do this, for example, before failing over from one NIC to another NIC. If the offload target receives a send request in this case, it should not complete the request with a status of NDIS_STATUS_PAUSED. Instead, it should complete the request with NDIS_STATUS_UPLOAD_IN_PROGRESS.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")