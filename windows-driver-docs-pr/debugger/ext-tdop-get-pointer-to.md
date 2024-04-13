---
title: EXT_TDOP_GET_POINTER_TO
description: The EXT\_TDOP\_GET\_POINTER\_TO sub-operation of the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI Request operation returns a new typed data description that represents a pointer to specified typed data.
keywords: ["EXT_TDOP_GET_POINTER_TO Windows Debugging"]
topic_type:
- apiref
ms.topic: reference
api_name:
- EXT_TDOP_GET_POINTER_TO
api_type:
- NA
ms.date: 11/28/2017
---

# EXT\_TDOP\_GET\_POINTER\_TO


The EXT\_TDOP\_GET\_POINTER\_TO sub-operation of the [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)[**Request**](request.md) operation returns a new typed data description that represents a pointer to specified typed data.

**Parameters**

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
Set to EXT\_TDOP\_GET\_POINTER\_TO for this sub-operation.

<span id="InData"></span><span id="indata"></span><span id="INDATA"></span>**InData**  
Specifies the original typed data description to which a pointer is returned.

<span id="OutData"></span><span id="outdata"></span><span id="OUTDATA"></span>**OutData**  
Receives a typed data description that represents a pointer to the typed data specified by **InData**.

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
Receives the status code returned by this sub-operation. This is the same as the value returned by [**Request**](request.md).

## Remarks

EXT\_TDOP\_GET\_POINTER\_TO is a value in the [**EXT\_TDOP**](/windows-hardware/drivers/ddi/wdbgexts/ne-wdbgexts-_ext_tdop) enumeration.

The parameters for this sub-operation are members of the [**EXT\_TYPED\_DATA**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_ext_typed_data) structure. The members of EXT\_TYPED\_DATA that are not listed in the preceding Parameters section are not used by this sub-operation and should be set to zero. The descriptions of the members in the preceding Parameters section specify what the members are used for. See **EXT\_TYPED\_DATA** for more details.

## <span id="see_also"></span>See also


[**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)

[**EXT\_TDOP**](/windows-hardware/drivers/ddi/wdbgexts/ne-wdbgexts-_ext_tdop)

[**EXT\_TYPED\_DATA**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_ext_typed_data)

[**Request**](request.md)

 

