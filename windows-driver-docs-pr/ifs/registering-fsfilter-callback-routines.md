---
title: Registering FsFilter Callback Routines
description: Registering FsFilter Callback Routines
keywords:
- registering callback routines
- callback routines WDK file system
- FsFilter notification callback routines WDK file system
ms.date: 02/23/2023
---

# Registering FsFilter Callback Routines

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

FsFilter notification callback routines are called before and after the underlying file system performs certain operations. For more information about FsFilter callback routines, see [**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks).

To register the FsFilter notification callback routines, you must allocate and initialize an FS_FILTER_CALLBACKS structure, store the entry points of the FsFilter callback routines in the structure, and pass the address of the structure in the *Callbacks* parameter to **FsRtlRegisterFileSystemFilterCallbacks**.

For example, a hypothetical "MyLegacyFilter" driver can register its FsFilter callback routines as follows:

```cpp
fsFilterCallbacks.SizeOfFsFilterCallbacks = sizeof(FS_FILTER_CALLBACKS);
fsFilterCallbacks.PreAcquireForSectionSynchronization = MyLegacyFilterPreFsFilterOperation;
fsFilterCallbacks.PostAcquireForSectionSynchronization = MyLegacyFilterPostFsFilterOperation;
fsFilterCallbacks.PreReleaseForSectionSynchronization = MyLegacyFilterPreFsFilterOperation;
fsFilterCallbacks.PostReleaseForSectionSynchronization = MyLegacyFilterPostFsFilterOperation;
fsFilterCallbacks.PreAcquireForCcFlush = MyLegacyFilterPreFsFilterOperation;
fsFilterCallbacks.PostAcquireForCcFlush = MyLegacyFilterPostFsFilterOperation;
fsFilterCallbacks.PreReleaseForCcFlush = MyLegacyFilterPreFsFilterOperation;
fsFilterCallbacks.PostReleaseForCcFlush = MyLegacyFilterPostFsFilterOperation;
fsFilterCallbacks.PreAcquireForModifiedPageWriter = MyLegacyFilterPreFsFilterOperation;
fsFilterCallbacks.PostAcquireForModifiedPageWriter = MyLegacyFilterPostFsFilterOperation;
fsFilterCallbacks.PreReleaseForModifiedPageWriter = MyLegacyFilterPreFsFilterOperation;
fsFilterCallbacks.PostReleaseForModifiedPageWriter = MyLegacyFilterPostFsFilterOperation;

status = FsRtlRegisterFileSystemFilterCallbacks(DriverObject, &fsFilterCallbacks);
```

 

