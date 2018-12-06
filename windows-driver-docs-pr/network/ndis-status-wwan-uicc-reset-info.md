---
title: NDIS_STATUS_WWAN_UICC_RESET_INFO
description: NDIS_STATUS_WWAN_UICC_RESET_INFO
ms.assetid: ADA3ADC9-82AD-423A-ABA4-902EAF5F5C74
keywords:
- NDIS_STATUS_WWAN_UICC_RESET_INFO, UICC reset status notification, Mobile Broadband UICC reset status notification, MB UICC reset status notification
ms.date: 08/18/2017
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_UICC_RESET_INFO

The NDIS_STATUS_WWAN_UICC_RESET_INFO status notification is sent by a modem miniport adapter to inform the MB host of the current passthrough status to a UICC smart card. This notification is sent in the folloiwng two scenarios:

1. After an [OID_WWAN_UICC_RESET](oid-wwan-uicc-reset.md) query request.
2. After UICC reset is complete following an OID_WWAN_UICC_RESET set request, to inform the MB host of the passthrough status of the UICC card post-reset.

This notification uses the [NDIS_WWAN_UICC_RESET_INFO](https://msdn.microsoft.com/library/windows/hardware/9CBAFC44-187A-41ED-9405-1208167AC75D) structure.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ndis.h |

## See also

[OID_WWAN_UICC_RESET](oid-wwan-uicc-reset.md)

[NDIS_WWAN_UICC_RESET_INFO](https://msdn.microsoft.com/library/windows/hardware/9CBAFC44-187A-41ED-9405-1208167AC75D)

[MB low level UICC access](mb-low-level-uicc-access.md)

