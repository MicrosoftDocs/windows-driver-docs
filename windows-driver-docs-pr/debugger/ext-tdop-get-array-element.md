---
title: EXT\_TDOP\_GET\_ARRAY\_ELEMENT
description: The EXT\_TDOP\_GET\_ARRAY\_ELEMENT sub-operation of the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI Request operation returns an element from an array.
ms.assetid: 67c87b14-3580-4507-884e-b02576ce7be2
keywords: ["EXT_TDOP_GET_ARRAY_ELEMENT Windows Debugging"]
topic_type:
- apiref
api_name:
- EXT_TDOP_GET_ARRAY_ELEMENT
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# EXT\_TDOP\_GET\_ARRAY\_ELEMENT


The EXT\_TDOP\_GET\_ARRAY\_ELEMENT sub-operation of the [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)[**Request**](request.md) operation returns an element from an array.

**Parameters**

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
Set to EXT\_TDOP\_GET\_ARRAY\_ELEMENT for this sub-operation.

<span id="InData"></span><span id="indata"></span><span id="INDATA"></span>**InData**  
Specifies the array whose element is being requested. **InData** can also specify a pointer, in which case it is treated as an array.

<span id="OutData"></span><span id="outdata"></span><span id="OUTDATA"></span>**OutData**  
Receives the requested element from the array.

<span id="In64"></span><span id="in64"></span><span id="IN64"></span>**In64**  
Specifies the index of the element in the array.

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
Receives the status code returned by this sub-operation. This is the same as the value returned by [**Request**](request.md).

Remarks
-------

EXT\_TDOP\_GET\_ARRAY\_ELEMENT is a value in the [**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529) enumeration.

The parameters for this sub-operation are members of the [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) structure. The members of EXT\_TYPED\_DATA that are not listed in the preceding Parameters section are not used by this sub-operation and should be set to zero. The descriptions of the members in the preceding Parameters section specify what the members are used for. See **EXT\_TYPED\_DATA** for more details.

## <span id="see_also"></span>See also


[**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)

[**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529)

[**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306)

[**Request**](request.md)

 

 






