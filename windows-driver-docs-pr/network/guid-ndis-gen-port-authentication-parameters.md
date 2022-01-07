---
title: GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS
description: This topic describes the GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS, WDK GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS network drivers
ms.date: 11/22/2017
---

# GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS

WMI clients can use the GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS set GUID to set the port authentication parameters for an NDIS port. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS translates this GUID to the [OID_GEN_PORT_AUTHENTICATION_PARAMETERS](oid-gen-port-authentication-parameters.md) OID to set the current authentication configuration of an NDIS port. Miniport drivers that support NDIS ports must support this OID.

The WMI input buffer specifies an [NDIS_WMI_SET_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_set_header) structure that is followed by an NDIS_PORT_AUTHENTICATION_PARAMETERS structure.

For more information about port parameters, see [OID_GEN_PORT_AUTHENTICATION_PARAMETERS](oid-gen-port-authentication-parameters.md).
