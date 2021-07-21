---
title: FLT_PARAMETERS for IRP_MJ_SYSTEM_CONTROL union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_SYSTEM\_CONTROL.
keywords: ["FLT_PARAMETERS for IRP_MJ_SYSTEM_CONTROL union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FLT\_PARAMETERS for IRP\_MJ\_SYSTEM\_CONTROL union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP\_MJ\_SYSTEM\_CONTROL.

## Syntax

```ManagedCPlusPlus
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

**WMI**  
Structure containing the following members.

**ProviderId**  
The meaning of this parameter depends on the minor function code for the operation. (See the following Remarks section.)

**DataPath**  
The meaning of this parameter depends on the minor function code for the operation. (See the following Remarks section.)

**BufferSize**  
The meaning of this parameter depends on the minor function code for the operation. (See the following Remarks section.)

**Buffer**  
The meaning of this parameter depends on the minor function code for the operation. (See the following Remarks section.)

## Remarks

The [**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP\_MJ\_SYSTEM\_CONTROL operations contains the parameters for a system-control operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

The meaning of the IRP\_MJ\_SYSTEM\_CONTROL parameters depends on the minor function code. (See the **MinorFunction** member of the [**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.) For more information, see the reference entries for the following minor function codes:

[**IRP\_MN\_CHANGE\_SINGLE\_INSTANCE**](../kernel/irp-mn-change-single-instance.md)

[**IRP\_MN\_CHANGE\_SINGLE\_ITEM**](../kernel/irp-mn-change-single-item.md)

[**IRP\_MN\_DISABLE\_COLLECTION**](../kernel/irp-mn-disable-collection.md)

[**IRP\_MN\_DISABLE\_EVENTS**](../kernel/irp-mn-disable-events.md)

[**IRP\_MN\_ENABLE\_COLLECTION**](../kernel/irp-mn-enable-collection.md)

[**IRP\_MN\_ENABLE\_EVENTS**](../kernel/irp-mn-enable-events.md)

[**IRP\_MN\_EXECUTE\_METHOD**](../kernel/irp-mn-execute-method.md)

[**IRP\_MN\_QUERY\_ALL\_DATA**](../kernel/irp-mn-query-all-data.md)

[**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](../kernel/irp-mn-query-single-instance.md)

[**IRP\_MN\_REGINFO**](../kernel/irp-mn-reginfo.md)

[**IRP\_MN\_REGINFO\_EX**](../kernel/irp-mn-reginfo-ex.md)

IRP\_MJ\_SYSTEM\_CONTROL is an IRP-based operation.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Fltkernel.h (include Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FLT\_CALLBACK\_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT\_IS\_FASTIO\_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT\_IS\_IRP\_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IRP\_MN\_CHANGE\_SINGLE\_INSTANCE**](../kernel/irp-mn-change-single-instance.md)

[**IRP\_MN\_CHANGE\_SINGLE\_ITEM**](../kernel/irp-mn-change-single-item.md)

[**IRP\_MN\_DISABLE\_COLLECTION**](../kernel/irp-mn-disable-collection.md)

[**IRP\_MN\_DISABLE\_EVENTS**](../kernel/irp-mn-disable-events.md)

[**IRP\_MN\_ENABLE\_COLLECTION**](../kernel/irp-mn-enable-collection.md)

[**IRP\_MN\_ENABLE\_EVENTS**](../kernel/irp-mn-enable-events.md)

[**IRP\_MN\_EXECUTE\_METHOD**](../kernel/irp-mn-execute-method.md)

[**IRP\_MN\_QUERY\_ALL\_DATA**](../kernel/irp-mn-query-all-data.md)

[**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](../kernel/irp-mn-query-single-instance.md)

[**IRP\_MN\_REGINFO**](../kernel/irp-mn-reginfo.md)

[**IRP\_MN\_REGINFO\_EX**](../kernel/irp-mn-reginfo-ex.md)

 

