---
title: FLT_PARAMETERS for IRP_MJ_SET_EA union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_SET_EA.
keywords: ["FLT_PARAMETERS for IRP_MJ_SET_EA union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_SET_EA union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_SET_EA**](irp-mj-set-ea.md).

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG Length;
    PVOID EaBuffer;
    PMDL  MdlAddress;
  } SetEa;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **SetEa**: Structure containing the following members.

- **Length**: Length, in bytes, of the buffer that **EaBuffer** points to.

- **EaBuffer**: Pointer to a caller-supplied, [**FILE_FULL_EA_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)-structured input buffer that contains the extended attribute (EA) values to be set. This member is optional and can be NULL if a MDL is provided in **MdlAddress**. See **Remarks**.

- **MdlAddress**: Address of a memory descriptor list (MDL) describing the buffer that **EaBuffer** points to. This member is optional and can be **NULL** if a buffer is provided in **EaBuffer**. See **Remarks**.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP_MJ_SET_EA**](irp-mj-set-ea.md) operations contains the parameters for a set-extended-attributes-information-operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

If both an **EaBuffer** and **MdlAddress** buffer are provided, it is recommended that minifilters use the MDL. The memory that **EaBuffer** points to is valid when it is a user mode address being accessed within the context of the calling process, or if it is a kernel mode address.

If a minifilter changes the value of **MdlAddress**, then after its post operation callback, Filter Manager will free the MDL currently stored in **MdlAddress** and restore the previous value of **MdlAddress**.

IRP_MJ_SET_EA is an IRP-based operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FILE_FULL_EA_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IoCheckEaBufferValidity**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckeabuffervalidity)

[**IRP_MJ_SET_EA**](irp-mj-set-ea.md)
