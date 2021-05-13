---
title: PUNLOCK\_ROUTINE function pointer
description: A filter (legacy filter or minifilter) can register a PUNLOCK\_ROUTINE-typed routine as the filter's UnlockRoutine callback routine for a FILE\_LOCK structure.
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

## Syntax

```ManagedCPlusPlus
typedef VOID ( *UnlockRoutine)(
  _In_ PVOID           Context,
  _In_ PFILE_LOCK_INFO FileLockInfo
);
```

## Parameters

*Context* \[in\]  
Context pointer that was passed to [**FltProcessFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltprocessfilelock) or [**FsRtlProcessFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlprocessfilelock).

*FileLockInfo* \[in\]  
Opaque pointer to the FILE\_LOCK\_INFO structure for the byte-range lock.

## Return value

None

## Remarks

A filter (legacy filter or minifilter) can optionally specify a PUNLOCK\_ROUTINE-typed routine as the filter's *UnlockRoutine* callback for a byte-range file lock.

If the filter specifies a *UnlockRoutine* routine for a FILE\_LOCK structure, this routine is called when the lock is removed from a locked byte range in a file.

A minifilter specifies this routine by passing a pointer to the routine as the *UnlockRoutine* parameter for [**FltAllocateFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatefilelock).

A legacy filter specifies this routine by passing a pointer to the routine as the *UnlockRoutine* parameter for [**FsRtlAllocateFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlallocatefilelock) or [**FsRtlInitializeFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlinitializefilelock).

## Requirements

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


[**FltAllocateFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatefilelock)

[**FltCheckLockForReadAccess**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltchecklockforreadaccess)

[**FltCheckLockForWriteAccess**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltchecklockforwriteaccess)

[**FltFreeFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreefilelock)

[**FltInitializeFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinitializefilelock)

[**FltProcessFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltprocessfilelock)

[**FltUninitializeFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltuninitializefilelock)

[**FsRtlAllocateFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlallocatefilelock)

[**FsRtlCheckLockForReadAccess**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlchecklockforreadaccess)

[**FsRtlCheckLockForWriteAccess**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlchecklockforwriteaccess)

[**FsRtlFreeFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlfreefilelock)

[**FsRtlInitializeFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlinitializefilelock)

[**FsRtlProcessFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlprocessfilelock)

[**FsRtlUninitializeFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtluninitializefilelock)

[**IRP\_MJ\_LOCK\_CONTROL**](irp-mj-lock-control.md)

[**PCOMPLETE\_LOCK\_IRP\_ROUTINE**](pcomplete-lock-irp-routine.md)

[**PFLT\_COMPLETE\_LOCK\_CALLBACK\_DATA\_ROUTINE**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_complete_lock_callback_data_routine)

 

