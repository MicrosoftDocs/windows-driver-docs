---
title: FLT_PARAMETERS for IRP_MJ_QUERY_EA union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_QUERY_EA.
ms.assetid: 858e8c72-33ae-441c-ada9-86c5df0e4f59
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_EA union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
<<<<<<< HEAD
ms.date: 02/04/2020
=======
ms.date: 01/30/2020
>>>>>>> 6a916dfae... Complete first pass on TOC
ms.localizationpriority: medium
---

# FLT_PARAMETERS for IRP_MJ_QUERY_EA union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_QUERY_EA**](irp-mj-query-ea.md).

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
<<<<<<< HEAD
Pointer to a caller-supplied, [**FILE_FULL_EA_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)-structured output buffer where the extended attribute values are to be returned. This member is optional and can be NULL if a MDL is provided in **MdlAddress**. See **Remarks**.
=======
Pointer to a caller-supplied, [**FILE_FULL_EA_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)-structured output buffer where the extended attribute values are to be returned. This member is optional and can be **NULL** if a MDL is provided in **MdlAddress**. See **Remarks**.
>>>>>>> 6a916dfae... Complete first pass on TOC

**MdlAddress**  
Address of a memory descriptor list (MDL) describing the buffer that **EaBuffer** points to. This member is optional and can be **NULL** if a buffer is provided in **EaBuffer**. See **Remarks**.

## Remarks
<<<<<<< HEAD

The [**FLT_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP_MJ_QUERY_EA**](irp-mj-query-ea.md) operations contains the parameters for an IRP-based query-extended-attributes-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

If both an **EaBuffer** and **MdlAddress** buffer are provided, it is recommended that minifilters use the MDL. The memory that **EaBuffer** points to is valid when it is a user mode address being accessed within the context of the calling process, or if it is a kernel mode address.

If a minifilter changes the value of **MdlAddress**, then after its post operation callback, Filter Manager will free the MDL currently stored in **MdlAddress** and restore the previous value of **MdlAddress**.

IRP_MJ_QUERY_EA is an IRP-based operation.

## Requirements

|   |   |
| - | - |
| Header | Fltkernel.h (include Fltkernel.h) |

=======

The [**FLT_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP_MJ_QUERY_EA**](irp-mj-query-ea.md) operations contains the parameters for an IRP-based query-extended-attributes-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

If both an **EaBuffer** and **MdlAddress** buffer are provided, it is recommended that minifilters use the MDL. The memory that **EaBuffer** points to is valid when it is user space being accessed within the process of the calling process, or if it contains system memory addresses.

Filter Manager performs MDL teardown when the operation is completed, so a filter can return FLT_PENDING. Additionally, if a filter swaps out the MDL provided by a higher-level filter with its own MDL, Filter Manager will swap back in the higher level filter's MDL once the operation is complete.

If a minifilter creates its own MDL to pass down instead of using a MDL provided in **MdlAddress**, the filter needs to save and restore the MDL that was passed down to it.

IRP_MJ_QUERY_EA is an IRP-based operation.

## Requirements

|   |   |
| - | - |
| Header | *fltkernel.h (include Fltkernel.h)* |

>>>>>>> 6a916dfae... Complete first pass on TOC
## See also

[**FILE_FULL_EA_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)

[**FLT_CALLBACK_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](https://docs.microsoft.com/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](https://docs.microsoft.com/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IoCheckEaBufferValidity**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckeabuffervalidity)

[**IRP_MJ_QUERY_EA**](irp-mj-query-ea.md)
