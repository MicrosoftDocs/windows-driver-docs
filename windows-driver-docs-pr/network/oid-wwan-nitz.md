---
title: OID_WWAN_NITZ
ms.topic: reference
description: OID_WWAN_NITZ is used to query the current network time with Network Identity and Time Zone (NITZ).
ms.date: 04/11/2019
keywords: 
- OID_WWAN_NITZ Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID_WWAN_NITZ

OID_WWAN_NITZ is used to query the current network time with Network Identity and Time Zone (NITZ).

Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_NITZ_INFO](ndis-status-wwan-nitz-info.md) status notification containing an [**NDIS_WWAN_NITZ_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_nitz_info) structure that describes the current network time and time zone.

Set requests are not applicable.

## Remarks

For more information about usage of this OID, see [MB NITZ support](mb-nitz-support.md).

## Requirements

**Version**: Windows 10, version 1903
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB NITZ support](mb-nitz-support.md)

[NDIS_STATUS_WWAN_NITZ_INFO](ndis-status-wwan-nitz-info.md)

[**NDIS_WWAN_NITZ_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_nitz_info)
