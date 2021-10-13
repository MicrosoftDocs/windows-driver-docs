---
title: AVCSTRM_OPEN
description: The AVCSTRM_OPEN function code opens a stream with a specific stream format.
keywords: ["AVCSTRM_OPEN Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVCSTRM_OPEN
api_type:
- NA
ms.date: 10/07/2021
ms.localizationpriority: medium
---

# AVCSTRM_OPEN

The **AVCSTRM_OPEN** function code opens a stream with a specific stream format.

## I/O Status Block

If successful, *avcstrm.sys* sets **Irp-&gt;IoStatus.Status** to STATUS_SUCCESS.

If successful, a STATUS_SUCCESS is returned along with the stream context in **AVCStreamContext** member of the [**AVC_STREAM_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avc_stream_request_block) structure. This context is subsequently used for other *avcstrm.sys* requests.

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
Use the [**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header) macro to initialize these members. Pass **AVCSTRM_OPEN** in the Request argument of the macro.

**AVCStreamContext**  
Specifies the stream context (handle). This should be **NULL** on input, and if **AVCSTRM_OPEN** returns successfully, this member contains a valid stream context for subsequent *avcstrm.sys* operations.

**OpenStruct**  
Specifies the description of the AV/C stream to be created.

The [**AVCSTRM_FORMAT**](/windows-hardware/drivers/ddi/avcstrm/ne-avcstrm-_avcstrm_format) enumeration provides the list of supported AV/C streaming formats (from the IEC 61883 specifications) that *avcstrm.sys* supports, such as SDDV (61883-2) and MPEG2TS (61883-4).

In order to make an isochronous connection, the CIP headers and subunit dependent parameters are required and are defined in the [**AVCSTRM_FORMAT_INFO**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avcstrm_format_info) structure.

The following is an example of the MPEG2TS format information for receiving data:

```cpp
//
// MPEG2TS
//
    { 
        sizeof(AVCSTRM_FORMAT_INFO),
        AVCSTRM_FORMAT_MPEG2TS,
        {
            0,0,
            CIP_SPH_MPEG, 
            CIP_QPC_MPEG,
            CIP_FN_MPEG,
            IP_DBS_MPEG,
            0,0
        }, // CIP header[0]
        {
            0,0,0,
            CIP_TSF_OFF,
            CIP_FMT_MPEG,
            2,
        },  // CIP header[1]
        SRC_PACKETS_PER_MPEG2TS_FRAME,   // varies depending on number of source packets
        BUFFER_SIZE_MPEG2TS_NO_SPH,   // Remove source packet header
        NUM_OF_XMT_BUFFERS_MPEG2TS,   // Subunit defined
        0,
        FALSE, // not striping SPH is the default
        0,  
        BLOCK_PERIOD_MPEG2TS, // 192, / number of 1394 cycle offset to send one block
        0,0,0,0,
    },
```

A subunit driver must first allocate an IRP and an [**AVC_STREAM_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avc_stream_request_block) structure.

Next, it should use the [**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header) macro to initialize the AVC_STREAM_REQUEST_BLOCK structure, passing **AVCSTRM_OPEN** as the Request argument to the macro.

Next, the subunit driver sets the **AVCStreamContext** member to **NULL**.

On successful operation, this member should contain a valid stream context (a handle) that is used in subsequent *avcstrm.sys* operations. This member should not be modified thereafter until the stream is closed through [**AVCSTRM_CLOSE**](avcstrm-close.md).. Finally, the subunit driver sets the **OpenStruct** member of the **CommandData** union that describes the stream to be opened.

To send this request, a subunit submits an [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](../kernel/irp-mj-internal-device-control.md) IRP with the **IoControlCode** member of the IRP set to [**IOCTL_AVCSTRM_CLASS**](/windows-hardware/drivers/ddi/avcstrm/ni-avcstrm-ioctl_avcstrm_class) and the **Argument1** member of the IRP set to the AVC_STREAM_REQUEST_BLOCK structure that describes the open operation to take place.

A subunit driver can expect this command to complete synchronously. The result returns immediately without pending operation in *avcstrm.sys*.

This function code must be called at IRQL = PASSIVE_LEVEL.

## Comments

This function uses the **OpenStruct** member of the **CommandData** union in the AVC_STREAM_REQUEST_BLOCK structure as shown below.

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
    AVCSTRM_OPEN_STRUCT  OpenStruct;
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

[**AVCSTRM_OPEN_STRUCT**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avcstrm_open_struct)

[**AVCSTRM_FUNCTION**](/windows-hardware/drivers/ddi/avcstrm/ne-avcstrm-_avcstrm_function)

[**AVCSTRM_FORMAT**](/windows-hardware/drivers/ddi/avcstrm/ne-avcstrm-_avcstrm_format)

[**AVCSTRM_FORMAT_INFO**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avcstrm_format_info)
