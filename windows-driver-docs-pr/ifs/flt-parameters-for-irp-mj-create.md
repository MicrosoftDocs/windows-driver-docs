---
title: FLT\_PARAMETERS for IRP\_MJ\_CREATE union
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_CREATE%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





