---
title: FLT_PARAMETERS for IRP_MJ_READ union
description: The following union component is used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_READ.
ms.assetid: 48674db7-c0cc-45a0-bce9-eaf1a4cec362
keywords: ["FLT_PARAMETERS for IRP_MJ_READ union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT\_PARAMETERS for IRP\_MJ\_READ union


The following union component is used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP\_MJ\_READ**](irp-mj-read.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                   Length;
    ULONG POINTER_ALIGNMENT Key;
    LARGE_INTEGER           ByteOffset;
    PVOID                   ReadBuffer;
    PMDL                    MdlAddress;
  } Read;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**Read**  
Structure containing the following members.

**Length**  
Length, in bytes, of the data to be read.

**Key**  
Key value associated with a byte-range lock on the target file.

**ByteOffset**  
Starting byte offset within the file of the data to be read.

**ReadBuffer**  
Pointer to a buffer that receives the data that is read from the file.

**MdlAddress**  
Address of a memory descriptor list (MDL) that describes the buffer that the **ReadBuffer** member points to. This member is optional and can be **NULL**.

Remarks
-------

The [**FLT\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP\_MJ\_READ operations contains the parameters for a read operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_READ can be an IRP-based operation or a fast I/O operation.

Requirements
------------

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


[**FLT\_CALLBACK\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT\_IS\_FASTIO\_OPERATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://docs.microsoft.com/previous-versions/ff544648(v=vs.85))

[**FLT\_IS\_IRP\_OPERATION**](https://docs.microsoft.com/previous-versions/ff544654(v=vs.85))

[**FLT\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_parameters)

[**FltReadFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltreadfile)

[**IRP\_MJ\_READ**](irp-mj-read.md)

[**ZwReadFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-ntreadfile)

 

 






