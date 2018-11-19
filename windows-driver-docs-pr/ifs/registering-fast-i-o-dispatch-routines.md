---
title: Registering Fast I/O Dispatch Routines
description: Registering Fast I/O Dispatch Routines
ms.assetid: e559d3f2-be33-4a35-8931-4716e6082fc9
keywords:
- registering fast I/O dispatch routines
- dispatch routines WDK file system
- fast I/O dispatch routines WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Fast I/O Dispatch Routines


## <span id="ddk_registering_fast_io_dispatch_routines_if"></span><span id="DDK_REGISTERING_FAST_IO_DISPATCH_ROUTINES_IF"></span>


The *DriverObject* parameter of the filter driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine supplies a pointer to the filter driver's [**driver object**](https://msdn.microsoft.com/library/windows/hardware/ff544174).

To register the file system filter driver's fast I/O dispatch routines, you must allocate and initialize a fast I/O dispatch table, store the entry points of the fast I/O dispatch routines into the table, and store the address of the table in the **FastIoDispatch** member of the driver object.

For example, a hypothetical "MyLegacyFilter" driver can set the entry points for its fast I/O dispatch routines as follows:

```cpp
RtlZeroMemory(fastIoDispatch, sizeof(FAST_IO_DISPATCH));
fastIoDispatch->SizeOfFastIoDispatch = sizeof(FAST_IO_DISPATCH);
fastIoDispatch->FastIoCheckIfPossible = MyLegacyFilterIoCheckIfPossible;
fastIoDispatch->FastIoRead = MyLegacyFilterIoRead;
fastIoDispatch->FastIoWrite = MyLegacyFilterIoWrite;
fastIoDispatch->FastIoQueryBasicInfo = MyLegacyFilterIoQueryBasicInfo;
fastIoDispatch->FastIoQueryStandardInfo = MyLegacyFilterIoQueryStandardInfo;
fastIoDispatch->FastIoLock = MyLegacyFilterIoLock;
fastIoDispatch->FastIoUnlockSingle = MyLegacyFilterIoUnlockSingle;
fastIoDispatch->FastIoUnlockAll = MyLegacyFilterIoUnlockAll;
fastIoDispatch->FastIoUnlockAllByKey = MyLegacyFilterIoUnlockAllByKey;
fastIoDispatch->FastIoDeviceControl = MyLegacyFilterIoDeviceControl;
fastIoDispatch->FastIoDetachDevice = MyLegacyFilterIoDetachDevice;
fastIoDispatch->FastIoQueryNetworkOpenInfo = MyLegacyFilterIoQueryNetworkOpenInfo;
fastIoDispatch->MdlRead = MyLegacyFilterIoMdlRead;
fastIoDispatch->MdlReadComplete = MyLegacyFilterIoMdlReadComplete;
fastIoDispatch->PrepareMdlWrite = MyLegacyFilterIoPrepareMdlWrite;
fastIoDispatch->MdlWriteComplete = MyLegacyFilterIoMdlWriteComplete;
fastIoDispatch->FastIoReadCompressed = MyLegacyFilterIoReadCompressed;
fastIoDispatch->FastIoWriteCompressed = MyLegacyFilterIoWriteCompressed;
fastIoDispatch->MdlReadCompleteCompressed = MyLegacyFilterIoMdlReadCompleteCompressed;
fastIoDispatch->MdlWriteCompleteCompressed = MyLegacyFilterIoMdlWriteCompleteCompressed;
fastIoDispatch->FastIoQueryOpen = MyLegacyFilterIoQueryOpen;

DriverObject->FastIoDispatch = fastIoDispatch;
```

 

 




