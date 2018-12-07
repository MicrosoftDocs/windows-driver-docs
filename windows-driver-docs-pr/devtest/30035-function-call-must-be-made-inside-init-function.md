---
title: C30035
description: Warning C30035 A call was made to a function that must be made from inside the initialization function (for example, DriverEntry() or DllInitialize()). PREfast was unable to determine if the call was made from the initialization function.
ms.assetid: 1A5F97EA-7DDC-4D3A-8058-B9C0C2211DA9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C30035


warning C30035: A call was made to a function that must be made from inside the initialization function (for example, **DriverEntry()** or **DllInitialize()**). PREfast was unable to determine if the call was made from the initialization function.

BANNED\_MEM\_ALLOCATION\_MAYBE\_BAD\_CALL\_SITE

The code was compiled with the [POOL\_NX\_OPTIN](https://msdn.microsoft.com/library/windows/hardware/hh920402) macro but the initialization did not occur inside of **DriverEntry()** or **DllInitialize()**. To fix this, move the call inside of the initialization function.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code generates this warning.

In the sources file:

```
C_DEFINES=$(C_DEFINES) -DPOOL_NX_OPTIN=1
```

```
NTSTATUS
DriverEntry (
    _In_ PDRIVER_OBJECT DriverObject,
    _In_ PUNICODE_STRING RegistryPath
    )
{
    NTSTATUS status;

    MakeSafeInitialization ();
…
}

void MakeSafeInitialization()
{
    ExInitializeDriverRuntime(DrvRtPoolNxOptIn);
}
```

The following code avoids this warning:

```
NTSTATUS
DriverEntry (
    _In_ PDRIVER_OBJECT DriverObject,
    _In_ PUNICODE_STRING RegistryPath
    )
{
    NTSTATUS status;

    ExInitializeDriverRuntime(DrvRtPoolNxOptIn);
…
}
```

 

 





