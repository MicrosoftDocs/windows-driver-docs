---
title: AVC\_FUNCTION\_COMMAND
description: AVC\_FUNCTION\_COMMAND
ms.assetid: 5e1f7f93-83ef-4015-a952-f7efd93ccee5
keywords: ["AVC_FUNCTION_COMMAND Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_COMMAND
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_COMMAND


## <span id="ddk_avc_function_command_ks"></span><span id="DDK_AVC_FUNCTION_COMMAND_KS"></span>


The **AVC\_FUNCTION\_COMMAND** function code is used to send an AV/C request and receive a response as one operation.

### I/O Status Block

If successful, the AV/C protocol driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

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
<td><p>STATUS_TIMEOUT</p></td>
<td><p>The request was made, but no response was received before all time-out and retry processing was complete. The target device ignores requests if a previous request is still being processed. Some AV/C devices are noncompliant, and refuse to respond within the 100-ms time-out, even after several successive attempts. The AVC_COMMAND_IRB structure permits the adjustment of the default <strong>Timeout</strong> and <strong>Retries</strong> members (100ms and 9, respectively), but these default settings have been sufficient for all known implementations.</p></td>
</tr>
<tr class="even">
<td><p>STATUS_PENDING</p></td>
<td><p>The request was made, and an interim response was received. It is the responsibility of the completion routine to handle the final response and free the IRP and IRB resources.</p></td>
</tr>
<tr class="odd">
<td><p>STATUS_REQUEST_ABORTED</p></td>
<td><p>When submitting AV/C requests, immediately abort when the IRP completion status is STATUS_REQUEST_ABORTED.</p></td>
</tr>
<tr class="even">
<td><p>STATUS_*</p></td>
<td><p>Any other return code indicates that an error or warning occurred that was beyond the scope of the AV/C protocol.</p></td>
</tr>
</tbody>
</table>

 

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

### Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### <span id="avc_command_irb_input"></span><span id="AVC_COMMAND_IRB_INPUT"></span>AVC\_COMMAND\_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_COMMAND** from the AVC\_FUNCTION enumeration.

<span id="SubunitAddrFlag"></span><span id="subunitaddrflag"></span><span id="SUBUNITADDRFLAG"></span>**SubunitAddrFlag**  
Set this to one to override the subunit address that *avc.sys* associates with the subunit driver. Reasons to override include: the subunit driver represents multiple subunits in a single instance; a unit command must be sent; or the driver was loaded because *avc.sys* could not determine the subunit type or ID. If this is set, the **SubunitAddr** member must point to nonpaged memory containing the desired subunit address.

This must be set to one (and the appropriate **SubunitAddr** supplied) if the caller is submitting requests directly to an *avc.sys* FDO.

Note: If this flag is not set on request, on response from a successful request, this flag is set, and the **SubunitAddr** member points to the actual address of the subunit. Do not attempt to alter the contents or free the memory: it is part of the parent driver's device extension. This may, of course, be set back to zero, and the **SubunitAddr** pointer cleared to reuse the structure for a different subunit.

<span id="AlternateOpcodesFlag"></span><span id="alternateopcodesflag"></span><span id="ALTERNATEOPCODESFLAG"></span>**AlternateOpcodesFlag**  
Set this to one if the command type and opcode of this request results in a response with a different opcode. Without this, only responses with matching opcodes are accepted. If this is set, the **AlternateOpcodes** member must pointer to nonpaged memory containing the list of alternate opcodes.

<span id="TimeoutFlag"></span><span id="timeoutflag"></span><span id="TIMEOUTFLAG"></span>**TimeoutFlag**  
Set this to one if the default time-out is not appropriate for the subunit. If this is set, the **Timeout** member must be set to the desired time-out (in 100-ns units).

<span id="RetryFlag"></span><span id="retryflag"></span><span id="RETRYFLAG"></span>**RetryFlag**  
Set this to one if the default retry count is not appropriate for the subunit. If this is set, the **Retries** member must be set to the desired retry count.

<span id="CommandType"></span><span id="commandtype"></span><span id="COMMANDTYPE"></span>**CommandType**  
On request, this member must be set to one of the enumerators from the **AvcCommandType** enumeration. This is a required parameter.

<span id="ResponseCode"></span><span id="responsecode"></span><span id="RESPONSECODE"></span>**ResponseCode**  
On response, this member is set to a value from the **AvcResponseCode** enumeration.

<span id="SubunitAddr"></span><span id="subunitaddr"></span><span id="SUBUNITADDR"></span>**SubunitAddr**  
Set this to the address of nonpaged memory containing the desired subunit address encoded according to Section 5.3.3 of the AV/C Digital Interface Command Set General Specification, Rev 3.0. This specification can be found at the [1394 Trade Association](http://go.microsoft.com/fwlink/p/?linkid=8728) website. No length is necessary because the subunit address encoding implies this. This parameter is ignored if **SubunitAddrFlag** is zero.

<span id="AlternateOpcodes"></span><span id="alternateopcodes"></span><span id="ALTERNATEOPCODES"></span>**AlternateOpcodes**  
Set this to the address of nonpaged memory containing the desired alternate opcode list. The first byte of the opcode list is the count of opcodes to follow (equivalent to the number of bytes). The total length of the memory containing the alternate opcode list is AlternateOpcodes\[0\]+1. This parameter is ignored if **AlternateOpcodesFlag** is zero.

<span id="Timeout"></span><span id="timeout"></span><span id="TIMEOUT"></span>**Timeout**  
Set this to the desired time-out in 100-ns units. For example, the default time-out value is: **Timeout.QuadPart** = 1000000 (100ms in 100ns units). This parameter is ignored if **TimeoutFlag** is zero.

<span id="Retries"></span><span id="retries"></span><span id="RETRIES"></span>**Retries**  
Set this to the desired number of times *avc.sys* should attempt to retry requests after each time-out without a response. Note that a retry count of zero means that the request is tried once. The total amount of time spent trying to process a command without getting a response is calculated by the following formula:

***Timeout*** *\* (***<em>Retries</em>** *+ 1)*

This parameter is ignored if **RetryFlag** is zero.

<span id="Opcode"></span><span id="opcode"></span><span id="OPCODE"></span>**Opcode**  
Set this to the desired AV/C opcode (appropriate for the subunit type). This is a required parameter. On response, if **AlternateOpcodesFlag** was set, and one of the alternate opcodes was used to match the response, this is set to that alternate opcode.

<span id="OperandLength"></span><span id="operandlength"></span><span id="OPERANDLENGTH"></span>**OperandLength**  
Set this to the number of bytes used to store the operands in the **Operands** member. This is a required parameter. On response, this parameter is set to the number of bytes in the operand list used by the response.

<span id="Operands"></span><span id="operands"></span><span id="OPERANDS"></span>**Operands**  
Set this to the operand list appropriate for the subunit type and opcode. This is a required parameter. On response, this parameter contains the operand list of the response.

<span id="NodeAddress"></span><span id="nodeaddress"></span><span id="NODEADDRESS"></span>**NodeAddress**  
Reserved. This must be zero.

<span id="Generation"></span><span id="generation"></span><span id="GENERATION"></span>**Generation**  
Reserved. This must be zero.

The **AVC\_FUNCTION\_COMMAND** function code is not supported by virtual instances of *avc.sys*. If the caller wishes to control an external device, that device's nonvirtual instance can be located through a private mechanism, or through some combination of the AVC\_FUNCTION\_FIND\_PEER\_DO, **AVC\_FUNCTION\_PEER\_DO\_LIST** and **AVC\_FUNCTION\_GET\_SUBUNIT\_INFO** function codes of the IOCTL\_AVC\_CLASS I/O control code.

This structure defines the common components of an AV/C command request. It holds the opcode and operands of a request, and the opcode and operands of a response (upon completion). The size of the operand list is fixed at the maximum allowable number of operands given a one-byte subunit address. If the subunit address is extended in any way, the maximum permissible number of operand bytes is reduced accordingly.

The recommended use of this structure is to first zero the structure (use **RtlZeroMemory**) before filling in the parameters.

This must be called at IRQL = PASSIVE\_LEVEL.

### See Also

[**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145), [**AvcCommandType**](https://msdn.microsoft.com/library/windows/hardware/ff554099), [**AvcResponseCode**](https://msdn.microsoft.com/library/windows/hardware/ff554105), [**AVC\_FUNCTION\_FIND\_PEER\_DO**](avc-function-find-peer-do.md), [**AVC\_FUNCTION\_PEER\_DO\_LIST**](avc-function-peer-do-list.md), [**AVC\_FUNCTION\_GET\_SUBUNIT\_INFO**](avc-function-get-subunit-info.md)

 

 





