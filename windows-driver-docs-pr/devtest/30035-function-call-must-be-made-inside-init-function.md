---
title: C30035 warning
description: Warning C30035 A call was made to a function that must be made from inside the initialization function (for example, DriverEntry() or DllInitialize()). PREfast was unable to determine if the call was made from the initialization function.
ms.date: 04/20/2017
f1_keywords: 
  - "C30035"
---

# C30035


warning C30035: A call was made to a function that must be made from inside the initialization function (for example, **DriverEntry()** or **DllInitialize()**). PREfast was unable to determine if the call was made from the initialization function.

BANNED\_MEM\_ALLOCATION\_MAYBE\_BAD\_CALL\_SITE

The code was compiled with the [POOL\_NX\_OPTIN](../kernel/single-binary-opt-in-pool-nx-optin.md) macro but the initialization did not occur inside of **DriverEntry()** or **DllInitialize()**. To fix this, move the call inside of the initialization function.

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

 

