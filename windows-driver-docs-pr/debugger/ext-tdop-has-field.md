---
title: EXT\_TDOP\_HAS\_FIELD
description: The EXT\_TDOP\_HAS\_FIELD sub-operation of the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI Request operation determines if a structure contains a specified member.
ms.assetid: c1486aff-63d3-4ceb-8dce-45a9c5835c99
keywords: ["EXT_TDOP_HAS_FIELD Windows Debugging"]
topic_type:
- apiref
api_name:
- EXT_TDOP_HAS_FIELD
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# EXT\_TDOP\_HAS\_FIELD


The EXT\_TDOP\_HAS\_FIELD sub-operation of the [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)[**Request**](request.md) operation determines if a structure contains a specified member.

**Parameters**

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
Set to EXT\_TDOP\_HAS\_FIELD for this sub-operation.

<span id="InData"></span><span id="indata"></span><span id="INDATA"></span>**InData**  
Specifies the typed data that is checked for the existence of the member. The typed data is first checked to see if it represents an instance of a structure, then the structure is checked to see if it contains the specified member.

<span id="InStrIndex"></span><span id="instrindex"></span><span id="INSTRINDEX"></span>**InStrIndex**  
Specifies the name of the member. The name is a dot-separated path and can contain sub-members - for example, **mymember.mysubmember**. Pointers on this dot-separated path will automatically be dereferenced. However, a dot operator (**.**) should still be used here instead of the usual C pointer dereference operator (**-&gt;**).

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
Receives the status code returned by this sub-operation. This is the same as the value returned by [**Request**](request.md).

If the typed data contains the member, **Status** receives S\_OK. If the typed data does not contain the member, **Status** receives E\_NOINTERFACE. Other error values might also be returned.

Remarks
-------

EXT\_TDOP\_HAS\_FIELD is a value in the [**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529) enumeration.

The parameters for this sub-operation are members of the [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) structure. The members of EXT\_TYPED\_DATA that are not listed in the preceding Parameters section are not used by this sub-operation and should be set to zero. The descriptions of the members in the preceding Parameters section specify what the members are used for. See **EXT\_TYPED\_DATA** for more details.

## <span id="see_also"></span>See also


[**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)

[**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529)

[**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306)

[**Request**](request.md)

 

 






