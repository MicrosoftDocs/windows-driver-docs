---
title: FLT_PARAMETERS for IRP_MJ_CREATE union
description: The following union component is used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_CREATE.
ms.assetid: aa223d51-7d13-4244-bad5-db14f1fb0d2c
keywords: ["FLT_PARAMETERS for IRP_MJ_CREATE union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT\_PARAMETERS for IRP\_MJ\_CREATE union


The following union component is used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_CREATE**](irp-mj-create.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PIO_SECURITY_CONTEXT     SecurityContext;
    ULONG                    Options;
    USHORT POINTER_ALIGNMENT FileAttributes;
    USHORT                   ShareAccess;
    USHORT POINTER_ALIGNMENT EaLength;
    PVOID                    EaBuffer;
    LARGE_INTEGER            AllocationSize;
  } Create;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**Create**  
Structure containing the following members.

**SecurityContext**  
SecurityContext-&gt;AccessState

Pointer to an [**ACCESS\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff538840) structure that contains the object's subject context, granted access types, and remaining desired access types.

SecurityContext-&gt;DesiredAccess

[**ACCESS\_MASK**](https://msdn.microsoft.com/library/windows/hardware/ff540466) structure that specifies access rights requested for the file. For more information, see the *DesiredAccess* parameter to [**FltCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff541935).

**Options**  
Bitmask of flags that specify the options to be applied when creating or opening the file, as well as the action to be taken if the file already exists. The low 24 bits of this member correspond to the *CreateOptions* parameter to [**FltCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff541935). The high 8 bits correspond to the *CreateDisposition* parameter to **FltCreateFile**.

**FileAttributes**  
Bitmask of attributes to be applied when creating or opening the file. For more information, see the *FileAttributes* parameter to [**FltCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff541935).

**ShareAccess**  
Bitmask of share access rights requested for the file. If this parameter is zero, exclusive access is being requested. For more information, see the *ShareAccess* parameter to [**FltCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff541935).

**EaLength**  
Length, in bytes, of the buffer that the **EaBuffer** member points to. For more information, see the *EaLength* parameter to [**FltCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff541935).

**EaBuffer**  
Pointer to a caller-supplied, [**FILE\_FULL\_EA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545793)-structured buffer that contains extended attribute (EA) information to be applied to the file. For more information, see the *EaBuffer* parameter to [**FltCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff541935).

**AllocationSize**  
Optionally specifies the initial allocation size, in bytes, for the file. A nonzero value has no effect unless the file is being created, overwritten, or superseded. For more information, see the *AllocationSize* parameter to [**FltCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff541935).

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for the [**IRP\_MJ\_CREATE**](irp-mj-create.md) operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure.

IRP\_MJ\_CREATE is an IRP-based operation.

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


[**ACCESS\_MASK**](https://msdn.microsoft.com/library/windows/hardware/ff540466)

[**ACCESS\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff538840)

[**FILE\_FULL\_EA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545793)

[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**FltCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff541935)

[**IRP\_MJ\_CREATE**](irp-mj-create.md)

 

 






