---
title: FLT_PARAMETERS for IRP_MJ_SET_QUOTA union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_SET_QUOTA.
keywords: ["FLT_PARAMETERS for IRP_MJ_SET_QUOTA union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_SET_QUOTA union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_SET_QUOTA**](irp-mj-set-quota.md).

## Syntax

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG Length;
    PVOID QuotaBuffer;
    PMDL  MdlAddress;
  } SetQuota;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

**SetQuota**  
Structure containing the following members.

**Length**  
Length, in bytes, of the buffer that **QuotaBuffer** points to.

**QuotaBuffer**  
Pointer to a caller-supplied, [**FILE_QUOTA_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_quota_information)-structured input buffer that contains the quota information to be set. This member is optional and can be NULL if a MDL is provided in **MdlAddress**. See **Remarks**.

**MdlAddress**  
Address of a memory descriptor list (MDL) that describes the buffer that **QuotaBuffer** points to. This member is optional and can be **NULL** if a buffer is provided in **QuotaBuffer**. See **Remarks**.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP_MJ_SET_QUOTA**](irp-mj-set-quota.md) operations contains the parameters for a set-quota-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

If both a **QuotaBuffer** and **MdlAddress** buffer are provided, it is recommended that minifilters use the MDL. The memory that **QuotaBuffer** points to is valid when it is a user mode address being accessed within the context of the calling process, or if it is a kernel mode address.

If a minifilter changes the value of **MdlAddress**, then after its post operation callback, Filter Manager will free the MDL currently stored in **MdlAddress** and restore the previous value of **MdlAddress**.

IRP_MJ_SET_QUOTA is an IRP-based operation.

## Requirements

**Header**: Fltkernel.h (include Fltkernel.h)


## See also

[**FILE_QUOTA_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_quota_information)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IoCheckQuotaBufferValidity**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckquotabuffervalidity)

[**IRP_MJ_SET_QUOTA**](irp-mj-set-quota.md)
