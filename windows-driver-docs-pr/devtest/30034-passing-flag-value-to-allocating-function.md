---
title: C30034
description: Warning C30034 Passing a flag value to an allocating function that could result in executable memory being allocated. Please verify that the allocating function is not requesting a form of executable nonpaged pool.
ms.assetid: 11B06B23-17B4-4B97-A1EE-3351B72B7B1D
---

# C30034


warning C30034: Passing a flag value to an allocating function that could result in executable memory being allocated. Please verify that the allocating function is not requesting a form of executable nonpaged pool.

BANNED\_MEM\_ALLOCATION\_MAYBE\_UNSAFE

A call to a function that results in possible allocation of executable nonpaged pool has been found. There are parameters used that indicate the resulting allocation may actually be non-executable, but it is determined that this is unlikely and executable memory has been allocated. This is most common with a function that takes optional allocating functions as a parameter.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code generates this warning because it is not known if *pAllocate* allocates the specified type - in this the fourth parameter (0, which is executable) or if the allocation type is set from within *pAllocate.*

```
ExInitializeNPagedLookasideList(   pLookaside,
                pAllocate,
                pFree,
                0,
                size,
                tag,
                depth);
```

The following code avoids this warning:

```
ExInitializeNPagedLookasideList(   pLookaside,
                pAllocate,
                pFree,
                POOL_NX_ALLOCATION,
                size,
                tag,
                depth);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C30034%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




