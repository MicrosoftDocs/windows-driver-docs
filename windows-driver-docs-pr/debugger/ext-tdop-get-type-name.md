---
title: EXT_TDOP_GET_TYPE_NAME
description: The EXT\_TDOP\_GET\_TYPE\_NAME sub-operation of the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI Request operation returns the type name of the specified typed data.
keywords: ["EXT_TDOP_GET_TYPE_NAME Windows Debugging"]
topic_type:
- apiref
ms.topic: reference
api_name:
- EXT_TDOP_GET_TYPE_NAME
api_type:
- NA
ms.date: 11/28/2017
---

# EXT\_TDOP\_GET\_TYPE\_NAME


The EXT\_TDOP\_GET\_TYPE\_NAME sub-operation of the [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)[**Request**](request.md) operation returns the type name of the specified typed data.

**Parameters**

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
Set to EXT\_TDOP\_GET\_TYPE\_NAME for this sub-operation.

<span id="InData"></span><span id="indata"></span><span id="INDATA"></span>**InData**  
Specifies the typed data whose type name is being requested.

<span id="StrBufferIndex"></span><span id="strbufferindex"></span><span id="STRBUFFERINDEX"></span>**StrBufferIndex**  
Receives the type name.

<span id="StrBufferChars"></span><span id="strbufferchars"></span><span id="STRBUFFERCHARS"></span>**StrBufferChars**  
Specifies the size, in characters, of the ANSI string buffer **StrBufferIndex**.

<span id="StrCharsNeeded"></span><span id="strcharsneeded"></span><span id="STRCHARSNEEDED"></span>**StrCharsNeeded**  
Receives the size, in characters, of the type name.

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
Receives the status code returned by this sub-operation. This is the same as the value returned by [**Request**](request.md).

## Remarks

EXT\_TDOP\_GET\_TYPE\_NAME is a value in the [**EXT\_TDOP**](/windows-hardware/drivers/ddi/wdbgexts/ne-wdbgexts-_ext_tdop) enumeration.

The parameters for this sub-operation are members of the [**EXT\_TYPED\_DATA**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_ext_typed_data) structure. The members of EXT\_TYPED\_DATA that are not listed in the preceding Parameters section are not used by this sub-operation and should be set to zero. The descriptions of the members in the preceding Parameters section specify what the members are used for. See **EXT\_TYPED\_DATA** for more details.

## <span id="see_also"></span>See also


[**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)

[**EXT\_TDOP**](/windows-hardware/drivers/ddi/wdbgexts/ne-wdbgexts-_ext_tdop)

[**EXT\_TYPED\_DATA**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_ext_typed_data)

[**Request**](request.md)

 

