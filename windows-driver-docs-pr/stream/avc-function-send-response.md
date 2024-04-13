---
title: AVC_FUNCTION_SEND_RESPONSE
description: The AVC_FUNCTION_SEND_RESPONSE function code is used to respond to AV/C unit and subunit requests.
keywords: ["AVC_FUNCTION_SEND_RESPONSE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- AVC_FUNCTION_SEND_RESPONSE
api_location:
- avc.h
api_type:
- HeaderDef
ms.date: 07/27/2021
---

# AVC_FUNCTION_SEND_RESPONSE

The **AVC_FUNCTION_SEND_RESPONSE** function code is used to respond to AV/C unit and subunit requests.

## I/O Status Block

If successful, the AV/C protocol driver may set **Irp->IoStatus.Status** to either:

- STATUS_SUCCESS if the response is discarded due to one or more bus resets since original request, or

- STATUS_PENDING if the response is successfully delivered to *61883.sys* (implies successful delivery to the request initiator)

Possible other return values include:

| Return value | Description |
|--|--|
| STATUS_INSUFFICIENT_RESOURCES | An internal buffer allocation failed. |

## Comments

This function uses the AVC_COMMAND_IRB structure as shown below.

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

**Header:** Avc.h (include Avc.h)

### AVC_COMMAND_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC_FUNCTION_SEND_RESPONSE** from the AVC_FUNCTION enumeration.

**SubunitAddrFlag**  
Set to the value obtained from the **AVC_FUNCTION_GET_REQUEST** completion.

**AlternateOpcodesFlag**  
Ignored.

**TimeoutFlag**  
Ignored.

**RetryFlag**  
Ignored.

**CommandType**  
Ignored for responses.

**ResponseCode**  
This member must be set to one of the values from the **AvcResponseCode** enumeration.

 **SubunitAddr**  
Set to the value obtained from the **AVC_FUNCTION_GET_REQUEST** completion.

**AlternateOpcodes**  
Ignored.

**Timeout**  
Ignored.

**Retries**  
Ignored.

**Opcode**  
This must contain the AV/C unit opcode appropriate for the response (may be different than the opcode provided in the original request).

**OperandLength**  
Set to the number of bytes in the operand list of the response.

**Operands**  
The operand list of the response.

**NodeAddress**  
The node address of the source of the original request.

**Generation**  
The generation ID obtained from the original request.

In the context of the GUID_AVC_CLASS device interface, the **AVC_FUNCTION_SEND_RESPONSE** function code is used to respond only to AV/C unit requests.

In the case of virtual instances of *avc.sys* (that is, instances that register the GUID_VIRTUAL_AVC_CLASS device interface), the **AVC_FUNCTION_SEND_RESPONSE** function code is used to respond to AV/C unit *and* subunit requests.

If the first response uses the **AVC_RESPONSE_INTERIM** response code (from the **AvcResponseType** enumeration), then follow-up processing is expected. The **NodeAddress** and **Generation** members, obtained by the completion of the **AVC_FUNCTION_GET_REQUEST** original function, must be used in subsequent responses. In any case, the next **AVC_FUNCTION_GET_REQUEST** function should be submitted before returning from the initial **AVC_FUNCTION_SEND_RESPONSE** completion routine, so that the next unit request may be received.

The recommended use of this structure is to use the contents of the original request, and update the **Opcode**, **OperandLength**, and **Operands** members as appropriate for the response.

This function code may be called at IRQL >= DISPATCH_LEVEL.

### See Also

[**AVC_FUNCTION_GET_REQUEST**](avc-function-get-request.md)

[**AvcResponseCode**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavcresponsecode)

[**AVC_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)
