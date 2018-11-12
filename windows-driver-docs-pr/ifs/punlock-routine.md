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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 






