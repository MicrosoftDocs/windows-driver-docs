---
title: FLT_PARAMETERS for IRP_MJ_NETWORK_QUERY_OPEN union
description: The following union component is used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_NETWORK\_QUERY\_OPEN.
keywords: ["FLT_PARAMETERS for IRP_MJ_NETWORK_QUERY_OPEN union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT\_PARAMETERS for IRP\_MJ\_NETWORK\_QUERY\_OPEN union


The following union component is used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP\_MJ\_NETWORK\_QUERY\_OPEN.

## Syntax

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PIRP                           Irp;
    PFILE_NETWORK_OPEN_INFORMATION NetworkInformation;
  } NetworkQueryOpen;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

**NetworkQueryOpen**  
Structure containing the following members.

**Irp**  
Pointer to a create IRP that represents this open operation. This IRP is to be used by the file system for common open/create code but not actually completed.

**NetworkInformation**  
Pointer to a [**FILE\_NETWORK\_OPEN\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information)-structured buffer to receive the requested information about the file.

## Remarks

The [**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP\_MJ\_NETWORK\_QUERY\_OPEN operations contains the parameters for a NetworkQueryOpen operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. The **FLT\_PARAMETERS** structure is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

> [!NOTE]
> The file object associated with IRP\_MJ\_NETWORK\_QUERY\_OPEN is a stack-based object.
A filter registered for the NetworkQueryOpen callback must not reference this object. That is, do not call ObReferenceObject or ObDereferenceObject on this stack-based file object. Also, do not save a pointer to the object.

 

IRP\_MJ\_NETWORK\_QUERY\_OPEN is a fast I/O operation. It is the equivalent of the FastIoQueryOpen (not FastIoQueryNetworkOpenInfo) operation. A filter must register for this operation.

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


[**FILE\_NETWORK\_OPEN\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information)

[**FLT\_CALLBACK\_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT\_IS\_FASTIO\_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT\_IS\_IRP\_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FltQueryInformationFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueryinformationfile)

[**IRP\_MJ\_QUERY\_INFORMATION**](irp-mj-query-information.md)

[**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile)

 

