---
title: AVC\_FUNCTION\_GET\_REQUEST
description: AVC\_FUNCTION\_GET\_REQUEST
ms.assetid: b29df7a8-782b-4014-b47e-7cf917f8e99d
keywords: ["AVC_FUNCTION_GET_REQUEST Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_REQUEST
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AVC\_FUNCTION\_GET\_REQUEST


## <span id="ddk_avc_function_get_request_ks"></span><span id="DDK_AVC_FUNCTION_GET_REQUEST_KS"></span>


The **AVC\_FUNCTION\_GET\_REQUEST** function code is used to register to receive AV/C unit and subunit requests.

### <span id="i_o_status_block"></span><span id="I_O_STATUS_BLOCK"></span>I/O Status Block

This function always sets **Irp-&gt;IoStatus.Status** to STATUS\_PENDING.

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

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### <span id="avc_command_irb_input"></span><span id="AVC_COMMAND_IRB_INPUT"></span>AVC\_COMMAND\_IRB Input

<span id="Common"></span><span id="common"></span><span id="COMMON"></span>**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_GET\_REQUEST** from the AVC\_FUNCTION enumeration.

<span id="SubunitAddrFlag"></span><span id="subunitaddrflag"></span><span id="SUBUNITADDRFLAG"></span>**SubunitAddrFlag**  
Used only when registering to receive unit commands. Set this to 1 and provide a Unit Address in the **SubunitAddr** parameter. Note that for subunit requests, on completion this is set to 1, and the **SubunitAddr** parameter points to memory containing the subunit address for this virtual subunit instance. The caller may access this nonpaged memory, but must not attempt to free it.

<span id="AlternateOpcodesFlag"></span><span id="alternateopcodesflag"></span><span id="ALTERNATEOPCODESFLAG"></span>**AlternateOpcodesFlag**  
Used only when registering to receive unit commands. Set this to 1 and provide a list of opcodes supported by the caller in the **AlternateOpcodes** parameter.

<span id="TimeoutFlag"></span><span id="timeoutflag"></span><span id="TIMEOUTFLAG"></span>**TimeoutFlag**  
Ignored.

<span id="RetryFlag"></span><span id="retryflag"></span><span id="RETRYFLAG"></span>**RetryFlag**  
Ignored.

<span id="CommandType"></span><span id="commandtype"></span><span id="COMMANDTYPE"></span>**CommandType**  
Ignored in input. On output, the **CommandType** member is set to one of the values from the **AvcCommandType** enumeration.

<span id="ResponseCode"></span><span id="responsecode"></span><span id="RESPONSECODE"></span>**ResponseCode**  
Ignored for requests.

<span id="SubunitAddr"></span><span id="subunitaddr"></span><span id="SUBUNITADDR"></span>**SubunitAddr**  
Used only when registering to receive unit commands. Set this to the address of nonpaged memory containing the Unit Address encoded according to Section 5.3.3 of the **AV/C** Digital Interface Command Set General Specification, Rev 3.0 (0xff). This specification can be found at the [1394 Trade Association](http://go.microsoft.com/fwlink/p/?linkid=8728) website. Note that for subunit requests, on completion this points to memory containing the subunit address for this virtual subunit instance. The caller may access this nonpaged memory, but must not attempt to free it.

<span id="AlternateOpcodes"></span><span id="alternateopcodes"></span><span id="ALTERNATEOPCODES"></span>**AlternateOpcodes**  
Used only when registering to receive unit commands. Set this to the address of nonpaged memory containing the list of unit opcodes supported by the caller. The first byte of the opcode list is the count of opcodes to follow (equivalent to the number of bytes). The total length of the memory containing the alternate opcode list is **AlternateOpcodes**\[0\]+1.

<span id="Timeout"></span><span id="timeout"></span><span id="TIMEOUT"></span>**Timeout**  
Ignored.

<span id="Retries"></span><span id="retries"></span><span id="RETRIES"></span>**Retries**  
Ignored.

<span id="Opcode"></span><span id="opcode"></span><span id="OPCODE"></span>**Opcode**  
Ignored on input. On output, this contains an AV/C unit opcode. This is one of the opcodes specified through **AlternateOpcodes**.

<span id="OperandLength"></span><span id="operandlength"></span><span id="OPERANDLENGTH"></span>**OperandLength**  
Ignored on input. On output, this is set to the number of bytes in the operand list used by the request.

<span id="Operands"></span><span id="operands"></span><span id="OPERANDS"></span>**Operands**  
Ignored on input. On output, this parameter contains the operand list of the request.

<span id="NodeAddress"></span><span id="nodeaddress"></span><span id="NODEADDRESS"></span>**NodeAddress**  
Ignored on input. On output, this is set to the node address of the source of the request. This parameter is used when sending the response (for more information, see [**AVC\_FUNCTION\_SEND\_RESPONSE**](avc-function-send-response.md)).

<span id="Generation"></span><span id="generation"></span><span id="GENERATION"></span>**Generation**  
Ignored on input. On output, this is set to the generation count in force when the node address was considered valid. This parameter is used when sending the response (for more information, see [**AVC\_FUNCTION\_SEND\_RESPONSE**](avc-function-send-response.md)).

In the context of the GUID\_AVC\_CLASS Device Interface, the **AVC\_FUNCTION\_GET\_REQUEST** function code is used to register to receive AV/C unit requests only (not subunit requests). This function generally is used by an upper filter driver (of the *avc.sys* FDO) to support peer device functionality (that is, to handle unit requests from the target device from the nonvirtual stack). Although nothing prevents subunit drivers from registering to handle unit requests, subunit driver instances registering to support the same unit opcodes must cooperate with each other to share state information. *Avc.sys* does not directly support multiple registrations for the same unit opcodes.

This function uses the AVC\_COMMAND\_IRB structure. This structure defines the common components of an AV/C command request. The only valid input parameters are **SubunitAddrFlag**, **AlternateOpcodesFlag**, **AlternateOpcodes** and **SubunitAddr**, and all are required. **AlternateOpcodes** must point to a buffer containing the list of unit opcodes supported by the caller. **SubunitAddr** must point to a buffer containing a unit address (0xff).

In the case of virtual instances of *avc.sys* (that is, instances that register the GUID\_VIRTUAL\_AVC\_CLASS device interface) **AVC\_FUNCTION\_GET\_REQUEST** is used to register to receive AV/C unit and subunit requests. Upper filter drivers (of the virtual *avc.sys* FDO) generally register to handle unit requests, while subunit drivers register to handle requests for their particular type of subunit. Although nothing prevents subunit drivers from registering to handle unit requests, subunit driver instances registering to support the same unit opcodes must cooperate with each other to share state information. *Avc.sys* does not directly support multiple registrations for the same unit opcodes.

Subunit drivers do not set any input parameters when registering to receive subunit-specific requests.

This function always returns STATUS\_PENDING, so any processing must be carried out in a completion routine. On completion, the AVC\_COMMAND\_IRB structure holds the opcode and operands of a request. The AV/C protocol requires that a response be sent within 100ms. This may be done from the completion routine by using the **AVC\_FUNCTION\_SEND\_RESPONSE** function.

If the first response uses the **AVC\_RESPONSE\_INTERIM** response code (from the **AvcResponseType** enumeration), then follow-up processing is expected. The **NodeAddress** and **Generation** members, obtained by the completion of the **AVC\_FUNCTION\_GET\_REQUEST** original function, must be used in subsequent responses. In any case, the next **AVC\_FUNCTION\_GET\_REQUEST** function should be submitted before returning from the initial **AVC\_FUNCTION\_SEND\_RESPONSE** completion routine, so that the next unit request may be received.

The recommended use of this structure is to first zero the structure (use **RtlZeroMemory**) before filling in the parameters.

This function code may be called at IRQL &lt;= DISPATCH\_LEVEL.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**AVC\_FUNCTION\_SEND\_RESPONSE**](avc-function-send-response.md), [**AvcResponseCode**](https://msdn.microsoft.com/library/windows/hardware/ff554105), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145), [**RtlZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563610)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVC_FUNCTION_GET_REQUEST%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




