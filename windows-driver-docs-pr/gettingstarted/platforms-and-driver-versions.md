---
title: Writing drivers for different versions of Windows
description: Writing drivers for different versions of Windows
ms.assetid: 7519235c-46c5-49aa-8b11-9e9ac5a51026
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing drivers for different versions of Windows


When you create a driver project, you specify the minimum target operating system, which is the minimum version of Windows that your driver will run on. For example, you could specify that Windows 7 is the minimum target operating system. In that case, your driver would run on Windows 7 and later versions of Windows.

**Note**  If you develop a driver for a particular minimum version of Windows and you want your driver to work on later versions of Windows, you must not use any undocumented functions, and you must not use documented functions in any way other than how it is described in the documentation. Otherwise your driver might fail to run on the later versions of Windows. Even if you have been careful to use only documented functions, you should test your driver on the new version of Windows each time one is released.



## <span id="Writing_a_multiversion_driver_using_only_common_features"></span><span id="writing_a_multiversion_driver_using_only_common_features"></span><span id="WRITING_A_MULTIVERSION_DRIVER_USING_ONLY_COMMON_FEATURES"></span>Writing a multiversion driver using only common features


When you design a driver that will run on multiple versions of Windows, the simplest approach is to allow the driver to use only DDI functions and structures that are common to all versions of Windows that the driver will run on. In this situation, you set the minimum target operating system to the earliest version of Windows that the driver will support.

For example, to support all versions of Windows, starting with Windows 7, you should:

1.  Design and implement the driver so that it uses only those features that are present in Windows 7.

2.  When you build your driver, specify Windows 7 as the minimum target operating system.

While this process is simple, it might restrict the driver to use only a subset of the functionality that is available on later versions of Windows.

## <span id="Writing_a_multiversion_driver_that_uses_version-dependent_features"></span><span id="writing_a_multiversion_driver_that_uses_version-dependent_features"></span><span id="WRITING_A_MULTIVERSION_DRIVER_THAT_USES_VERSION-DEPENDENT_FEATURES"></span>Writing a multiversion driver that uses version-dependent features


A kernel-mode driver can dynamically determine which version of Windows it is running on and choose to use features that are available in that version. For example, a driver that must support all versions of Windows, starting with Windows 7, can determine, at run time, the version of Windows that it is running on. If the driver is running on Windows 7, it must use only the DDI functions that Windows 7 supports. However, the same driver can use additional DDI functions that are unique to Windows 8, for example, when its run-time check determines that it is running on Windows 8.

### <span id="determining_the_windows_version"></span><span id="DETERMINING_THE_WINDOWS_VERSION"></span>Determining the Windows version

[**RtlIsNtDdiVersionAvailable**](https://msdn.microsoft.com/library/windows/hardware/ff561954) is a function that drivers can use to determine, at run time, if the features that are provided by a particular version of Windows are available. The prototype for this function is as follows:

```cpp
BOOLEAN RtlIsNtDdiVersionAvailable(IN ULONG Version)
```

In this prototype, *Version* is a value that indicates the required version of the Windows DDI. This value must be one of the DDI version constants, defined in sdkddkver.h, such as NTDDI\_WIN8 or NTDDI\_WIN7.

[**RtlIsNtDdiVersionAvailable**](https://msdn.microsoft.com/library/windows/hardware/ff561954) returns TRUE when the caller is running on a version of Windows that is the same as, or later than, the one that is specified by *Version.*

Your driver can also check for a specific service pack by calling the [**RtlIsServicePackVersionInstalled**](https://msdn.microsoft.com/library/windows/hardware/ff561956) function. The prototype for this function is as follows:

```cpp
BOOLEAN RtlIsServicePackVersionInstalled(IN ULONG Version)
```

In this prototype, *Version* is a value that indicates the required Windows version and service pack. This value must be one of the DDI version constants, defined in sdkddkver.h, such as NTDDI\_WS08SP3.

Note that [**RtlIsServicePackVersionInstalled**](https://msdn.microsoft.com/library/windows/hardware/ff561956) returns TRUE only when the operating system version exactly matches the specified version. Thus, a call to **RtlIsServicePackVersionInstalled** with *Version* set to NTDDI\_WS08SP3 will fail if the driver is not running on Windows Server 2008 with SP4.

### <span id="conditionally_calling_windows_version_dependent_functions"></span><span id="CONDITIONALLY_CALLING_WINDOWS_VERSION_DEPENDENT_FUNCTIONS"></span>Conditionally calling Windows version-dependent functions

After a driver determines that a specific operating system version is available on the computer, the driver can use the [**MmGetSystemRoutineAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554563) function to dynamically locate the routine and call it through a pointer. This function is available in Windows 7 and later operating system versions.

**Note**  To help preserve type checking and prevent unintentional errors, you should create a typedef that mirrors the original function type.



### <span id="example__determining_the_windows_version_and_conditionally_calling_a_v"></span><span id="EXAMPLE__DETERMINING_THE_WINDOWS_VERSION_AND_CONDITIONALLY_CALLING_A_V"></span>Example: Determining the Windows version and conditionally calling a version-dependent function

This code example, which is from a driver's header file, defines the PAISQSL type as a pointer to the [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) function. The example then declares a `AcquireInStackQueuedSpinLock` variable with this type.

```cpp
...
 //
// Pointer to the ordered spin lock function.
// This function is only available on Windows 7 and
// later systems
 typedef (* PAISQSL) (KeAcquireInStackQueuedSpinLock);
PAISQSL AcquireInStackQueued = NULL;
 ...
```

This code example, which is from the driver's initialization code, determines whether the driver is running on Windows 7 or a later operating system. If it is, the code retrieves a pointer to [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899).

```cpp
...

//
// Are we running on Windows 7 or later?
//
 if (RtlIsNtDdiVersionAvailable(NTDDI_WIN7) ) {

 //
  // Yes... Windows 7 or later it is!
  //
     RtlInitUnicodeString(&funcName,
                  L"KeAcquireInStackQueuedSpinLock");

 //
  // Get a pointer to Windows implementation
  // of KeAcquireInStackQueuedSpinLock into our
  // variable "AcquireInStackQueued"
     AcquireInStackQueued = (PAISQSL)
                  MmGetSystemRoutineAddress(&funcName);
 }

...
// Acquire a spin lock.

 if( NULL != AcquireInStackQueued) {
  (AcquireInStackQueued)(&SpinLock, &lockHandle);
} else {
    KeAcquireSpinLock(&SpinLock);
}
```

In the example the driver calls [**RtlIsNtDdiVersionAvailable**](https://msdn.microsoft.com/library/windows/hardware/ff561954) to determine whether the driver is running on Windows 7 or later. If the version is Windows 7 or later, the driver calls [**MmGetSystemRoutineAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554563) to get a pointer to the [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) function and stores this pointer in the variable named `AcquireInStackQueued` (which was declared as a PAISQSL type).

Later, when the driver must acquire a spin lock, it checks to see whether it has received a pointer to the [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) function. If the driver has received this pointer, the driver uses the pointer to call **KeAcquireInStackQueuedSpinLock**. If the pointer to **KeAcquireInStackQueuedSpinLock** is null, the driver uses [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) to acquire the spin lock.









