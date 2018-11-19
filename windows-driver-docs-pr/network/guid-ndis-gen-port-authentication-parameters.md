---
title: GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS
description: This topic describes the GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS GUID for the NDIS WMI interface.
ms.assetid: a61e972b-0969-4ee8-ad57-cf88beda962d
keywords:
- GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS, WDK GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS

WMI clients can use the GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS set GUID to set the port authentication parameters for an NDIS port. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS translates this GUID to the [OID_GEN_PORT_AUTHENTICATION_PARAMETERS](oid-gen-port-authentication-parameters.md) OID to set the current authentication configuration of an NDIS port. Miniport drivers that support NDIS ports must support this OID.

The WMI input buffer specifies an [NDIS_WMI_SET_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567904) structure that is followed by an NDIS_PORT_AUTHENTICATION_PARAMETERS structure.

For more information about port parameters, see [OID_GEN_PORT_AUTHENTICATION_PARAMETERS](oid-gen-port-authentication-parameters.md).

