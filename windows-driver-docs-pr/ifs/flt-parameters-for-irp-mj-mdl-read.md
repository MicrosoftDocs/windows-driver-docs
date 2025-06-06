---
title: FLT_PARAMETERS for IRP_MJ_MDL_READ Union
description: Describes the FLT_PARAMETERS union member used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_MDL_READ.
keywords: ["FLT_PARAMETERS for IRP_MJ_MDL_READ union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FLT_PARAMETERS for IRP_MJ_MDL_READ union

The following [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) union member is used when [**FLT_IO_PARAMETER_BLOCK.MajorFunction**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) is IRP_MJ_MDL_READ.

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    LARGE_INTEGER           FileOffset;
    ULONG POINTER_ALIGNMENT Length;
    ULONG POINTER_ALIGNMENT Key;
    PMDL                    *MdlChain;
  } MdlRead;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **MdlRead**: Structure containing the following members.

- **FileOffset**: Starting byte within the cached file.

- **Length**: Length, in bytes, of the data to be read from the cached file.

- **Key**: Key value associated with a byte-range lock on the target file. If the range to be read overlaps or is a subrange of an exclusively locked range within the file, this parameter must be the key for that exclusive lock. The exclusive lock must be held by the parent process of the calling thread; otherwise, this parameter is ignored.

- **MdlChain**: Pointer to a variable that receives a pointer to a chain of one or more memory descriptor lists (MDL) that describe the pages containing the data to be read.

## Remarks

IRP_MJ_MDL_READ is a fast I/O operation. It does the same thing as [IRP_MJ_READ](irp-mj-read.md) + IRP_MN_MDL except for the following difference:

- The IRP-based operation sets up caching on the file if it isn’t already cached before doing the MDL work.
- The Fast IO operation fails if the file isn’t already cached.

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_MDL_READ operations contains the parameters for a fast I/O [**MdlRead**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_fast_io_dispatch) operation. The operation is represented by a ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure, with the operation's parameters in the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure that **Iopb** points to.

If a fast I/O IRP_MJ_MDL_READ request fails, the issuer of the I/O determines how to reissue the request. For instance, the request could be reissued as an IRP-based operation using [IRP_MJ_READ](irp-mj-read.md) + IRP_MN_MDL.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flt_is_fastio_operation)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)
