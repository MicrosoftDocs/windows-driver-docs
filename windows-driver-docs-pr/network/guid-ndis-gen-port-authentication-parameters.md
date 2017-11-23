---
title: GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS
author: windows-driver-content
description: This topic describes the GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS GUID for the NDIS WMI interface.
ms.assetid: a61e972b-0969-4ee8-ad57-cf88beda962d
keywords:
- GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS, WDK GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS network drivers
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS

WMI clients can use the GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS set GUID to set the port authentication parameters for an NDIS port. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS translates this GUID to the [OID_GEN_PORT_AUTHENTICATION_PARAMETERS](oid-gen-port-authentication-parameters.md) OID to set the current authentication configuration of an NDIS port. Miniport drivers that support NDIS ports must support this OID.

The WMI input buffer specifies an [NDIS_WMI_SET_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567904) structure that is followed by an NDIS_PORT_AUTHENTICATION_PARAMETERS structure.

For more information about port parameters, see [OID_GEN_PORT_AUTHENTICATION_PARAMETERS](oid-gen-port-authentication-parameters.md).

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")