---
title: FLT_PARAMETERS for IRP_MJ_SYSTEM_CONTROL Union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_SYSTEM_CONTROL.
keywords: ["FLT_PARAMETERS for IRP_MJ_SYSTEM_CONTROL union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_SYSTEM_CONTROL union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP_MJ_SYSTEM_CONTROL.

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG_PTR ProviderId;
    PVOID     DataPath;
    ULONG     BufferSize;
    PVOID     Buffer;
  } WMI;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **WMI**: Structure containing the following members.

- **ProviderId**: The meaning of this parameter depends on the minor function code for the operation. (See the following Remarks section.)

- **DataPath**: The meaning of this parameter depends on the minor function code for the operation. (See the following Remarks section.)

- **BufferSize**: The meaning of this parameter depends on the minor function code for the operation. (See the following Remarks section.)

- **Buffer**: The meaning of this parameter depends on the minor function code for the operation. (See the following Remarks section.)

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_SYSTEM_CONTROL operations contains the parameters for a system-control operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

The meaning of the IRP_MJ_SYSTEM_CONTROL parameters depends on the minor function code. (See the **MinorFunction** member of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.) For more information, see the reference entries for the following minor function codes:

[**IRP_MN_CHANGE_SINGLE_INSTANCE**](../kernel/irp-mn-change-single-instance.md)

[**IRP_MN_CHANGE_SINGLE_ITEM**](../kernel/irp-mn-change-single-item.md)

[**IRP_MN_DISABLE_COLLECTION**](../kernel/irp-mn-disable-collection.md)

[**IRP_MN_DISABLE_EVENTS**](../kernel/irp-mn-disable-events.md)

[**IRP_MN_ENABLE_COLLECTION**](../kernel/irp-mn-enable-collection.md)

[**IRP_MN_ENABLE_EVENTS**](../kernel/irp-mn-enable-events.md)

[**IRP_MN_EXECUTE_METHOD**](../kernel/irp-mn-execute-method.md)

[**IRP_MN_QUERY_ALL_DATA**](../kernel/irp-mn-query-all-data.md)

[**IRP_MN_QUERY_SINGLE_INSTANCE**](../kernel/irp-mn-query-single-instance.md)

[**IRP_MN_REGINFO**](../kernel/irp-mn-reginfo.md)

[**IRP_MN_REGINFO_EX**](../kernel/irp-mn-reginfo-ex.md)

IRP_MJ_SYSTEM_CONTROL is an IRP-based operation.

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

[**IRP_MN_CHANGE_SINGLE_INSTANCE**](../kernel/irp-mn-change-single-instance.md)

[**IRP_MN_CHANGE_SINGLE_ITEM**](../kernel/irp-mn-change-single-item.md)

[**IRP_MN_DISABLE_COLLECTION**](../kernel/irp-mn-disable-collection.md)

[**IRP_MN_DISABLE_EVENTS**](../kernel/irp-mn-disable-events.md)

[**IRP_MN_ENABLE_COLLECTION**](../kernel/irp-mn-enable-collection.md)

[**IRP_MN_ENABLE_EVENTS**](../kernel/irp-mn-enable-events.md)

[**IRP_MN_EXECUTE_METHOD**](../kernel/irp-mn-execute-method.md)

[**IRP_MN_QUERY_ALL_DATA**](../kernel/irp-mn-query-all-data.md)

[**IRP_MN_QUERY_SINGLE_INSTANCE**](../kernel/irp-mn-query-single-instance.md)

[**IRP_MN_REGINFO**](../kernel/irp-mn-reginfo.md)

[**IRP_MN_REGINFO_EX**](../kernel/irp-mn-reginfo-ex.md)
