---
title: NDIS_STATUS_WWAN_NITZ_INFO
description: Miniport drivers use the NDIS_STATUS_WWAN_NITZ_INFO notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_NITZ Query request.
ms.date: 04/11/2019
keywords: 
 -NDIS_STATUS_WWAN_NITZ_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# NDIS_STATUS_WWAN_NITZ_INFO

Miniport drivers use the **NDIS_STATUS_WWAN_NITZ_INFO** notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_NITZ](oid-wwan-nitz.md) Query request.

Miniport drivers send this notification as an unsolicited event to provide the current network time and time zone intformation.

This notification uses the [**NDIS_WWAN_NITZ_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_nitz_info) structure.

## Requirements

**Version**: Windows 10, version 1903
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB modem logging with DSS](mb-modem-logging-with-dss.md)

[OID_WWAN_NITZ](oid-wwan-nitz.md)

[**NDIS_WWAN_NITZ_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_nitz_info)
