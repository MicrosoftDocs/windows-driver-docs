---
title: C30033
description: Warning C30033 Executable allocation was detected in a driver compiled with POOL\_NX\_OPTIN.
ms.assetid: A5212960-F33D-485A-9B80-23F3D95D475C
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
ExAllocatePoolWithTag(NonPagedPool, numberOfBytes, &#39;xppn&#39;);
```

The following code avoids this warning:

```
ExAllocatePoolWithTag(NonPagedPoolNx, numberOfBytes, &#39;xppn&#39;);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C30033%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




