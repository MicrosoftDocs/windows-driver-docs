---
title: Setting Contexts
description: Setting Contexts
ms.assetid: 3daa23e6-14d7-4d35-8bc8-695296cd289d
keywords: ["contexts WDK file system minifilter , setting", "attaching contexts"]
---

# Setting Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


After creating a new context, a minifilter driver can attach it to an object by calling **FltSet***Xxx***Context**, where *Xxx* is the context type.

If the *Operation* parameter of the **FltSet***Xxx***Context** routine is set to FLT\_SET\_CONTEXT\_KEEP\_IF\_EXISTS, **FltSet***Xxx***Context** attaches the newly allocated context to the object only if the minifilter driver has not already set a context for the object. If the minifilter driver has already set a context, **FltSet***Xxx***Context** returns STATUS\_FLT\_CONTEXT\_ALREADY\_DEFINED, which is an NTSTATUS error code, and does not replace the existing context. If the *OldContext* parameter of the **FltSet***Xxx***Context** routine is non-**NULL**, it receives a pointer to the existing context. When this pointer is no longer needed, the minifilter driver must release it by calling [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314).

If the *Operation* parameter is set to FLT\_SET\_CONTEXT\_REPLACE\_IF\_EXISTS, **FltSet***Xxx***Context** always attaches the new context to the object. If the minifilter driver has already set a context, **FltSet***Xxx***Context** deletes the existing context, sets the new context, and increments the reference count on the new context. If the *OldContext* parameter is non-**NULL**, it receives a pointer to the deleted context. When this pointer is no longer needed, the minifilter driver must release it by calling **FltReleaseContext**.

In the following code example, taken from the CTX sample minifilter driver, the **CtxInstanceSetup** routine creates and sets an instance context:

```
status = FltAllocateContext(
           FltObjects->Filter,           //Filter
           FLT_INSTANCE_CONTEXT,         //ContextType
           CTX_INSTANCE_CONTEXT_SIZE,    //ContextSize
           NonPagedPool,                 //PoolType
           &amp;instanceContext);            //ReturnedContext
...
status = FltSetInstanceContext(
           FltObjects->Instance,              //Instance
           FLT_SET_CONTEXT_KEEP_IF_EXISTS,    //Operation
           instanceContext,                   //NewContext
           NULL);                             //OldContext

if (instanceContext != NULL) {
  FltReleaseContext(instanceContext);
}
return status;
```

Note that after the call to [**FltSetInstanceContext**](https://msdn.microsoft.com/library/windows/hardware/ff544521), there is a call to **FltReleaseContext** to release the reference count that was set by [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710) (*not* **FltSetInstanceContext**). This is explained in [Releasing Contexts](releasing-contexts.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Setting%20Contexts%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




