---
title: NDIS_STATUS_UPLOAD_ALL
author: windows-driver-content
description: This topic describes the NDIS_STATUS_UPLOAD_ALL status indication.
ms.assetid: 88a756a6-04a0-410b-9bc7-50e7a67b3685
keywords:
- NDIS_STATUS_UPLOAD_ALL, TCP chimney offload NDIS status indications, NDIS_STATUS_UPLOAD_ALL WDK, NDIS_STATUS_UPLOAD_ALL networking
ms.author: windowsdriverdev
ms.date: 11/10/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NDIS_STATUS_UPLOAD_ALL

\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target makes this indication to request that the host stack terminate the offload of all the TCP connections that are offloaded to the offload target. This functionality might be used by an 802.3ad-capable intermediate driver when failing over from one NIC to another NIC.

In response to an NDIS_STATUS_UPLOAD_ALL indication, the host stack stops offloading state objects to the offload target and calls the offload target's [MiniportTerminateOffload](https://msdn.microsoft.com/library/windows/hardware/ff559468) function one or more times. The host stack might terminate all the offloaded TCP connections in a single call to the *MiniportTerminateOffload* function, or it might call the *MiniportTerminateOffload* function multiple times.

The host stack also terminates the offload of all of the offload target's path and neighbor state objects. The host stack might terminate the offload of the path neighbor state objects in the same call(s) used to terminate the TCP connections, or it might terminate the path and neighbor state objects in subsequent calls.

After completing the offload termination with a call to [NdisMTerminateOffloadComplete](https://msdn.microsoft.com/library/windows/hardware/ff563685), the offload target can request the host stack to resume offloading state objects. For more information on such a request, see the [NDIS_STATUS_OFFLOAD_RESUME](ndis-status-offload-resume.md) status indication.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")