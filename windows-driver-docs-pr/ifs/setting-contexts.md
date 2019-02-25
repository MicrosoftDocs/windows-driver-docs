---
title: Setting Contexts
description: Setting Contexts
ms.assetid: 3daa23e6-14d7-4d35-8bc8-695296cd289d
keywords:
- contexts WDK file system minifilter , setting
- attaching contexts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


After creating a new context, a minifilter driver can attach it to an object by calling **FltSet***Xxx***Context**, where *Xxx* is the context type.

If the *Operation* parameter of the **FltSet***Xxx***Context** routine is set to FLT\_SET\_CONTEXT\_KEEP\_IF\_EXISTS, **FltSet***Xxx***Context** attaches the newly allocated context to the object only if the minifilter driver has not already set a context for the object. If the minifilter driver has already set a context, **FltSet***Xxx***Context** returns STATUS\_FLT\_CONTEXT\_ALREADY\_DEFINED, which is an NTSTATUS error code, and does not replace the existing context. If the *OldContext* parameter of the **FltSet***Xxx***Context** routine is non-**NULL**, it receives a pointer to the existing context. When this pointer is no longer needed, the minifilter driver must release it by calling [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314).

If the *Operation* parameter is set to FLT\_SET\_CONTEXT\_REPLACE\_IF\_EXISTS, **FltSet***Xxx***Context** always attaches the new context to the object. If the minifilter driver has already set a context, **FltSet***Xxx***Context** deletes the existing context, sets the new context, and increments the reference count on the new context. If the *OldContext* parameter is non-**NULL**, it receives a pointer to the deleted context. When this pointer is no longer needed, the minifilter driver must release it by calling **FltReleaseContext**.

In the following code example, taken from the CTX sample minifilter driver, the **CtxInstanceSetup** routine creates and sets an instance context:

```cpp
status = FltAllocateContext(
           FltObjects->Filter,           //Filter
           FLT_INSTANCE_CONTEXT,         //ContextType
           CTX_INSTANCE_CONTEXT_SIZE,    //ContextSize
           NonPagedPool,                 //PoolType
           &instanceContext);            //ReturnedContext
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

 

 




