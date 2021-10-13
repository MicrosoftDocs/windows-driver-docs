---
title: PCOMPLETE\_LOCK\_IRP\_ROUTINE routine
description: A file system filter driver (legacy filter) can register a PCOMPLETE\_LOCK\_IRP\_ROUTINE-typed routine as the filter's CompleteLockIrpRoutine callback.
keywords: ["CompleteLockIrpRoutine routine Installable File System Drivers", "PCOMPLETE_LOCK_IRP_ROUTINE"]
topic_type:
- apiref
api_name:
- CompleteLockIrpRoutine
api_location:
- ntifs.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PCOMPLETE\_LOCK\_IRP\_ROUTINE routine


A file system filter driver (legacy filter) can register a PCOMPLETE\_LOCK\_IRP\_ROUTINE-typed routine as the filter's *CompleteLockIrpRoutine* callback.

## Syntax

```ManagedCPlusPlus
PCOMPLETE_LOCK_IRP_ROUTINE CompleteLockIrpRoutine;

NTSTATUS CompleteLockIrpRoutine(
  _In_ PVOID Context,
  _In_ PIRP  Irp
)
{ ... }
```

## Parameters

*Context* \[in\]  
Context pointer that was passed to [**FsRtlProcessFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlprocessfilelock).

*Irp* \[in\]  
IRP for the file lock [**IRP\_MJ\_LOCK\_CONTROL**](irp-mj-lock-control.md) request that is being completed. The lock request type will be one of the following:

IRP\_MN\_LOCK

IRP\_MN\_UNLOCK\_ALL

IRP\_MN\_UNLOCK\_ALL\_BY\_KEY

IRP\_MN\_UNLOCK\_SINGLE

## Return value

This routine returns STATUS\_SUCCESS or an appropriate NTSTATUS value. If it returns an NTSTATUS value that is not a success code, the file lock is removed from the file.

## Remarks

A file system filter driver (legacy filter) can optionally specify a PCOMPLETE\_LOCK\_IRP\_ROUTINE-typed routine as the legacy filter's *CompleteLockIrpRoutine* routine for a byte-range file lock.

To specify this routine, a legacy filter passes a pointer to the routine as the *CompleteLockIrpRoutine* parameter for [**FsRtlAllocateFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlallocatefilelock) or [**FsRtlInitializeFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlinitializefilelock).

If the legacy filter specifies a *CompleteLockIrpRoutine* routine for a file lock, the system calls this routine when completing an [**IRP\_MJ\_LOCK\_CONTROL**](irp-mj-lock-control.md) operation for the file lock.

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
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;= APC_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**FsRtlAllocateFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlallocatefilelock)

[**FsRtlCheckLockForReadAccess**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlchecklockforreadaccess)

[**FsRtlCheckLockForWriteAccess**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlchecklockforwriteaccess)

[**FsRtlFreeFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlfreefilelock)

[**FsRtlInitializeFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlinitializefilelock)

[**FsRtlProcessFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlprocessfilelock)

[**FsRtlUninitializeFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtluninitializefilelock)

[**IRP\_MJ\_LOCK\_CONTROL**](irp-mj-lock-control.md)

[**PUNLOCK\_ROUTINE**](punlock-routine.md)

 

