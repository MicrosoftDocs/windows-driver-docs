---
title: FLT_PARAMETERS for IRP_MJ_PREPARE_MDL_WRITE Union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_PREPARE_MDL_WRITE.
keywords: ["FLT_PARAMETERS for IRP_MJ_PREPARE_MDL_WRITE union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_PREPARE_MDL_WRITE union

The following union component is used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP_MJ_PREPARE_MDL_WRITE.

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    LARGE_INTEGER           FileOffset;
    ULONG POINTER_ALIGNMENT Length;
    ULONG POINTER_ALIGNMENT Key;
    PMDL                    *MdlChain;
  } PrepareMdlWrite;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **PrepareMdlWrite**: Structure containing the following members.

- **FileOffset**: Starting byte within the cached file.

- **Length**: Length, in bytes, of the data to be written to the cached file.

- **Key**: Key value associated with a byte-range lock on the target file. If the range to be written overlaps or is a subrange of an exclusively locked range within the file, this parameter must be the key for that exclusive lock,. The exclusive lock must be held by the parent process of the calling thread; otherwise, this parameter is ignored.

- **MdlChain**: Pointer to a variable that receives a pointer to a chain of one or more memory descriptor lists (MDL) that describe the pages containing the data to be written.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_PREPARE_MDL_WRITE operations contains the parameters for a fast I/O **PrepareMdlWrite** operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

If a fast I/O IRP_MJ_PREPARE_MDL_WRITE request fails, the issuer of the I/O determines how to reissue the request. A minifilter may not always get an IRP-based IRP_MJ_MDL_WRITE. For instance, the IRP request could be reissued as IRP_MJ_WRITE/IRP_MN_MDL.

IRP_MJ_PREPARE_MDL_WRITE is a fast I/O operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)
