---
title: TAPI extension OIDs for connection-oriented NDIS
author: windows-driver-content
description: This topic describes TAPI extension OIDs for connection-oriented NDIS.
ms.assetid: 06f7e2d0-b890-468e-8177-d3c28d0e9cd0
keywords:
- TAPI extension OIDs connection-oriented NDIS
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TAPI extension OIDs for connection-oriented NDIS

OIDs that allow TAPI calls to be made over connection-oriented media. Connection-oriented clients send these OIDs to call managers or integrated miniport call manager (MCM) drivers.

In this table, M indicates an OID is mandatory, while O indicates it is optional.

| Length | Query | Set | Name |
| --- | --- | --- | --- |
| Varies | O |   | [OID_CO_TAPI_ADDRESS_CAPS](oid-co-tapi-address-caps.md) |
| Sizeof(CO_TAPI_CM_CAPS) | O |   | [OID_CO_TAPI_CM_CAPS](oid-co-tapi-cm-caps.md) |
| Varies | O |   | [OID_CO_TAPI_GET_CALL_DIAGNOSTICS](oid-co-tapi-get-call-diagnostics.md) |
| Varies | O |   | [OID_CO_TAPI_LINE_CAPS](oid-co-tapi-line-caps.md) |
| Varies | O |   | [OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS](oid-co-tapi-translate-ndis-callparams.md) |
| Varies | O |   | [OID_CO_TAPI_TRANSLATE_TAPI_CALLPARAMS](oid-co-tapi-translate-tapi-callparams.md) |
| Varies | O |   | [OID_CO_TAPI_TRANSLATE_TAPI_SAP](oid-co-tapi-translate-tapi-sap.md) |

In its call to [NdisCoRequest](https://msdn.microsoft.com/library/windows/hardware/ff551877), the client that queries any of the TAPI extension OIDs must specify an *NdisAfHandle* that identifies the address family to which the request applies. The client can specify an *NdisVcHandle* that identifies the virtual connection (VC) to which the request applies. From this VC handle, the call manager or MCM driver may be able to derive the particular line and perhaps the address to which the request applies.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")