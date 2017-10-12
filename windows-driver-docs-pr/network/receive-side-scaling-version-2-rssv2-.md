---
title: Receive Side Scaling Version 2 (RSSv2)
description: This topic describes Receive Side Scaling Version 2 (RSSv2)
ms.assetid: 192CAA41-0D17-4C06-8F13-68EA7C26D023
keywords: Receive Side Scaling Version 2, RSSv2, Receive Side Scaling Version 2 WDK, RSSv2 network drivers
ms.author: windowsdriverdev
ms.date: 10/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

[!include[RSSv2 Beta Prerelease](../rssv2-beta-prerelease.md)]

# Receive Side Scaling Version 2 (RSSv2)

[Receive Side Scaling](ndis-receive-side-scaling2.md) improves the system performance related to handling of network data on multiprocessor systems. NDIS 6.80 and later support RSS Version 2 (RSSv2), which extends RSS by offering per-VPort spreading of queues.

RSSv2 uses the NDIS 6.80 Synchronous Oid request interface for some of its OIDs. For more info about Synchronous OID calls, see [Synchronous OID request interface](synchronous-oid-request-interface-in-ndis-6-80.md).

## Overview



## Advertising RSSv2 capability in a miniport driver



[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")