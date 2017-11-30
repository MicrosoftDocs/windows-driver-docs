---
title: TCP chimney offload status indications
author: windows-driver-content
description: This topic describes TCP chimney offload status indications 
ms.assetid: 607c9319-82d5-4060-9401-510b7e6e2191
keywords:
- TCP chimney offload status indications, task offload NDIS status indications, TCP chimney offload status indications WDK, TCP chimney offload status indications networking
ms.author: windowsdriverdev
ms.date: 11/10/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TCP chimney offload status indications

\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target can call the [NdisMIndicateStatusEx](https://msdn.microsoft.com/library/windows/hardware/ff563600) function to request the host stack to:

- Stop offloading state objects to the offload target
- Resume offloading state objects to the offload target
- Terminate the offload of all TCP connections that are offloaded to the offload target

This section includes:

[NDIS_STATUS_OFFLOAD_PAUSE](ndis-status-offload-pause.md) 

[NDIS_STATUS_OFFLOAD_RESUME](ndis-status-offload-resume.md) 

[NDIS_STATUS_UPLOAD_ALL](ndis-status-upload-all.md)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")