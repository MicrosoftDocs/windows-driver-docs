---
title: EXT\_TDOP\_OUTPUT\_FULL\_VALUE
description: The EXT\_TDOP\_OUTPUT\_FULL\_VALUE sub-operation of the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI Request operation prints the type and value of the specified typed data.
keywords: ["EXT_TDOP_OUTPUT_FULL_VALUE Windows Debugging"]
topic_type:
- apiref
api_name:
- EXT_TDOP_OUTPUT_FULL_VALUE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# EXT\_TDOP\_OUTPUT\_FULL\_VALUE


The EXT\_TDOP\_OUTPUT\_FULL\_VALUE sub-operation of the [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)[**Request**](request.md) operation prints the type and value of the specified typed data.

**Parameters**

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
Set to EXT\_TDOP\_OUTPUT\_FULL\_VALUE for this sub-operation.

<span id="InData"></span><span id="indata"></span><span id="INDATA"></span>**InData**  
Specifies the typed data whose type name and value will be printed.

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
Receives the status code returned by this sub-operation. This is the same as the value returned by [**Request**](request.md).

## Remarks

The type name and formatted value are sent to the debugger engine's [output callbacks](./using-input-and-output.md#output-callbacks). EXT\_TDOP\_OUTPUT\_FULL\_VALUE prints more detailed information about the value than [**EXT\_TDOP\_OUTPUT\_SIMPLE\_VALUE**](ext-tdop-output-simple-value.md). For example, pointers are dereferenced and the values they point to are also printed.

EXT\_TDOP\_OUTPUT\_FULL\_VALUE is a value in the [**EXT\_TDOP**](/windows-hardware/drivers/ddi/wdbgexts/ne-wdbgexts-_ext_tdop) enumeration.

The parameters for this sub-operation are members of the [**EXT\_TYPED\_DATA**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_ext_typed_data) structure. The members of EXT\_TYPED\_DATA that are not listed in the preceding Parameters section are not used by this sub-operation and should be set to zero. The descriptions of the members in the preceding Parameters section specify what the members are used for. See **EXT\_TYPED\_DATA** for more details.

## <span id="see_also"></span>See also


[**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)

[**EXT\_TDOP**](/windows-hardware/drivers/ddi/wdbgexts/ne-wdbgexts-_ext_tdop)

[**EXT\_TYPED\_DATA**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_ext_typed_data)

[**Request**](request.md)

 

