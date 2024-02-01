---
title: FLT_PARAMETERS for IRP_MJ_QUERY_INFORMATION Union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_QUERY_INFORMATION.
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_INFORMATION union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_QUERY_INFORMATION union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_QUERY_INFORMATION**](irp-mj-query-information.md).

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                                    Length;
    FILE_INFORMATION_CLASS POINTER_ALIGNMENT FileInformationClass;
    PVOID                                    InfoBuffer;
  } QueryFileInformation;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **QueryFileInformation**: Structure containing the following members.

- **Length**: Length, in bytes, of the buffer at **InfoBuffer**.

- **FileInformationClass**: Type of file information to be returned. One of the following:

  | Value | Meaning |
  | ----- | ------- |
  | FileAllInformation          | Return a FILE_ALL_INFORMATION structure for the file. |
  | FileAttributeTagInformation | Return a [**FILE_ATTRIBUTE_TAG_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_attribute_tag_information) structure for the file. |
  | FileBasicInformation | Return a [**FILE_BASIC_INFORMATION</strong>**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information) structure for the file. |
  | FileCompressionInformation  | Return a FILE_COMPRESSION_INFORMATION structure for the file. |
  | FileEaInformation           | Return a FILE_EA_INFORMATION structure for the file. |
  | FileInternalInformation     | Return a [**FILE_INTERNAL_INFORMATION</strong>**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_internal_information) structure for the file. |
  | FileMoveClusterInformation  | Return a FILE_MOVE_CLUSTER_INFORMATION structure for the file. |
  | FileNameInformation         | Return a [**FILE_NAME_INFORMATION</strong>**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_name_information) structure for the file. |
  | FileNetworkOpenInformation  | Return a single [**FILE_NETWORK_OPEN_INFORMATION</strong>**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information) structure for the file |
  | FilePositionInformation     | Return a single [**FILE_POSITION_INFORMATION</strong>**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information) structure for the file. |
  | FileStandardInformation     | Return a single [**FILE_STANDARD_INFORMATION</strong>**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_standard_information) structure for the file. |
  | FileStreamInformation       | Return a single [**FILE_STREAM_INFORMATION</strong>**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information) structure for the file. |

- **InfoBuffer**: Pointer to the output buffer where the file information is to be returned.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_QUERY_INFORMATION operations contains the parameters for a query-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

IRP_MJ_QUERY_INFORMATION can be an IRP-based operation or a fast I/O operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FILE_ATTRIBUTE_TAG_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_attribute_tag_information)

[**FILE_BASIC_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information)

[**FILE_INTERNAL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_internal_information)

[**FILE_NAME_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_name_information)

[**FILE_NETWORK_OPEN_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information)

[**FILE_POSITION_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information)

**FILE_POSITION_INFORMATION**
[**FILE_STANDARD_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_standard_information)

[**FILE_STREAM_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IRP_MJ_QUERY_INFORMATION**](irp-mj-query-information.md)
