---
title: Writing drivers for different versions of Windows
description: Writing drivers for different versions of Windows
ms.date: 04/12/2022
---

# Writing drivers for different versions of Windows

When you create a driver project, you specify the minimum target operating system, which is the minimum version of Windows that your driver will run on. For example, you could specify that Windows 7 is the minimum target operating system. In that case, your driver would run on Windows 7 and later versions of Windows.

> [!NOTE]
> If you develop a driver for a particular minimum version of Windows and you want your driver to work on later versions of Windows, you must not use any undocumented functions, and you must not use documented functions in any way other than how it is described in the documentation. Otherwise your driver might fail to run on the later versions of Windows. Even if you have been careful to use only documented functions, you should test your driver on the new version of Windows each time one is released.

## Writing a multi-version driver using only common features

When you design a driver that will run on multiple versions of Windows, the simplest approach is to allow the driver to use only DDI functions and structures that are common to all versions of Windows that the driver will run on. In this situation, you set the minimum target operating system to the earliest version of Windows that the driver will support.

For example, to support all versions of Windows, starting with Windows 7, you should:

1. Design and implement the driver so that it uses only those features that are present in Windows 7.

1. When you build your driver, specify Windows 7 as the minimum target operating system.

While this process is simple, it might restrict the driver to use only a subset of the functionality that is available on later versions of Windows.  In many cases, you will want to make use of newer operating system functionality when it is available in order to improve security, improve reliability, or enable newer features.

## Writing a multi-version driver that uses version-dependent features

A kernel-mode driver can dynamically determine if an operating system provided API is available or which version of Windows the driver is running on and choose to use features that are available in that run time environment. For example, a driver that must support all versions of Windows, starting with Windows 7, can determine, at run time, the version of Windows that it is running on. If the driver is running on Windows 7, it must use only the DDI functions that Windows 7 supports. However, the same driver can use additional DDI functions that are unique to Windows 8, for example, when its run-time check determines that those APIs are currently present or determines that it is running on Windows 8.

> [!NOTE]
> It is recommended that you check for feature or API availability whenever possible instead of trying to check if your driver is running on a certain operating system version or later.

### Conditionally calling Windows version-dependent functions

A kernel-mode driver can use the [**MmGetSystemRoutineAddress**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemroutineaddress) or [**MmGetSystemRoutineAddressEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemroutineaddressex) functions to dynamically check if a particular API it wants to use is available in the current run time environment and to get a function pointer to use in order to call that API.

> [!NOTE]
> To help preserve type checking and prevent unintentional errors, you should create a typedef that mirrors the original function type.

#### Example: Determining API availability and conditionally calling API

```cpp
typedef
NTSTATUS
(*PFN_IoOpenDriverRegistryKey)(
    PDRIVER_OBJECT     DriverObject,
    DRIVER_REGKEY_TYPE RegKeyType,
    ACCESS_MASK        DesiredAccess,
    ULONG              Flags,
    PHANDLE            DriverRegKey
    );

VOID ExampleFunction(VOID) {
    NTSTATUS status = STATUS_UNSUCCESSFUL;
    HANDLE persistentStateKey = NULL;
    PFN_IoOpenDriverRegistryKey pfnIoOpenDriverRegistryKey = NULL;
    UNICODE_STRING functionName = {0};

    RtlInitUnicodeString(&functionName, L"IoOpenDriverRegistryKey");
    pfnIoOpenDriverRegistryKey = (PFN_IoOpenDriverRegistryKey)MmGetSystemRoutineAddress(&functionName);

    if (pfnIoOpenDriverRegistryKey != NULL) {
        // Open a key to where state can be stored under the driver service
        status = pfnIoOpenDriverRegistryKey(g_GlobalStructure.DriverObject,
                                            DriverRegKeyPersistentState,
                                            KEY_WRITE,
                                            0,
                                            &persistentStateKey);
    } else {
        // Fall back to opening up a different location to store state in
    }

    // Use the opened registry key
}
```

### Determining the Windows version

[**RtlIsNtDdiVersionAvailable**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlisntddiversionavailable) is a function that drivers can use at run time to determine if the features that are provided by a particular version of Windows are available. The prototype for this function is as follows:

```cpp
BOOLEAN RtlIsNtDdiVersionAvailable(IN ULONG Version)
```

In this prototype, *Version* is a value that indicates the required version of the Windows DDI. This value must be one of the DDI version constants, defined in sdkddkver.h, such as NTDDI_WIN8 or NTDDI_WIN7.

[**RtlIsNtDdiVersionAvailable**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlisntddiversionavailable) returns TRUE when the caller is running on a version of Windows that is the same as, or later than, the one that is specified by *Version*.

Your driver can also check for a specific service pack by calling the [**RtlIsServicePackVersionInstalled**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlisservicepackversioninstalled) function. The prototype for this function is as follows:

```cpp
BOOLEAN RtlIsServicePackVersionInstalled(IN ULONG Version)
```

In this prototype, *Version* is a value that indicates the required Windows version and service pack. This value must be one of the DDI version constants, defined in sdkddkver.h, such as NTDDI_WS08SP3.

Note that [**RtlIsServicePackVersionInstalled**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlisservicepackversioninstalled) returns TRUE only when the operating system version exactly matches the specified version. Thus, a call to **RtlIsServicePackVersionInstalled** with *Version* set to NTDDI_WS08SP3 will fail if the driver is not running on Windows Server 2008 with SP4.

### Example: Determining the Windows version and conditionally calling a version-dependent function

This code example, which is from a driver's header file, defines the PAISQSL type as a pointer to the [**KeAcquireInStackQueuedSpinLock**](/previous-versions/windows/hardware/drivers/ff551899(v=vs.85)) function. The example then declares a `AcquireInStackQueuedSpinLock` variable with this type.

```cpp
...
// Pointer to the ordered spin lock function. This function is only
// available on Windows 7 and later systems
typedef (* PAISQSL) (KeAcquireInStackQueuedSpinLock);
PAISQSL AcquireInStackQueued = NULL;
...
```

This code example, which is from the driver's initialization code, determines whether the driver is running on Windows 7 or a later operating system. If it is, the code retrieves a pointer to [**KeAcquireInStackQueuedSpinLock**](/previous-versions/windows/hardware/drivers/ff551899(v=vs.85)).

```cpp
...

// Are we running on Windows 7 or later?
if (RtlIsNtDdiVersionAvailable(NTDDI_WIN7)) {

    // Yes... Windows 7 or later it is!
    RtlInitUnicodeString(&funcName, L"KeAcquireInStackQueuedSpinLock");

    // Get a pointer to Windows implementation of KeAcquireInStackQueuedSpinLock
    // into our variable "AcquireInStackQueued"
    AcquireInStackQueued = (PAISQSL) MmGetSystemRoutineAddress(&funcName);
}

...

// Acquire a spin lock.
if (NULL != AcquireInStackQueued) {
    (AcquireInStackQueued)(&SpinLock, &lockHandle);
} else {
    KeAcquireSpinLock(&SpinLock);
}
```

In the example, the driver calls [**RtlIsNtDdiVersionAvailable**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlisntddiversionavailable) to determine whether the driver is running on Windows 7 or later. If the version is Windows 7 or later, the driver calls [**MmGetSystemRoutineAddress**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemroutineaddress) to get a pointer to the [**KeAcquireInStackQueuedSpinLock**](/previous-versions/windows/hardware/drivers/ff551899(v=vs.85)) function and stores this pointer in the variable named `AcquireInStackQueued` (which was declared as a PAISQSL type).

Later, when the driver must acquire a spin lock, it checks to see whether it has received a pointer to the [**KeAcquireInStackQueuedSpinLock**](/previous-versions/windows/hardware/drivers/ff551899(v=vs.85)) function. If the driver has received this pointer, the driver uses the pointer to call **KeAcquireInStackQueuedSpinLock**. If the pointer to **KeAcquireInStackQueuedSpinLock** is null, the driver uses [**KeAcquireSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlock) to acquire the spin lock.
