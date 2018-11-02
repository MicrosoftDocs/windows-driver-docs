---
title: EXT\_TDOP\_RELEASE
description: The EXT\_TDOP\_RELEASE sub-operation of the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI Request operation releases a typed data description.
ms.assetid: 4c2bbc65-a98d-4ee7-bbd0-e30b33c330e0
keywords: ["EXT_TDOP_RELEASE Windows Debugging"]
topic_type:
- apiref
api_name:
- EXT_TDOP_RELEASE
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# EXT\_TDOP\_RELEASE


The EXT\_TDOP\_RELEASE sub-operation of the [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)[**Request**](request.md) operation releases a typed data description.

**Parameters**

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
Set to EXT\_TDOP\_RELEASE for this sub-operation.

<span id="InData"></span><span id="indata"></span><span id="INDATA"></span>**InData**  
Specifies the instance of the [**DEBUG\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff541706) structure to release.

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
Receives the status code returned by this sub-operation. This is the same as the value returned by [**Request**](request.md).

Remarks
-------

EXT\_TDOP\_RELEASE is a value in the [**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529) enumeration.

The parameters for this sub-operation are members of the [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) structure. The members of EXT\_TYPED\_DATA that are not listed in the preceding Parameters section are not used by this sub-operation and should be set to zero. The descriptions of the members in the preceding Parameters section specify only the purpose of the members in this particular setting. See **EXT\_TYPED\_DATA** for more details.

## <span id="see_also"></span>See also


[**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)

[**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529)

[**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306)

[**Request**](request.md)

 

 






