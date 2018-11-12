---
title: C30031
description: Warning C30031 Calling a memory allocating function and passing a parameter that indicates executable memory.
ms.assetid: 5DBC7AC3-30CA-4BD4-BBCB-2275033FF505
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C30031


warning C30031: Calling a memory allocating function and passing a parameter that indicates executable memory

Code Analysis detected use of [POOL\_NX\_OPTIN](https://msdn.microsoft.com/library/windows/hardware/hh920402) and **ExInitializeDriverRuntime(*DrvRtPoolNxOptIn*)** was called before the entry function (for example, **DriverEntry()** or **DllInitialize()**). It is possible that the entry function indirectly calls **ExInitializeDriverRuntime(*DrvRtPoolNxOptIn*)**, in which case the error can be suppressed (see [Pragma Prefast to Suppress Warning Messages](https://msdn.microsoft.com/library/gg155764.aspx)).

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

 

 





