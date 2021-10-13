---
title: AVCSTRM_WRITE
description: The AVCSTRM_WRITE function code is used to submit a data buffer to be transmitted to the specified stream.
keywords: ["AVCSTRM_WRITE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVCSTRM_WRITE
api_type:
- NA
ms.date: 10/07/2021
ms.localizationpriority: medium
---

# AVCSTRM_WRITE

The **AVCSTRM_WRITE** function code is used to submit a data buffer to be transmitted to the specified stream.

## I/O Status Block

If successful, *avcstrm.sys* sets **Irp->IoStatus.Status** to STATUS_SUCCESS.

Possible error return values include:

| Error Status | Description |
|--|--|
| STATUS_DEVICE_REMOVED | The device corresponding to the **AVCSTRM_READ** operation no longer exists. |
| STATUS_CANCELLED | The request was unable to be completed. |
| STATUS_INVALID_PARAMETER | A parameter specified in the IRP is incorrect, |
| STATUS_INSUFFICIENT_RESOURCES | There were not sufficient system resources to complete the request. |
| STATUS_PENDING | The request has been received but requires further processing. The I/O completion routine will handle the final response. |

## AVC_STREAM_REQUEST_BLOCK Input

**SizeOfThisBlock, Version and Function**  
Use the [**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header) macro to initialize these members. Pass **AVCSTRM_WRITE** in the Request argument of the macro.

**AVCStreamContext**  
Specifies the stream context (handle) returned by an earlier **AVCSTRM_OPEN** call that is the target for the data write operation.

**BufferStruct**  
Specifies the buffer the write operation should obtain data from.

A subunit driver must first allocate an IRP and an [**AVC_STREAM_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avc_stream_request_block) structure.

Next, it should use the [**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header) macro to initialize the AVC_STREAM_REQUEST_BLOCK structure, passing **AVCSTRM_READ** as the Request argument to the macro.

Next, the subunit driver sets the **AVCStreamContext** member to the stream context (handle) of the stream that is the target of the write data operation. Finally, the subunit driver sets the **BufferStruct** member of the **CommandData** union that describes the buffer the write operation obtains data from.

To send this request, a subunit submits an [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](../kernel/irp-mj-internal-device-control.md) IRP with the **IoControlCode** member of the IRP set to [**IOCTL_AVCSTRM_CLASS**](/windows-hardware/drivers/ddi/avcstrm/ni-avcstrm-ioctl_avcstrm_class) and the **Argument1** member of the IRP set to the AVC_STREAM_REQUEST_BLOCK structure that describes the write operation to take place.

This command completes asynchronously. When it is completed, the I/O completion routine set in the IRP is be called.

This function code must be called at IRQL = PASSIVE_LEVEL.

## Comments

This function uses the **BufferStruct** member of the **CommandData** union in the AVC_STREAM_REQUEST_BLOCK structure as shown below.

```cpp
typedef struct _AVC_STREAM_REQUEST_BLOCK {
  ULONG  SizeOfThisBlock;
  ULONG  Version;
  AVCSTRM_FUNCTION  Function;
  .
  .
  PVOID AVCStreamContext;
  .
  .
  union _tagCommandData {
    .
    .
    AVCSTRM_BUFFER_STRUCT  BufferStruct;
    .
    .
  } CommandData;
} AVC_STREAM_REQUEST_BLOCK, *PAVC_STREAM_REQUEST_BLOCK;
```

## Requirements

**Headers:** Declared in *avcstrm.h*. Include *avcstrm.h*.

## See Also

[**AVC_STREAM_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avc_stream_request_block)

[**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header)

[**IRP_MJ_INTERNAL_DEVICE_CONTROL**](../kernel/irp-mj-internal-device-control.md)

[**IOCTL_AVCSTRM_CLASS**](/windows-hardware/drivers/ddi/avcstrm/ni-avcstrm-ioctl_avcstrm_class)

[**AVCSTRM_BUFFER_STRUCT**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avcstrm_buffer_struct)

[**AVCSTRM_FUNCTION**](/windows-hardware/drivers/ddi/avcstrm/ne-avcstrm-_avcstrm_function)
