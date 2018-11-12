---
title: EXT\_TDOP\_SET\_PTR\_FROM\_TYPE\_ID\_AND\_U64
description: The EXT\_TDOP\_SET\_PTR\_FROM\_TYPE\_ID\_AND\_U64 sub-operation of the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI Request operation creates a typed data description that represents a pointer to a specified memory location with a specified type.
ms.assetid: 1ca61962-718e-4cbd-8e16-f87e0c9ec9af
keywords: ["EXT_TDOP_SET_PTR_FROM_TYPE_ID_AND_U64 Windows Debugging"]
topic_type:
- apiref
api_name:
- EXT_TDOP_SET_PTR_FROM_TYPE_ID_AND_U64
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# EXT\_TDOP\_SET\_PTR\_FROM\_TYPE\_ID\_AND\_U64


The EXT\_TDOP\_SET\_PTR\_FROM\_TYPE\_ID\_AND\_U64 sub-operation of the [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)[**Request**](request.md) operation creates a typed data description that represents a pointer to a specified memory location with a specified type.

**Parameters**

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
Set to EXT\_TDOP\_SET\_PTR\_FROM\_TYPE\_ID\_AND\_U64 for this sub-operation.

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>**Flags**  
Specifies the bit flags that describe the target's memory in which the value of the typed data resides. See [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) for details of these flags.

<span id="InData"></span><span id="indata"></span><span id="INDATA"></span>**InData**  
Specifies the type and memory location. This instance of the [**DEBUG\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff541706) structure can be manually created and populated with the required members. The following members are used:

<span id="ModBase"></span><span id="modbase"></span><span id="MODBASE"></span>**ModBase**  
Specifies the location in the target's virtual memory of the base address of the module that contains the type.

<span id="Offset"></span><span id="offset"></span><span id="OFFSET"></span>**Offset**  
Specifies the location in the target's memory of the data. **Offset** is a virtual memory address unless there are flags present in **Flags** that specify that **Offset** is a physical memory address.

<span id="TypeId"></span><span id="typeid"></span><span id="TYPEID"></span>**TypeId**  
Specifies the type ID of the type.

<span id="OutData"></span><span id="outdata"></span><span id="OUTDATA"></span>**OutData**  
Receives the typed data description that represents a pointer to the memory location and type.

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
Receives the status code returned by this sub-operation. This is the same as the value returned by [**Request**](request.md).

Remarks
-------

EXT\_TDOP\_SET\_PTR\_FROM\_TYPE\_ID\_AND\_U64 is a value in the [**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529) enumeration.

The parameters for this sub-operation are members of the [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) structure. The members of EXT\_TYPED\_DATA that are not listed in the preceding Parameters section are not used by this sub-operation and should be set to zero. The descriptions of the members in the preceding Parameters section specify what the members are used for. See **EXT\_TYPED\_DATA** for more details.

## <span id="see_also"></span>See also


[**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)

[**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529)

[**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306)

[**Request**](request.md)

 

 






