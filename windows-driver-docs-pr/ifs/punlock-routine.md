---
title: PUNLOCK\_ROUTINE function pointer
description: A filter (legacy filter or minifilter) can register a PUNLOCK\_ROUTINE-typed routine as the filter's UnlockRoutine callback routine for a FILE\_LOCK structure.
ms.assetid: e188bc88-e3dd-49d3-9c79-8eb408cd0338
keywords: ["PUNLOCK_ROUTINE function pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- UnlockRoutine
api_location:
- ntifs.h
api_type:
- UserDefined
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PUNLOCK\_ROUTINE function pointer


A filter (legacy filter or minifilter) can register a PUNLOCK\_ROUTINE-typed routine as the filter's *UnlockRoutine* callback routine for a FILE\_LOCK structure.

Syntax
------

```ManagedCPlusPlus
typedef VOID ( *UnlockRoutine)(
  _In_ PVOID           Context,
  _In_ PFILE_LOCK_INFO FileLockInfo
);
```

Parameters
----------

*Context* \[in\]  
Context pointer that was passed to [**FltProcessFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff543427) or [**FsRtlProcessFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff547166).

*FileLockInfo* \[in\]  
Opaque pointer to the FILE\_LOCK\_INFO structure for the byte-range lock.

Return value
------------

None

Remarks
-------

A filter (legacy filter or minifilter) can optionally specify a PUNLOCK\_ROUTINE-typed routine as the filter's *UnlockRoutine* callback for a byte-range file lock.

If the filter specifies a *UnlockRoutine* routine for a FILE\_LOCK structure, this routine is called when the lock is removed from a locked byte range in a file.

A minifilter specifies this routine by passing a pointer to the routine as the *UnlockRoutine* parameter for [**FltAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff541743).

A legacy filter specifies this routine by passing a pointer to the routine as the *UnlockRoutine* parameter for [**FsRtlAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff545640) or [**FsRtlInitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff546122).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or Fltkernel.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;= APC_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**FltAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff541743)

[**FltCheckLockForReadAccess**](https://msdn.microsoft.com/library/windows/hardware/ff541834)

[**FltCheckLockForWriteAccess**](https://msdn.microsoft.com/library/windows/hardware/ff541837)

[**FltFreeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff542969)

[**FltInitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff543273)

[**FltProcessFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff543427)

[**FltUninitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff544595)

[**FsRtlAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff545640)

[**FsRtlCheckLockForReadAccess**](https://msdn.microsoft.com/library/windows/hardware/ff545758)

[**FsRtlCheckLockForWriteAccess**](https://msdn.microsoft.com/library/windows/hardware/ff545760)

[**FsRtlFreeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff546011)

[**FsRtlInitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff546122)

[**FsRtlProcessFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff547166)

[**FsRtlUninitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff547313)

[**IRP\_MJ\_LOCK\_CONTROL**](irp-mj-lock-control.md)

[**PCOMPLETE\_LOCK\_IRP\_ROUTINE**](pcomplete-lock-irp-routine.md)

[**PFLT\_COMPLETE\_LOCK\_CALLBACK\_DATA\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff551073)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20PUNLOCK_ROUTINE%20function%20pointer%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





