---
title: FILE\_LOCK structure
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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FILE_LOCK%20structure%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





