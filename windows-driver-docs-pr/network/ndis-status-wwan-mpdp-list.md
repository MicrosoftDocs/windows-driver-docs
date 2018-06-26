---
title: NDIS_STATUS_WWAN_MPDP_LIST
description: Miniport drivers use the NDIS_STATUS_WWAN_MPDP_LIST notification to inform the MB service about the completion of a previous OID_WWAN_MPDP query request.
ms.assetid: 20D66ECE-A0F8-4902-BC91-3A3D385DA939
keywords: ["NDIS_STATUS_WWAN_MPDP_LIST, Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_WWAN_MPDP_LIST
api_location:
- ndis.h
api_type:
- HeaderDef
---

# NDIS_STATUS_WWAN_MPDP_LIST

The **NDIS_STATUS_WWAN_MPDP_LIST** notification is sent by the Mobile Broadband WDF class extension (MBBCx) to inform the MB service about the completion of a previous [OID_WWAN_MPDP](oid-wwan-mpdp.md) query request.

MBBCx does not send this notification as an unsolicited event.

This notification uses the [**NDIS_WWAN_MPDP_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_list) structure.

## Requirements

|   |   |
| --- | --- |
| Version | Windows 10, version 1809 |
| Header | Ndis.h |