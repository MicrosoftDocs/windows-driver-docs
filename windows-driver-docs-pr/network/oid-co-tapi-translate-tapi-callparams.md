---
title: OID_CO_TAPI_TRANSLATE_TAPI_CALLPARAMS
author: windows-driver-content
description: This topic describes the OID_CO_TAPI_TRANSLATE_TAPI_CALLPARAMS object identifier (OID).
ms.assetid: bee8871d-9166-4c5a-8428-964f8b321cf1
keywords:
- OID_CO_TAPI_TRANSLATE_TAPI_CALLPARAMS
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")