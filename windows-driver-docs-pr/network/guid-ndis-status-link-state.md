---
title: GUID_NDIS_STATUS_LINK_STATE
description: This topic describes the GUID_NDIS_STATUS_LINK_STATE GUID for the NDIS WMI interface.
ms.assetid: 7f56d211-14c7-4b8b-8d1c-ee7836b7b70a
keywords:
- GUID_NDIS_STATUS_LINK_STATE, WDK GUID_NDIS_STATUS_LINK_STATE network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_STATUS_LINK_STATE

The GUID_NDIS_STATUS_LINK_STATE event GUID indicates that there has been a change in the link state of a miniport adapter. This WMI GUID is supported in NDIS 6.0 and later versions.

Miniport drivers use the [NDIS_STATUS_LINK_STATE](ndis-status-link-state.md) status indication to notify NDIS and overlying drivers that there has been a change in link state.

When a miniport driver indicates a link state change, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_LINK_STATE event for WMI clients.

The data buffer that NDIS provides with the GUID contains an [NDIS_WMI_EVENT_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567900) structure that is followed by an [NDIS_LINK_STATE](https://msdn.microsoft.com/library/windows/hardware/hh205390) structure. The **NDIS_LINK_STATE** structure specifies the physical state of the medium.

For more information about link status, see [OID_GEN_LINK_STATE](oid-gen-link-state.md) and [NDIS_STATUS_LINK_STATE](ndis-status-link-state.md).

