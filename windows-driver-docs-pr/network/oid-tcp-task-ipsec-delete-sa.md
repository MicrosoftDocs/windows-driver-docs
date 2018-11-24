---
title: OID_TCP_TASK_IPSEC_DELETE_SA
description: This topic describes the OID_TCP_TASK_IPSEC_DELETE_SA object identifier (OID).
ms.assetid: 5f3b1f30-ab44-4d1c-96ff-b70ae6cfe324
keywords:
- OID_TCP_TASK_IPSEC_DELETE_SA
ms.date: 11/06/2017
ms.localizationpriority: medium
---

# OID_TCP_TASK_IPSEC_DELETE_SA

The OID_TCP_TASK_IPSEC_DELETE_SA OID is set by a transport protocol to request that a miniport driver delete a security association (SA) from a NIC. The SA information is formatted as an [OFFLOAD_IPSEC_DELETE_SA](https://msdn.microsoft.com/library/windows/hardware/ff569058) structure.

On receiving this request, the miniport driver should delete the specified SA from the NIC and free any system resources allocated for the SA.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

