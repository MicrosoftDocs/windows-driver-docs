---
title: C30035
description: Warning C30035 A call was made to a function that must be made from inside the initialization function (for example, DriverEntry() or DllInitialize()). PREfast was unable to determine if the call was made from the initialization function.
ms.assetid: 1A5F97EA-7DDC-4D3A-8058-B9C0C2211DA9
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C30035%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




