---
title: C30031
description: Warning C30031 Calling a memory allocating function and passing a parameter that indicates executable memory.
ms.assetid: 5DBC7AC3-30CA-4BD4-BBCB-2275033FF505
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C30031%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




