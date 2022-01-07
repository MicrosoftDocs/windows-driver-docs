---
title: NDIS_STATUS_WWAN_MPDP_LIST
description: The NDIS_STATUS_WWAN_MPDP_LIST notification is sent by a mobile broadband miniport driver to inform the MB service about the completion of a previous OID_WWAN_MPDP query request.
keywords: ["NDIS_STATUS_WWAN_MPDP_LIST, Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_WWAN_MPDP_LIST
api_location:
- ndis.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# NDIS_STATUS_WWAN_MPDP_LIST

The **NDIS_STATUS_WWAN_MPDP_LIST** notification is sent by a mobile broadband miniport driver to inform the MB service about the completion of a previous [OID_WWAN_MPDP](oid-wwan-mpdp.md) query request.

This notification is not sent as an unsolicited event.

This notification uses the [**NDIS_WWAN_MPDP_LIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_list) structure.

## Requirements

**Version**: Windows 10, version 1809

**Header**: Ndis.h
