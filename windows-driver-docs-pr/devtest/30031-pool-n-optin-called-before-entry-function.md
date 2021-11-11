---
title: C30031 warning
description: Warning C30031 Calling a memory allocating function and passing a parameter that indicates executable memory.
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C30031"
---

# C30031


warning C30031: Calling a memory allocating function and passing a parameter that indicates executable memory

Code Analysis detected use of [POOL\_NX\_OPTIN](../kernel/single-binary-opt-in-pool-nx-optin.md) and **ExInitializeDriverRuntime(*DrvRtPoolNxOptIn*)** was called before the entry function (for example, **DriverEntry()** or **DllInitialize()**). It is possible that the entry function indirectly calls **ExInitializeDriverRuntime(*DrvRtPoolNxOptIn*)**, in which case the error can be suppressed (see [Pragma Prefast to Suppress Warning Messages](/previous-versions/windows/embedded/gg155764(v=winembedded.70))).

BANNED\_MEM\_ALLOCATION\_MAYBE\_SAFE

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code in the sources file generates this warning:

```
C_DEFINES=$(C_DEFINES) -DPOOL_NX_OPTIN=1
```

In the code file

```
void MakeSafeInitialization()
{
    ExInitializeDriverRuntime(DrvRtPoolNxOptIn);
}

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

 

