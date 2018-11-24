---
title: GUID_NDIS_GEN_PORT_STATE
description: This topic describes the GUID_NDIS_GEN_PORT_STATE GUID for the NDIS WMI interface.
ms.assetid: 0632843e-ea79-4ada-919e-8ab7d94a4421
keywords:
- GUID_NDIS_GEN_PORT_STATE, WDK GUID_NDIS_GEN_PORT_STATE network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_GEN_PORT_STATE

WMI clients can use the GUID_NDIS_GEN_PORT_STATE method GUID to obtain the state of an NDIS port. This WMI GUID is supported in NDIS 6.0 and later versions.

GUID_NDIS_GEN_PORT_STATE requires a WMI method request to return the state of an NDIS port. The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID, and the WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567903) structure.

NDIS handles this GUID, and miniport drivers do not receive an OID query.

The data buffer that NDIS returns with the GUID contains an [NDIS_PORT_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569624) structure.

For more information about the port state, see [OID_GEN_PORT_STATE](oid-gen-port-state.md).

