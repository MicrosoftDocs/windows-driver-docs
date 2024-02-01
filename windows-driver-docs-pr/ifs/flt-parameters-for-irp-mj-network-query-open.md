---
title: FLT_PARAMETERS for IRP_MJ_NETWORK_QUERY_OPEN Union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_NETWORK_QUERY_OPEN.
keywords: ["FLT_PARAMETERS for IRP_MJ_NETWORK_QUERY_OPEN union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_NETWORK_QUERY_OPEN union

The following union component is used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP_MJ_NETWORK_QUERY_OPEN.

## Syntax

``` C
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

- **NetworkQueryOpen**: Structure containing the following members.

- **Irp**: Pointer to a create IRP that represents this open operation. This IRP is to be used by the file system for common open/create code but not actually completed.

- **NetworkInformation**: Pointer to a [**FILE_NETWORK_OPEN_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information)-structured buffer to receive the requested information about the file.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_NETWORK_QUERY_OPEN operations contains the parameters for a NetworkQueryOpen operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. The **FLT_PARAMETERS** structure is contained in an [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

> [!NOTE]
> The file object associated with IRP_MJ_NETWORK_QUERY_OPEN is a stack-based object.
A filter registered for the NetworkQueryOpen callback must not reference this object. That is, do not call ObReferenceObject or ObDereferenceObject on this stack-based file object. Also, do not save a pointer to the object.

IRP_MJ_NETWORK_QUERY_OPEN is a fast I/O operation. It is the equivalent of the FastIoQueryOpen (not FastIoQueryNetworkOpenInfo) operation. A filter must register for this operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FILE_NETWORK_OPEN_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FltQueryInformationFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueryinformationfile)

[**IRP_MJ_QUERY_INFORMATION**](irp-mj-query-information.md)

[**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile)
