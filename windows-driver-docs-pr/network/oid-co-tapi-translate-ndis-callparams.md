---
title: OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS
author: windows-driver-content
description: This topic describes the OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS object identifier (OID).
ms.assetid: a56affc9-4118-4322-85bc-f979b70e0dad
keywords:
- OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS

The OID_CO_TAPI_TRANSLATE_NDIS_CALLPARAMS OID requests a call manager or MCM driver to translate NDIS call parameters (passed in a [CO_CALL_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff545384) structure to the client's [ProtocolClIncomingCall](https://msdn.microsoft.com/library/windows/hardware/ff570228) function) to TAPI call parameters. The client uses the translated TAPI call parameters returned by the call manager or MCM driver to determine whether to accept or reject the incoming call.

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
Specifies an [NDIS_VAR_DATA_DESC](https://msdn.microsoft.com/library/windows/hardware/ff559020) structure that contains an offset from the beginning of the NDIS_VAR_DATA_DESC structure to a [CO_CALL_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff545384) structure. The NDIS_VAR_DATA_DESC structure also contains the length of the CO_CALL_PARAMETERS structure. The client fills in the CO_CALL_PARAMETERS structure with the NDIS call parameters to be translated to TAPI call parameters.

**LineCallInfo**  
Specifies an [NDIS_VAR_DATA_DESC](https://msdn.microsoft.com/library/windows/hardware/ff559020) structure that contains an offset from the beginning of the NDIS_VAR_DATA_DESC structure to a LINE_CALL_INFO structure. The NDIS_VAR_DATA_DESC structure also contains the length of the CO_CALL_PARAMETERS structure. The LINE_CALL_INFO structure specifies the TAPI call parameters into which the given NDIS call parameters have been translated. For more information about the LINE_CALL_INFO structure, see the Windows SDK and the ndistapi.h header file.

## Remarks

If the request is successful, the call manager or MCM driver fills in the LINE_CALL_PARAMS structure referred to by **LineCallInfo** with the translated TAPI call parameters. The call manager or MCM driver must allocate the LINE_CALL_INFO structure within the flat memory section referred to **LineCallInfo**. The client writes the total length of the LINE_CALL_INFO structure to **LineCallInfo.Length**.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")