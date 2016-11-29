---
title: C28168
description: Warning C28168 The dispatch function does not have a \_Dispatch\_type\_ annotation matching this dispatch table entry.
ms.assetid: 5e5acc54-acb3-4366-a625-eb79865e932e
---

# C28168


warning C28168: The dispatch function does not have a **\_Dispatch\_type\_** annotation matching this dispatch table entry

This warning supports [Static Driver Verifier](static-driver-verifier.md) by checking that each function assigned into the dispatch table is annotated with one or more **\_Dispatch\_type\_** annotations that indicate the kinds of dispatch operations performed by that function. The Code Analysis tool reports this error when the annotations on the function do not match the dispatch table entry slot.

This defect can be corrected either by adding a **\_Dispatch\_type\_** annotation to the function or correcting the dispatch table entry being used.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example generates this warning.

```
DRIVER_DISPATCH SampleCreate;
...
pDo->MajorFunction[IRP_MJ_CREATE] = SampleCreate;
...
```

The following code example avoids this warning.

```
_Dispatch_type_(IRP_MJ_CREATE) DRIVER_DISPATCH SampleCreate;
...
pDo->MajorFunction[IRP_MJ_CREATE] = SampleCreate;
...
```

## <span id="Comments"></span><span id="comments"></span><span id="COMMENTS"></span>Comments


In some circumstances, you might need to suppress this warning. There are some drivers, for example, filter drivers, that might register dispatch routines inside a loop, after they have registered others directly.

```ManagedCPlusPlus
DriverObject->MajorFunction[IRP_MJ_CREATE]         = DispatchCreate;
DriverObject->MajorFunction[IRP_MJ_READ]           = DispatchRead;
for (Index = 0; Index <= IRP_MJ_MAXIMUM_FUNCTION; Index++)
    {
            DriverObject->MajorFunction[Index] = DispatchPassIrp;
    }
```

In this example, the **DispatchPassIrp** function is correctly declared with the following annotations:

```ManagedCPlusPlus
__drv_dispatchType(IRP_MJ_CREATE_NAMED_PIPE)
__drv_dispatchType(IRP_MJ_QUERY_INFORMATION)
// .... 
//  (additional dispatch type annotations) 
// ....
__drv_dispatchType(IRP_MJ_CREATE_NAMED_PIPE)
    DRIVER_DISPATCH DispatchPassIrp;
```

In this situation, the Code Analysis tool reports this error:

``` syntax
The function 'DispatchPassIrp' does not have a _Dispatch_type_ annotation matching dispatch table position 'IRP_MJ_CREATE' (0x00):  This can be  corrected either by adding a _Dispatch_type_ annotation to the function declaration or correcting the dispatch table entry being used.
```

This use of a loop in the dispatch table is common in some filter drivers. In this situation, the error message can be ignored, as this is a limitation of static analysis. The Code Analysis tool reports this error when the annotations on the function do not match the dispatch table entry slot. In this case, the Code Analysis tool reports an illegal assignment (that’s undone later). However, there is no way for a static tool to know that an illegal state will be undone later. If you know you are making an assignments this way, and fixing them later, you can suppress the warning.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28168%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




