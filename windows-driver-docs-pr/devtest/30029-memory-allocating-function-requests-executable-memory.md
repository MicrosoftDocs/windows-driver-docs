---
title: C30029
description: Warning C30029 Calling a memory allocating function that requests executable memory.
ms.assetid: E32E6EDB-010A-4E7F-8505-1E7557BB3FDF
---

# C30029


warning C30029: Calling a memory allocating function that requests executable memory

BANNED\_MEM\_ALLOCATION\_NOTYPE

Some APIs allocate only executable nonpaged pool. There are no parameters you can supply that will change this behavior. The only way to fix this issue is to use an alternative API that allows for allocation of non-executable nonpaged pool memory.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code generates warning C30029:

```
MmMapIoSpace(  PhysicalAddress,
        numberOfBytes,
        PAGE_NOCACHE);
```

The following code avoids this warning:

```
MmMapIoSpaceEx(    PhysicalAddress,
        numberOfBytes,
        PAGE_NOCACHE | PAGE_READWRITE);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C30029%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




