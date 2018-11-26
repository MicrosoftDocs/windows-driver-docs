---
title: OID_CO_TAPI_TRANSLATE_TAPI_CALLPARAMS
description: This topic describes the OID_CO_TAPI_TRANSLATE_TAPI_CALLPARAMS object identifier (OID).
ms.assetid: bee8871d-9166-4c5a-8428-964f8b321cf1
keywords:
- OID_CO_TAPI_TRANSLATE_TAPI_CALLPARAMS
ms.date: 11/03/2017
ms.localizationpriority: medium
---

# OID_CO_TAPI_TRANSLATE_TAPI_CALLPARAMS

The OID_CO_TAPI_TRANSLATE_TAPI_CALLPARAMS OID requests a call manager or integrated call manager miniport (MCM) driver to translate TAPI call parameters to NDIS call parameters. The client that queries this OID uses the returned NDIS call parameters as an input (formatted as a [CO_CALL_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff545384) structure) to [NdisClMakeCall](https://msdn.microsoft.com/library/windows/hardware/ff561635), with which the client places an outgoing call.

This OID uses a CO_TAPI_TRANSLATE_TAPI_CALLPARAMS structure, which is defined as follows:

```c++
typedef struct _CO_TAPI_TRANSLATE_TAPI_CALLPARAMS {
    IN  ULONG               ulLineID;
    IN  ULONG               ulAddressID;
    IN  ULONG               ulFlags;
    IN  NDIS_VAR_DATA_DESC  DestAddress;
    IN  NDIS_VAR_DATA_DESC  LineCallParams;
    OUT NDIS_VAR_DATA_DESC  NdisCallParams;
} CO_TAPI_TRANSLATE_TAPI_CALLPARAMS, *PCO_TAPI_TRANSLATE_TAPI_CALLPARAMS;
```

The members of this structure contain the following information:

**ulLineID**  
Specifies a zero-based line identifier to which the outgoing call will be directed.

**ulAddressID**  
Specifies a zero-based address identifier (on the line specified by **ulLineID**) to which the outgoing call will be directed.

**ulFlags**  
The client must set the CO_TAPI_FLAG_OUTGOING_CALL bit in **ulFlags**. The client can optionally set the CO_TAPI_USE_DEFAULT_CALLPARAMS bit in **ulFlags** to require the call manager or MCM driver to ignore the **LineCallParams** and return the default NDIS call parameters for the device.

**DestAddress**  
Specifies an [NDIS_VAR_DATA_DESC](https://msdn.microsoft.com/library/windows/hardware/ff559020) structure that contains an offset from the beginning of the NDIS_VAR_DATA_DESC structure to a destination address formatted as a character array. The NDIS_VAR_DATA_DESC structure also contains the length of the destination address. The destination address is the address to which the outgoing call will be directed.

**LineCallParams**  
Specifies an [NDIS_VAR_DATA_DESC](https://msdn.microsoft.com/library/windows/hardware/ff559020) structure that contains an offset from the beginning of the NDIS_VAR_DATA_DESC structure to a LINE_CALL_PARAMS structure. The NDIS_VAR_DATA_DESC structure also contains the length of the LINE_CALL_PARAMS structure. The LINE_CALL_PARAMS structure specifies the TAPI call parameters to be translated into NDIS call parameters. For more information about the LINE_CALL_PARAMS structure, see the Microsoft Windows SDK and the ndistapi.h header file.

**NdisCallParams**  
Specifies an [NDIS_VAR_DATA_DESC](https://msdn.microsoft.com/library/windows/hardware/ff559020) structure that contains an offset from the beginning of the NDIS_VAR_DATA_DESC structure to a CO_CALL_PARAMETERS structure. The NDIS_VAR_DATA_DESC structure also contains the length of the [CO_CALL_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff545384) structure. The CO_CALL_PARAMETERS structure specifies the NDIS call parameters into which the given TAPI call parameters have been translated.

## Remarks

If the request is successful, the call manager or MCM driver fills in the CO_CALL_PARAMETERS structure referenced by **NdisCallParams** with the translated NDIS call parameters. The call manager or MCM driver must allocate the CO_CALL_PARAMETERS structure within the flat memory section referred to by **NdisCallParams**. The client writes the total length of the CO_CALL_PARAMETERS structure to **NdisCallParams.Length**.

If the client sets the CO_TAPI_USE_DEFAULT_CALLPARAMS bit in **ulFlags**, the client does not specify TAPI call parameters. In this case, the call manager or MCM driver should return the default NDIS call parameters for the device. If there are no default NDIS call parameters for the device, the call manager or MCM driver should return NDIS_STATUS_FAILURE.


## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

