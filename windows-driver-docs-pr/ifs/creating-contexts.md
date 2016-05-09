---
title: Creating Contexts
description: Creating Contexts
ms.assetid: da62d79d-064b-4ea4-abed-ffb13a9cc13d
keywords: ["contexts WDK file system minifilter , creating"]
---

# Creating Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


Once a minifilter driver has registered the context types that it uses, it can create a context by calling [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710). This routine selects the appropriate context definition to use according to the criteria described in [Registering Context Types](registering-context-types.md).

In the following code example, taken from the CTX sample minifilter driver, the **CtxInstanceSetup** routine calls [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710) to create an instance context:

```
status = FltAllocateContext(
 FltObjects->Filter,           //Filter
           FLT_INSTANCE_CONTEXT,         //ContextType
           CTX_INSTANCE_CONTEXT_SIZE,    //ContextSize
 NonPagedPool,                 //PoolType
           &amp;instanceContext);            //ReturnedContext
```

In the CTX sample, the following context definition is registered for instance contexts:

```
{ FLT_INSTANCE_CONTEXT,              //ContextType
  0,                                 //Flags
 CtxContextCleanup,                 //ContextCleanupCallback
  CTX_INSTANCE_CONTEXT_SIZE,         //Size
  CTX_INSTANCE_CONTEXT_TAG },        //PoolTag
```

This is a fixed-size context definition, because the **Size** member is a constant. (If the **Size** member were FLT\_VARIABLE\_SIZED\_CONTEXTS, it would be a variable-size context definition.) Note that the FLTFL\_CONTEXT\_REGISTRATION\_NO\_EXACT\_SIZE\_MATCH flag is not set in the **Flags** member. In this case, if the value of the *Size* parameter of [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710) matches that of the **Size** member of the context definition, **FltAllocateContext** allocates the instance context from the appropriate nonpaged lookaside list. If the values do not match, **FltAllocateContext** fails with a return value of STATUS\_FLT\_CONTEXT\_ALLOCATION\_NOT\_FOUND.

[**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710) initializes the reference count on the new context to one. When the context is no longer needed, the minifilter driver must release this reference. Thus, every call to **FltAllocateContext** must be matched by a subsequent call to [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Creating%20Contexts%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




