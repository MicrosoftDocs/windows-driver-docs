---
title: OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS
ms.topic: reference
description: This topic describes the OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS object identifier (OID).
keywords:
- OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS
ms.date: 03/02/2023
---

# OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS

The OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS OID requests a call manager or MCM driver to translate NDIS call parameters (passed in a [CO_CALL_PARAMETERS](/previous-versions/windows/hardware/network/ff545384(v=vs.85)) structure to the client's [ProtocolClIncomingCall](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_call) function) to TAPI call parameters. The client uses the translated TAPI call parameters returned by the call manager or MCM driver to determine whether to accept or reject the incoming call.

This request uses a CO_TAPI_TRANSLATE_NDIS_CALLPARAMS structure, which is defined as follows:

```c++
typedef struct _CO_TAPI_TRANSLATE_NDIS_CALLPARAMS {
    IN  ULONG               ulFlags;
    IN  NDIS_VAR_DATA_DESC  NdisCallParams;
    OUT NDIS_VAR_DATA_DESC  LineCallInfo;
} CO_TAPI_TRANSLATE_NDIS_CALLPARAMS, *PCO_TAPI_TRANSLATE_NDIS_CALLPARAMS;
```

The members of this structure contain the following information:

**ulFlags**  
The client must set the CO_TAPI_FLAG_INCOMING_CALL bit in **ulFlags**.

**NdisCallParams**  
Specifies an [NDIS_VAR_DATA_DESC](/previous-versions/windows/hardware/network/ff559020(v=vs.85)) structure that contains an offset from the beginning of the NDIS_VAR_DATA_DESC structure to a [CO_CALL_PARAMETERS](/previous-versions/windows/hardware/network/ff545384(v=vs.85)) structure. The NDIS_VAR_DATA_DESC structure also contains the length of the CO_CALL_PARAMETERS structure. The client fills in the CO_CALL_PARAMETERS structure with the NDIS call parameters to be translated to TAPI call parameters.

**LineCallInfo**  
Specifies an [NDIS_VAR_DATA_DESC](/previous-versions/windows/hardware/network/ff559020(v=vs.85)) structure that contains an offset from the beginning of the NDIS_VAR_DATA_DESC structure to a LINE_CALL_INFO structure. The NDIS_VAR_DATA_DESC structure also contains the length of the CO_CALL_PARAMETERS structure. The LINE_CALL_INFO structure specifies the TAPI call parameters into which the given NDIS call parameters have been translated. For more information about the LINE_CALL_INFO structure, see the Windows SDK and the ndistapi.h header file.

## Remarks

If the request is successful, the call manager or MCM driver fills in the LINE_CALL_PARAMS structure referred to by **LineCallInfo** with the translated TAPI call parameters. The call manager or MCM driver must allocate the LINE_CALL_INFO structure within the flat memory section referred to **LineCallInfo**. The client writes the total length of the LINE_CALL_INFO structure to **LineCallInfo.Length**.

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)
