---
title: AVC\_FUNCTION\_SEND\_RESPONSE
description: AVC\_FUNCTION\_SEND\_RESPONSE
ms.assetid: f04caed8-8521-4dfa-9bfa-cf71ec7a658e
keywords: ["AVC_FUNCTION_SEND_RESPONSE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_SEND_RESPONSE
api_location:
- avc.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_SEND\_RESPONSE


## <span id="ddk_avc_function_send_response_ks"></span><span id="DDK_AVC_FUNCTION_SEND_RESPONSE_KS"></span>


The **AVC\_FUNCTION\_SEND\_RESPONSE** function code is used to respond to AV/C unit and subunit requests.

### I/O Status Block

If successful, the AV/C protocol driver may set **Irp-&gt;IoStatus.Status** to either:

STATUS\_SUCCESS if the response is discarded due to one or more bus resets since original request, or

STATUS\_PENDING if the response is successfully delivered to *61883.sys* (implies successful delivery to the request initiator).

Possible other return values include:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>STATUS_INSUFFICIENT_RESOURCES</p></td>
<td><p>An internal buffer allocation failed.</p></td>
</tr>
</tbody>
</table>

 

### <span id="headers"></span><span id="HEADERS"></span>Headers

### Comments

This function uses the AVC\_COMMAND\_IRB structure as shown below.

```cpp
typedef struct _AVC_COMMAND_IRB {
  AVC_IRB  Common;
  UCHAR  SubunitAddrFlag : 1;
  UCHAR  AlternateOpcodesFlag : 1;
  UCHAR  TimeoutFlag : 1;
  UCHAR  RetryFlag : 1;
  union {
    UCHAR  CommandType;
    UCHAR  ResponseCode;
  };
  PUCHAR  SubunitAddr;
  PUCHAR  AlternateOpcodes;
  LARGE_INTEGER  Timeout;
  UCHAR  Retries;
  UCHAR  Opcode;
  ULONG  OperandLength;
  UCHAR  Operands[MAX_AVC_OPERAND_BYTES];
  NODE_ADDRESS  NodeAddress;
  ULONG  Generation;
} AVC_COMMAND_IRB, *PAVC_COMMAND_IRB;
```

### <span id="avc_command_irb_input"></span><span id="AVC_COMMAND_IRB_INPUT"></span>AVC\_COMMAND\_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_SEND\_RESPONSE** from the AVC\_FUNCTION enumeration.

<span id="SubunitAddrFlag"></span><span id="subunitaddrflag"></span><span id="SUBUNITADDRFLAG"></span>**SubunitAddrFlag**  
Set to the value obtained from the **AVC\_FUNCTION\_GET\_REQUEST** completion.

<span id="AlternateOpcodesFlag"></span><span id="alternateopcodesflag"></span><span id="ALTERNATEOPCODESFLAG"></span>**AlternateOpcodesFlag**  
Ignored.

<span id="TimeoutFlag"></span><span id="timeoutflag"></span><span id="TIMEOUTFLAG"></span>**TimeoutFlag**  
Ignored.

<span id="RetryFlag"></span><span id="retryflag"></span><span id="RETRYFLAG"></span>**RetryFlag**  
Ignored.

<span id="CommandType"></span><span id="commandtype"></span><span id="COMMANDTYPE"></span>**CommandType**  
Ignored for responses.

<span id="ResponseCode"></span><span id="responsecode"></span><span id="RESPONSECODE"></span>**ResponseCode**  
This member must be set to one of the values from the **AvcResponseCode** enumeration.

<span id="SubunitAddr"></span><span id="subunitaddr"></span><span id="SUBUNITADDR"></span>**SubunitAddr**  
Set to the value obtained from the **AVC\_FUNCTION\_GET\_REQUEST** completion.

<span id="AlternateOpcodes"></span><span id="alternateopcodes"></span><span id="ALTERNATEOPCODES"></span>**AlternateOpcodes**  
Ignored.

<span id="Timeout"></span><span id="timeout"></span><span id="TIMEOUT"></span>**Timeout**  
Ignored.

<span id="Retries"></span><span id="retries"></span><span id="RETRIES"></span>**Retries**  
Ignored.

<span id="Opcode"></span><span id="opcode"></span><span id="OPCODE"></span>**Opcode**  
This must contain the AV/C unit opcode appropriate for the response (may be different than the opcode provided in the original request).

<span id="OperandLength"></span><span id="operandlength"></span><span id="OPERANDLENGTH"></span>**OperandLength**  
Set to the number of bytes in the operand list of the response.

<span id="Operands"></span><span id="operands"></span><span id="OPERANDS"></span>**Operands**  
The operand list of the response.

<span id="NodeAddress"></span><span id="nodeaddress"></span><span id="NODEADDRESS"></span>**NodeAddress**  
The node address of the source of the original request.

<span id="Generation"></span><span id="generation"></span><span id="GENERATION"></span>**Generation**  
The generation ID obtained from the original request.

In the context of the GUID\_AVC\_CLASS device interface, the **AVC\_FUNCTION\_SEND\_RESPONSE** function code is used to respond only to AV/C unit requests.

In the case of virtual instances of *avc.sys* (that is, instances that register the GUID\_VIRTUAL\_AVC\_CLASS device interface), the **AVC\_FUNCTION\_SEND\_RESPONSE** function code is used to respond to AV/C unit *and* subunit requests.

If the first response uses the **AVC\_RESPONSE\_INTERIM** response code (from the **AvcResponseType** enumeration), then follow-up processing is expected. The **NodeAddress** and **Generation** members, obtained by the completion of the **AVC\_FUNCTION\_GET\_REQUEST** original function, must be used in subsequent responses. In any case, the next **AVC\_FUNCTION\_GET\_REQUEST** function should be submitted before returning from the initial **AVC\_FUNCTION\_SEND\_RESPONSE** completion routine, so that the next unit request may be received.

The recommended use of this structure is to use the contents of the original request, and update the **Opcode**, **OperandLength**, and **Operands** members as appropriate for the response.

This function code may be called at IRQL &lt;= DISPATCH\_LEVEL.

### See Also

[**AVC\_FUNCTION\_GET\_REQUEST**](avc-function-get-request.md), [**AvcResponseCode**](https://msdn.microsoft.com/library/windows/hardware/ff554105), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145)

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Avc.h (include Avc.h)</td>
</tr>
</tbody>
</table>

 

 





