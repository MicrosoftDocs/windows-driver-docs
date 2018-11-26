---
title: Registering FsFilter Callback Routines
description: Registering FsFilter Callback Routines
ms.assetid: d040e61c-514e-446b-9e72-934fd4322d3b
keywords:
- registering callback routines
- callback routines WDK file system
- FsFilter notification callback routines WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering FsFilter Callback Routines


## <span id="ddk_registering_fsfilter_callback_routines_if"></span><span id="DDK_REGISTERING_FSFILTER_CALLBACK_ROUTINES_IF"></span>


FsFilter notification callback routines are called before and after the underlying file system performs certain operations. For more information about FsFilter callback routines, see [**FsRtlRegisterFileSystemFilterCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff547172).

To register the FsFilter notification callback routines, you must allocate and initialize an FS\_FILTER\_CALLBACKS structure, store the entry points of the FsFilter callback routines in the structure, and pass the address of the structure in the *Callbacks* parameter to **FsRtlRegisterFileSystemFilterCallbacks**.

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

 

 




