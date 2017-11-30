---
title: OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA
author: windows-driver-content
description: This topic describes the OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA object identifier (OID).
ms.assetid: f598199e-48f2-4ff5-846e-e88139408824
keywords:
- OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA
ms.author: windowsdriverdev
ms.date: 11/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA

A transport protocol sets OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA to request that a miniport driver delete a UDP-ESP security association (SA) and, possibly, a parser entry from a NIC parser entry list. The SA and parser entry information is formatted as an [OFFLOAD_IPSEC_DELETE_UDPESP_SA](https://msdn.microsoft.com/library/windows/hardware/ff569059) structure.

If the **EncapTypeEntryOffldHandle** is **NULL**, the miniport should delete the specified SA from the NIC and free any system resources allocated for the SA. If the **EncapTypeEntryOffldHandle** is non-**NULL**, the miniport should also delete the specified parser entry from the NIC's parser entry list.

Note that a transport protocol could request a miniport to delete an SA and/or parser entry before the miniport has completed adding that SA and/or parser entry. The miniport must therefore serialize the deletion operation with the addition operation.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")