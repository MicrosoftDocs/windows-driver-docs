---
title: FLT_PARAMETERS for IRP_MJ_QUERY_EA union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_QUERY_EA.
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_EA union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 02/04/2020
ms.localizationpriority: medium
---

# FLT_PARAMETERS for IRP_MJ_QUERY_EA union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_QUERY_EA**](irp-mj-query-ea.md).

## Syntax

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                    Length;
    PVOID                    EaList;
    ULONG                    EaListLength;
    ULONG  POINTER_ALIGNMENT EaIndex;
    PVOID                    EaBuffer;
    PMDL                     MdlAddress;
  } QueryEa;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

**QueryEa**  
Structure within FLT_PARAMETERS union containing the following members.

**Length**  
Length, in bytes, of the buffer that **EaBuffer** points to.

**EaList**  
Pointer to a caller-supplied, FILE_GET_EA_INFORMATION-structured input buffer specifying the extended attributes to be queried.

**EaListLength**  
Length, in bytes, of the buffer that **EaList** points to.

**EaIndex**  
Index of the entry at which to begin scanning the extended-attribute list. This parameter is ignored if the SL_INDEX_SPECIFIED flag is not set in the FLT_IO_PARAMETER_BLOCK structure for the operation or if **EaList** points to a nonempty list.

**EaBuffer**  
Pointer to a caller-supplied, [**FILE_FULL_EA_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)-structured output buffer where the extended attribute values are to be returned. This member is optional and can be **NULL** if a MDL is provided in **MdlAddress**. See **Remarks**.

**MdlAddress**  
Address of a memory descriptor list (MDL) describing the buffer that **EaBuffer** points to. This member is optional and can be **NULL** if a buffer is provided in **EaBuffer**. See **Remarks**.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP_MJ_QUERY_EA**](irp-mj-query-ea.md) operations contains the parameters for an IRP-based query-extended-attributes-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

If both an **EaBuffer** and **MdlAddress** buffer are provided, it is recommended that minifilters use the MDL. The memory that **EaBuffer** points to is valid when it is a user mode address being accessed within the context of the calling process, or if it is a kernel mode address.

If a minifilter changes the value of **MdlAddress**, then after its post operation callback, Filter Manager will free the MDL currently stored in **MdlAddress** and restore the previous value of **MdlAddress**.

IRP_MJ_QUERY_EA is an IRP-based operation.

## Requirements

**Header**: Fltkernel.h (include Fltkernel.h)


## See also

[**FILE_FULL_EA_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IoCheckEaBufferValidity**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckeabuffervalidity)

[**IRP_MJ_QUERY_EA**](irp-mj-query-ea.md)
