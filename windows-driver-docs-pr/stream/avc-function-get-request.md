---
title: AVC\_FUNCTION\_GET\_REQUEST
description: AVC\_FUNCTION\_GET\_REQUEST
keywords: ["AVC_FUNCTION_GET_REQUEST Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_REQUEST
api_type:
- NA
ms.date: 06/16/2020
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_GET\_REQUEST

The **AVC\_FUNCTION\_GET\_REQUEST** function code is used to register to receive AV/C unit and subunit requests.

## I/O Status Block

This function always sets **Irp-&gt;IoStatus.Status** to STATUS\_PENDING.

## Comments

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

## Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

## AVC\_COMMAND\_IRB Input

**Common**
  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_GET\_REQUEST** from the AVC\_FUNCTION enumeration.

**SubunitAddrFlag**
  
Used only when registering to receive unit commands. Set this to 1 and provide a Unit Address in the **SubunitAddr** parameter. Note that for subunit requests, on completion this is set to 1, and the **SubunitAddr** parameter points to memory containing the subunit address for this virtual subunit instance. The caller may access this nonpaged memory, but must not attempt to free it.

**AlternateOpcodesFlag**
  
Used only when registering to receive unit commands. Set this to 1 and provide a list of opcodes supported by the caller in the **AlternateOpcodes** parameter.

**TimeoutFlag**
  
Ignored.

**RetryFlag**
  
Ignored.

**CommandType**
  
Ignored in input. On output, the **CommandType** member is set to one of the values from the **AvcCommandType** enumeration.

**ResponseCode**
  
Ignored for requests.

**SubunitAddr**
  
Used only when registering to receive unit commands. Set this to the address of nonpaged memory containing the Unit Address encoded according to Section 5.3.3 of the **AV/C** Digital Interface Command Set General Specification, Rev 3.0 (0xff). This specification can be found at the [1394 Trade Association](https://1394ta.org/library-2/) website. Note that for subunit requests, on completion this points to memory containing the subunit address for this virtual subunit instance. The caller may access this nonpaged memory, but must not attempt to free it.

**AlternateOpcodes**
  
Used only when registering to receive unit commands. Set this to the address of nonpaged memory containing the list of unit opcodes supported by the caller. The first byte of the opcode list is the count of opcodes to follow (equivalent to the number of bytes). The total length of the memory containing the alternate opcode list is **AlternateOpcodes**\[0\]+1.

**Timeout**
  
Ignored.

**Retries**
  
Ignored.

**Opcode**
  
Ignored on input. On output, this contains an AV/C unit opcode. This is one of the opcodes specified through **AlternateOpcodes**.

**OperandLength**
  
Ignored on input. On output, this is set to the number of bytes in the operand list used by the request.

**Operands**
  
Ignored on input. On output, this parameter contains the operand list of the request.

**NodeAddress**
  
Ignored on input. On output, this is set to the node address of the source of the request. This parameter is used when sending the response (for more information, see [**AVC\_FUNCTION\_SEND\_RESPONSE**](avc-function-send-response.md)).

**Generation**
  
Ignored on input. On output, this is set to the generation count in force when the node address was considered valid. This parameter is used when sending the response (for more information, see [**AVC\_FUNCTION\_SEND\_RESPONSE**](avc-function-send-response.md)).

In the context of the GUID\_AVC\_CLASS Device Interface, the **AVC\_FUNCTION\_GET\_REQUEST** function code is used to register to receive AV/C unit requests only (not subunit requests). This function generally is used by an upper filter driver (of the *avc.sys* FDO) to support peer device functionality (that is, to handle unit requests from the target device from the nonvirtual stack). Although nothing prevents subunit drivers from registering to handle unit requests, subunit driver instances registering to support the same unit opcodes must cooperate with each other to share state information. *Avc.sys* does not directly support multiple registrations for the same unit opcodes.

This function uses the AVC\_COMMAND\_IRB structure. This structure defines the common components of an AV/C command request. The only valid input parameters are **SubunitAddrFlag**, **AlternateOpcodesFlag**, **AlternateOpcodes** and **SubunitAddr**, and all are required. **AlternateOpcodes** must point to a buffer containing the list of unit opcodes supported by the caller. **SubunitAddr** must point to a buffer containing a unit address (0xff).

In the case of virtual instances of *avc.sys* (that is, instances that register the GUID\_VIRTUAL\_AVC\_CLASS device interface) **AVC\_FUNCTION\_GET\_REQUEST** is used to register to receive AV/C unit and subunit requests. Upper filter drivers (of the virtual *avc.sys* FDO) generally register to handle unit requests, while subunit drivers register to handle requests for their particular type of subunit. Although nothing prevents subunit drivers from registering to handle unit requests, subunit driver instances registering to support the same unit opcodes must cooperate with each other to share state information. *Avc.sys* does not directly support multiple registrations for the same unit opcodes.

Subunit drivers do not set any input parameters when registering to receive subunit-specific requests.

This function always returns STATUS\_PENDING, so any processing must be carried out in a completion routine. On completion, the AVC\_COMMAND\_IRB structure holds the opcode and operands of a request. The AV/C protocol requires that a response be sent within 100ms. This may be done from the completion routine by using the **AVC\_FUNCTION\_SEND\_RESPONSE** function.

If the first response uses the **AVC\_RESPONSE\_INTERIM** response code (from the **AvcResponseType** enumeration), then follow-up processing is expected. The **NodeAddress** and **Generation** members, obtained by the completion of the **AVC\_FUNCTION\_GET\_REQUEST** original function, must be used in subsequent responses. In any case, the next **AVC\_FUNCTION\_GET\_REQUEST** function should be submitted before returning from the initial **AVC\_FUNCTION\_SEND\_RESPONSE** completion routine, so that the next unit request may be received.

The recommended use of this structure is to first zero the structure (use **RtlZeroMemory**) before filling in the parameters.

This function code may be called at IRQL <= DISPATCH\_LEVEL.

### See also

[**AVC\_FUNCTION\_SEND\_RESPONSE**](avc-function-send-response.md)

[**AvcResponseCode**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavcresponsecode)

[**AVC\_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)

[**RtlZeroMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlzeromemory)
