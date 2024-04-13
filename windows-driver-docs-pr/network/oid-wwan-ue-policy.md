---
title: OID_WWAN_UE_POLICY
ms.topic: reference
description: OID_WWAN_UE_POLICY returns the UE policies from an MB device.
ms.date: 06/24/2022
keywords: 
 -OID_WWAN_READY_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WWAN_UE_POLICY

OID_WWAN_UE_POLICY returns the UE policies from an MB device.

Set requests are not supported.

Miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request, and later sending an [NDIS_STATUS_WWAN_UE_POLICY_STATE](ndis-status-wwan-ue-policy-state.md) status notification containing an [**NDIS_WWAN_UE_POLICY_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_ue_policy_info) structure that indicates the MB device's UE policies  when completing query requests.

Miniport drivers can also send unsolicited events with this notification.

## Requirements

**Version**: Windows 11, version 21H2

**Header**: Ntddndis.h (include Ndis.h)

## See also

[**NDIS_STATUS_WWAN_UE_POLICY_STATE**](ndis-status-wwan-ue-policy-state.md)

[**NDIS_WWAN_UE_POLICY_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_ue_policy_info)
