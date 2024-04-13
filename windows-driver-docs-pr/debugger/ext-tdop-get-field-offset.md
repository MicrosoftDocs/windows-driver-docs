---
title: EXT_TDOP_GET_FIELD_OFFSET
description: The EXT\_TDOP\_GET\_FIELD\_OFFSET sub-operation of the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI Request operation returns the offset of a member within a structure.
keywords: ["EXT_TDOP_GET_FIELD_OFFSET Windows Debugging"]
topic_type:
- apiref
ms.topic: reference
api_name:
- EXT_TDOP_GET_FIELD_OFFSET
api_type:
- NA
ms.date: 11/28/2017
---

# EXT\_TDOP\_GET\_FIELD\_OFFSET


The EXT\_TDOP\_GET\_FIELD\_OFFSET sub-operation of the [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)[**Request**](request.md) operation returns the offset of a member within a structure.

**Parameters**

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
Set to EXT\_TDOP\_GET\_FIELD\_OFFSET for this sub-operation.

<span id="InData"></span><span id="indata"></span><span id="INDATA"></span>**InData**  
Specifies the typed data that represents an instance of a structure that contains the member whose offset is being requested.

<span id="InStrIndex"></span><span id="instrindex"></span><span id="INSTRINDEX"></span>**InStrIndex**  
Specifies the name of the member whose offset is being requested. The name is a dot-separated path and can contain sub-members. For example, **mymember.mysubmember**. Pointers on this dot-separated path will automatically be dereferenced. However, a dot operator (**.**) should still be used here instead of the usual C pointer dereference operator (**-&gt;**).

<span id="Out32"></span><span id="out32"></span><span id="OUT32"></span>**Out32**  
Receives the offset of the member within an instance of the structure. This is the number of bytes between the beginning of an instance of the structure and the member.

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
Receives the status code returned by this sub-operation. This is the same as the value returned by [**Request**](request.md).

## Remarks

EXT\_TDOP\_GET\_FIELD\_OFFSET is a value in the [**EXT\_TDOP**](/windows-hardware/drivers/ddi/wdbgexts/ne-wdbgexts-_ext_tdop) enumeration.

The parameters for this sub-operation are members of the [**EXT\_TYPED\_DATA**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_ext_typed_data) structure. The members of EXT\_TYPED\_DATA that are not listed in the preceding Parameters section are not used by this sub-operation and should be set to zero. The descriptions of the members in the preceding Parameters section specify what the members are used for. See **EXT\_TYPED\_DATA** for more details.

## <span id="see_also"></span>See also


[**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)

[**EXT\_TDOP**](/windows-hardware/drivers/ddi/wdbgexts/ne-wdbgexts-_ext_tdop)

[**EXT\_TYPED\_DATA**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_ext_typed_data)

[**Request**](request.md)

 

