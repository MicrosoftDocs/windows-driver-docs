---
title: OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA
ms.topic: reference
description: This topic describes the OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA object identifier (OID).
keywords:
- OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA
ms.date: 11/06/2017
---

# OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA

A transport protocol sets OID_TCP_TASK_IPSEC_DELETE_UDPESP_SA to request that a miniport driver delete a UDP-ESP security association (SA) and, possibly, a parser entry from a NIC parser entry list. The SA and parser entry information is formatted as an [OFFLOAD_IPSEC_DELETE_UDPESP_SA](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_offload_ipsec_delete_udpesp_sa) structure.

If the **EncapTypeEntryOffldHandle** is **NULL**, the miniport should delete the specified SA from the NIC and free any system resources allocated for the SA. If the **EncapTypeEntryOffldHandle** is non-**NULL**, the miniport should also delete the specified parser entry from the NIC's parser entry list.

Note that a transport protocol could request a miniport to delete an SA and/or parser entry before the miniport has completed adding that SA and/or parser entry. The miniport must therefore serialize the deletion operation with the addition operation.

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)
