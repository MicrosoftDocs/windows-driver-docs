---
title: FLT\_PARAMETERS for IRP\_MJ\_LOCK\_CONTROL union
description: The following union component is used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_LOCK\_CONTROL.
ms.assetid: 4dbdb4c8-5908-40e5-b600-225b47118c6d
keywords: ["FLT_PARAMETERS for IRP_MJ_LOCK_CONTROL union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FLT\_PARAMETERS for IRP\_MJ\_LOCK\_CONTROL union


The following union component is used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_LOCK\_CONTROL**](irp-mj-lock-control.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PLARGE_INTEGER          Length;
    ULONG POINTER_ALIGNMENT Key;
    LARGE_INTEGER           ByteOffset;
    PEPROCESS               ProcessId;
    BOOLEAN                 FailImmediately;
    BOOLEAN                 ExclusiveLock;
  } LockControl;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**LockControl**  
Structure containing the following members.

**Length**  
Pointer to a variable that specifies the length in bytes of the range to be locked.

**Key**  
Key value to be assigned to the byte-range lock.

**ByteOffset**  
Starting byte offset within the file of the range to be locked.

**ProcessId**  
Opaque pointer to the process ID for the process that requested the byte-range lock.

**FailImmediately**  
Boolean value specifying whether the lock request should fail if the lock cannot be granted immediately. This member is set to **FALSE** if the requesting thread can be put into a wait state until the request is granted or **TRUE** if it cannot.

**ExclusiveLock**  
Boolean value specifying whether an exclusive lock is requested. This member is set to **TRUE** if an exclusive lock is requested or **FALSE** if a shared lock is requested.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for the [**IRP\_MJ\_LOCK\_CONTROL**](irp-mj-lock-control.md) operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure.

IRP\_MJ\_LOCK\_CONTROL can be an IRP-based I/O operation or a fast I/O operation.

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

[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**FltAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff541743)

[**FltCheckLockForReadAccess**](https://msdn.microsoft.com/library/windows/hardware/ff541834)

[**FltCheckLockForWriteAccess**](https://msdn.microsoft.com/library/windows/hardware/ff541837)

[**FltFreeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff542969)

[**FltInitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff543273)

[**FltProcessFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff543427)

[**FltUninitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff544595)

[**IRP\_MJ\_LOCK\_CONTROL**](irp-mj-lock-control.md)

[**PFLT\_COMPLETE\_LOCK\_CALLBACK\_DATA\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff551073)

[**PUNLOCK\_ROUTINE**](punlock-routine.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_LOCK_CONTROL%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





