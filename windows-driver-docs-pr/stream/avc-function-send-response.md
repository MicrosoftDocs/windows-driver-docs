---
title: AVC\_FUNCTION\_SEND\_RESPONSE
description: AVC\_FUNCTION\_SEND\_RESPONSE
MS-HAID:
- 'avcref\_8e3ab83b-6d29-495e-8c1d-b5c935cff731.xml'
- 'stream.avc\_function\_send\_response'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
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
---

# AVC\_FUNCTION\_SEND\_RESPONSE


## <span id="ddk_avc_function_send_response_ks"></span><span id="DDK_AVC_FUNCTION_SEND_RESPONSE_KS"></span>


The **AVC\_FUNCTION\_SEND\_RESPONSE** function code is used to respond to AV/C unit and subunit requests.

### <span id="i_o_status_block"></span><span id="I_O_STATUS_BLOCK"></span>I/O Status Block

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

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This function uses the AVC\_COMMAND\_IRB structure as shown below.

```
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

<span id="Common"></span><span id="common"></span><span id="COMMON"></span>**Common**  
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

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVC_FUNCTION_SEND_RESPONSE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




