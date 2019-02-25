---
title: TAPI extension OIDs for connection-oriented NDIS
description: This topic describes TAPI extension OIDs for connection-oriented NDIS.
ms.assetid: 06f7e2d0-b890-468e-8177-d3c28d0e9cd0
keywords:
- TAPI extension OIDs connection-oriented NDIS
ms.date: 11/03/2017
ms.localizationpriority: medium
---

# TAPI extension OIDs for connection-oriented NDIS

The following table summarizes OIDs that allow TAPI calls to be made over connection-oriented media. Connection-oriented clients send these OIDs to call managers or integrated miniport call manager (MCM) drivers.

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

