---
title: C28168
description: Warning C28168 The dispatch function does not have a _Dispatch_type_ annotation matching this dispatch table entry.
ms.assetid: 5e5acc54-acb3-4366-a625-eb79865e932e
ms.date: 04/20/2017
ms.localizationpriority: medium
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

```
The function 'DispatchPassIrp' does not have a _Dispatch_type_ annotation matching dispatch table position 'IRP_MJ_CREATE' (0x00):  This can be  corrected either by adding a _Dispatch_type_ annotation to the function declaration or correcting the dispatch table entry being used.
```

This use of a loop in the dispatch table is common in some filter drivers. In this situation, the error message can be ignored, as this is a limitation of static analysis. The Code Analysis tool reports this error when the annotations on the function do not match the dispatch table entry slot. In this case, the Code Analysis tool reports an illegal assignment (that’s undone later). However, there is no way for a static tool to know that an illegal state will be undone later. If you know you are making an assignments this way, and fixing them later, you can suppress the warning.

 

 





