---
title: EXT\_TDOP\_SET\_FROM\_U64\_EXPR
description: The EXT\_TDOP\_SET\_FROM\_U64\_EXPR sub-operation of the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSIRequest operation returns a typed data description that represents the value of an expression.
ms.assetid: 3d0007f8-09c7-4333-a1f0-090918c9f8fa
keywords: ["EXT_TDOP_SET_FROM_U64_EXPR Windows Debugging"]
topic_type:
- apiref
api_name:
- EXT_TDOP_SET_FROM_U64_EXPR
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# EXT\_TDOP\_SET\_FROM\_U64\_EXPR


The EXT\_TDOP\_SET\_FROM\_U64\_EXPR sub-operation of the [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)[**Request**](request.md) operation returns a typed data description that represents the value of an expression.

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
Set to EXT\_TDOP\_SET\_FROM\_U64\_EXPR for this sub-operation.

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>**Flags**  
Specifies the bit flags that describe the target's memory in which the value of the expression resides. See [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) for details of these flags.

<span id="InData"></span><span id="indata"></span><span id="INDATA"></span>**InData**  
Specifies optional typed data whose address in the target's memory can be used in the expression specified by **InStrIndex**. This address is used by the expression as the pseudo-register **$extin**.

<span id="OutData"></span><span id="outdata"></span><span id="OUTDATA"></span>**OutData**  
Receives the [**DEBUG\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff541706) structure that represents the value of the expression.

<span id="InStrIndex"></span><span id="instrindex"></span><span id="INSTRINDEX"></span>**InStrIndex**  
Specifies the expression to evaluate. This expression is evaluated by the default expression evaluator.

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
Receives the status code returned by this sub-operation. This is the same as the value returned by [**Request**](request.md).

Remarks
-------

EXT\_TDOP\_SET\_FROM\_U64\_EXPR is a value in the [**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529) enumeration.

The parameters for this sub-operation are members of the [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) structure. The members of EXT\_TYPED\_DATA that are not listed in the preceding Parameters section are not used by this sub-operation and should be set to zero. The descriptions of the members in the preceding Parameters section specify what the members are used for. See **EXT\_TYPED\_DATA** for more details.

## <span id="see_also"></span>See also


[**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)

[**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529)

[**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306)

[**Request**](request.md)

 

 






