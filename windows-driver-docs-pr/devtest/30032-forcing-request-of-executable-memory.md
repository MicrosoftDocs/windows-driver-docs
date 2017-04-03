---
title: C30032
description: Warning C30032 Calling a memory allocating function and forcing the request of executable memory through use of the POOL\_NX\_OPTOUT directive.
ms.assetid: 7C6F9ACE-DD02-45A7-A601-C5C7A5C89256
---

# C30032


warning C30032: Calling a memory allocating function and forcing the request of executable memory through use of the [POOL\_NX\_OPTOUT](https://msdn.microsoft.com/library/windows/hardware/hh920401) directive

BANNED\_MEM\_ALLOCATION\_FORCE\_UNSAFE

The preprocessor directive [POOL\_NX\_OPTOUT](https://msdn.microsoft.com/library/windows/hardware/hh920401) prevents the auto-promotion of non-safe types (**MM\_PAGE\_PRIORITY** and **POOL\_TYPE**) to safe types (for example, NonPagedPool to NonPagedPoolNx). The use of POOL\_NX\_OPTOUT in your sources is likely by design. If this is by design and executable memory is required, then you can suppress the warning with [Pragma Prefast to Suppress Warning Messages](https://msdn.microsoft.com/library/gg155764.aspx). This type of allocation is not permitted on Windows 10 systems that have opted-in to additional memory protections.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code generates this warning:

In the sources file:

```
C_DEFINES=$(C_DEFINES) –DUNICODE -DPOOL_NX_OPTOUT=1
```

in the code file:

```
pPtr = MmGetSystemAddressForMdlSafe( pMdl, NormalPagePriority);
```

The following code avoids this warning:

In the sources file, add:

```
C_DEFINES=$(C_DEFINES) -DUNICODE -DPOOL_NX_OPTIN_AUTO=1
```

in the code file:

```
pPtr = MmGetSystemAddressForMdlSafe( pMdl, NormalPagePriority);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C30032%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




