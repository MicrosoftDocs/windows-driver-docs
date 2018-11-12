---
title: FILE_LOCK structure
description: The operating system uses the opaque FILE\_LOCK structure to support the locking of files.
ms.assetid: 89df2075-c542-4105-847f-9bc7ae4dab50
keywords: ["FILE_LOCK structure Installable File System Drivers", "PFILE_LOCK structure pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FILE_LOCK
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FILE\_LOCK structure


The operating system uses the opaque FILE\_LOCK structure to support the locking of files.

Syntax
------

```ManagedCPlusPlus
typedef struct _FILE_LOCK {
  PCOMPLETE_LOCK_IRP_ROUTINE CompleteLockIrpRoutine;
  PUNLOCK_ROUTINE            UnlockRoutine;
  BOOLEAN                    FastIoIsQuestionable;
  BOOLEAN                    SpareC[3];
  PVOID                      LockInformation;
  FILE_LOCK_INFO             LastReturnedLockInfo;
  PVOID                      LastReturnedLock;
  volatile LONG              LockRequestsInProgress;
} FILE_LOCK, *PFILE_LOCK;
```

Members
-------

**CompleteLockIrpRoutine**  
Reserved for system use.

**UnlockRoutine**  
Reserved for system use.

**FastIoIsQuestionable**  
Reserved for system use.

**SpareC**  
Reserved for system use.

**LockInformation**  
Reserved for system use.

**LastReturnedLockInfo**  
Reserved for system use.

**LastReturnedLock**  
Reserved for system use.

**LockRequestsInProgress**  
Reserved for system use.

Remarks
-------

File system legacy filter drivers and minifilters can use a variety of routines to create and use FILE\_LOCK objects, as well as to test for read/write access to files.

-   To allocate a FILE\_LOCK object, call [**FsRtlAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff545640) or [**FltAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff541743).

-   To initialize an uninitialized FILE\_LOCK object, call [**FsRtlInitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff546122) or [**FltInitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff543273). Be aware that a FILE\_LOCK returned from [**FsRtlAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff545640) or [**FltAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff541743) is already initialized.

-   To uninitialize a FILE\_LOCK object, call [**FsRtlUninitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff547313) or [**FltUninitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff544595).

-   To free a FILE\_LOCK object that is allocated by the [**FsRtlAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff545640) routine, call [**FsRtlFreeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff546011). To free a FILE\_LOCK object that is allocated by the [**FltAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff541743) routine, call [**FltFreeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff542969).

After a FILE\_LOCK has been initialized, routines such as [**FsRtlCheckLockForReadAccess**](https://msdn.microsoft.com/library/windows/hardware/ff545758), [**FltCheckLockForWriteAccess**](https://msdn.microsoft.com/library/windows/hardware/ff541837), and [**FsRtlFastCheckLockForRead**](https://msdn.microsoft.com/library/windows/hardware/ff545918) can be used to determine if the file can be accessed by other threads.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Microsoft Windows 2000, and later versions of the Windows operating system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include FltKernel.h or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[**FltAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff541743)

[**FltCheckLockForReadAccess**](https://msdn.microsoft.com/library/windows/hardware/ff541834)

[**FltCheckLockForWriteAccess**](https://msdn.microsoft.com/library/windows/hardware/ff541837)

[**FltInitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff543273)

**FltInitializeFileLock**
[**FsRtlAllocateFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff545640)

[**FsRtlCheckLockForReadAccess**](https://msdn.microsoft.com/library/windows/hardware/ff545758)

[**FsRtlCheckLockForWriteAccess**](https://msdn.microsoft.com/library/windows/hardware/ff545760)

[**FsRtlFastCheckLockForRead**](https://msdn.microsoft.com/library/windows/hardware/ff545918)

[**FsRtlFastCheckLockForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff545928)

[**FsRtlInitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff546122)

[**FsRtlUninitializeFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff547313)

 

 






