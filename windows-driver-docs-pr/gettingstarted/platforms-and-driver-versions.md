---
title: Writing Drivers for Different Versions of Windows
description: Writing drivers for different versions of Windows
ms.date: 03/15/2024
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

A kernel-mode driver can use the [**RtlVerifyVersionInfo**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlverifyversioninfo) function to dynamically check which version of Windows it is currently running on. 

> [!NOTE]
> It is recommended that you check for feature or API availability whenever possible instead of trying to check if your driver is running on a certain operating system version or later.

### Example: Determining the Windows version 

The following example detects if the currently running operating system version is greater than or equal to version 10.0 and detects if the build number is greater than or equal to build 22000 (Windows 11, version 21H2).

```cpp
...

NTSTATUS Status = STATUS_SUCCESS;
RTL_OSVERSIONINFOEXW VersionInfo = {0};
ULONG TypeMask = 0;
ULONGLONG ConditionMask = 0;

VersionInfo.dwOSVersionInfoSize = sizeof(VersionInfo);
VersionInfo.dwMajorVersion = 10;
VersionInfo.dwMinorVersion = 0;
VersionInfo.dwBuildNumber = 22000;

TypeMask = VER_MAJORVERSION | VER_MINORVERSION | VER_BUILDNUMBER;
VER_SET_CONDITION(ConditionMask, VER_MAJORVERSION, VER_GREATER_EQUAL);
VER_SET_CONDITION(ConditionMask, VER_MINORVERSION, VER_GREATER_EQUAL);
VER_SET_CONDITION(ConditionMask, VER_BUILDNUMBER, VER_GREATER_EQUAL);

Status = RtlVerifyVersionInfo(&VersionInfo,
                              TypeMask,
                              ConditionMask);

if (NT_SUCCESS(Status)) {

    //
    // The call to RtlVerifyVersionInfo succeeded, so the running OS
    // version and build number is greater than or equal to the value
    // specified. Do appropriate action for newer OS versions.
    //

} else if (Status == STATUS_REVISION_MISMATCH) {

    //
    // The running OS version is less than the value specified. Do
    // appropriate action for older OS versions.
    //

} else {

    //
    // There was an error comparing to the running OS version. Do
    // appropriate action for when the OS version is not known.
    //

}
...
```
