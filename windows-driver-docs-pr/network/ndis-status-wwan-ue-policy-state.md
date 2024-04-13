---
title: NDIS_STATUS_WWAN_UE_POLICY_STATE
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_UE_POLICY_STATE notification to inform the MB Service of device UE policies
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_UE_POLICY_STATE
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_UE_POLICY_STATE

Miniport drivers use the NDIS_STATUS_WWAN_UE_POLICY_STATE notification to inform the MB Service of device UE policies in response to [OID_WWAN_UE_POLICY](oid-wwan-ue-policy.md) query requests.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS_STATUS_WWAN_UE_POLICY_STATE**](ndis-status-wwan-ue-policy-state.md) structure.

## Requirements

**Version**: Windows 11, version 21H2

**Header**: Ntddndis.h (include Ndis.h)

## See also

[**NDIS_STATUS_WWAN_UE_POLICY_STATE**](ndis-status-wwan-ue-policy-state.md)

[OID_WWAN_UE_POLICY](oid-wwan-ue-policy.md)
