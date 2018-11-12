---
title: C30033
description: Warning C30033 Executable allocation was detected in a driver compiled with POOL_NX_OPTIN.
ms.assetid: A5212960-F33D-485A-9B80-23F3D95D475C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C30033


warning C30033: Executable allocation was detected in a driver compiled with [POOL\_NX\_OPTIN](https://msdn.microsoft.com/library/windows/hardware/hh920402). This driver has been determined to be loaded at run time by another driver. Please verify that the loading driver calls **ExInitializeDriverRuntime(*DrvRtPoolNxOptIn*)** in its DriverEntry.

BANNED\_MEM\_ALLOCATION\_MAYBE\_UNSAFE\_DRIVER\_LOADED

It has been determined that this is a DLL that is loaded by another driver, and as such does not have a complete initialization function. Verify the loading driver is:

-   Compiled using [POOL\_NX\_OPTIN](https://msdn.microsoft.com/library/windows/hardware/hh920402)=1
-   Calls **ExInitializeDriverRuntime(*DrvRtPoolNxOptIn*)** in its initialization function

If the loading driver specifies these correctly, then the warning can be ignored.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code in every loader of the DLL means that you should make the change (as per the safe example below)

In the sources file

```
C_DEFINES=$(C_DEFINES)
```

In **DriverEntry**, before any memory allocation takes place:

```
NTSTATUS
DriverEntry (
    _In_ PDRIVER_OBJECT DriverObject,
    _In_ PUNICODE_STRING RegistryPath
    )
{
    NTSTATUS status;
…
    // No call to ExInitializeDriverRuntime
    return(status)
}
```

The following code in every loader of the DLL means that you can ignore the warning.

In the sources file, add

```
C_DEFINES=$(C_DEFINES) -DPOOL_NX_OPTIN=1
```

In **DriverEntry**, before any memory allocation takes place:

```
NTSTATUS
DriverEntry (
    _In_ PDRIVER_OBJECT DriverObject,
    _In_ PUNICODE_STRING RegistryPath
    )
{
    NTSTATUS status;

    ExInitializeDriverRuntime( DrvRtPoolNxOptIn );
…
```

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


A second way to fix this is to make every call explicitly reference non-executable memory.

The following code generates this warning.

```
ExAllocatePoolWithTag(NonPagedPool, numberOfBytes, 'xppn');
```

The following code avoids this warning:

```
ExAllocatePoolWithTag(NonPagedPoolNx, numberOfBytes, 'xppn');
```

 

 





