---
title: NDIS_STATUS_WWAN_MPDP_STATE
description: The NDIS_STATUS_WWAN_MPDP_STATE notification is sent by a mobile broadband miniport driver to inform the MB service about the completion of a previous OID_WWAN_MPDP set request.
ms.assetid: 59B8D9A0-FB22-4252-A24B-A9E58B068C4E
keywords: ["NDIS_STATUS_WWAN_MPDP_STATE, Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_WWAN_MPDP_STATE
api_location:
- ndis.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_MPDP_STATE

The **NDIS_STATUS_WWAN_MPDP_STATE** notification is sent by a mobile broadband miniport driver to inform the MB service about the completion of a previous [OID_WWAN_MPDP](oid-wwan-mpdp.md) set request.

This notification is not sent as an unsolicited event.

This notification uses the [**NDIS_WWAN_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_state) structure.

## Requirements

**Version**: Windows 10, version 1809

**Header**: Ndis.h

