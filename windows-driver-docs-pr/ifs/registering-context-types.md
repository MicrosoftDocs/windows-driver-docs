---
title: Registering Context Types
description: Registering Context Types
ms.assetid: ddf03426-5c49-4621-b81d-59d1cb002ae9
keywords:
- contexts WDK file system minifilter , registering types
- registering context types
- FLT_CONTEXT_REGISTRATION
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Context Types


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


When a minifilter driver calls [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305) from its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, it must register each type of context that it uses.

To register context types, the minifilter driver creates a variable-length array of [**FLT\_CONTEXT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544629) structures and stores a pointer to the array in the **ContextRegistration** member of the [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure that the minifilter driver passes in the *Registration* parameter of [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305). The order of the elements in this array does not matter. However, the last element in the array must be {FLT\_CONTEXT\_END}.

For each context type that the minifilter driver uses, it must supply at least one context definition in the form of an FLT\_CONTEXT\_REGISTRATION structure. Each FLT\_CONTEXT\_REGISTRATION structure defines the type, size, and other information for the context.

When the minifilter driver creates a new context by calling [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710), the filter manager uses the *Size* parameter of the **FltAllocateContext** routine, as well as the **Size** and **Flags** members of the FLT\_CONTEXT\_REGISTRATION structure, to select the context definition to be used.

For fixed-size contexts, the **Size** member of the FLT\_CONTEXT\_REGISTRATION structure specifies the size, in bytes, of the portion of the context structure that is defined by the minifilter driver. The maximum size for a context is MAXUSHORT (64 KB). Zero is a valid size value. The filter manager implements fixed-size contexts using lookaside lists. The filter manager creates two lookaside lists for each size value: one paged and one nonpaged.

For variable-size contexts, the **Size** member must be set to FLT\_VARIABLE\_SIZED\_CONTEXTS. The filter manager allocates variable-size contexts directly from paged or nonpaged pool.

In the **Flags** member of the FLT\_CONTEXT\_REGISTRATION structure, the FLTFL\_CONTEXT\_REGISTRATION\_NO\_EXACT\_SIZE\_MATCH flag can be specified. If the minifilter driver uses fixed-size contexts and this flag is specified, the filter manager allocates a context from the lookaside list if the context's size is greater than or equal to the requested size. Otherwise, the context's size must be equal to the requested size.

For a given context type, the minifilter driver can supply up to three fixed-size context definitions, each with a different size, and one variable-size definition. For more information, see [**FLT\_CONTEXT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544629).

The minifilter driver can optionally supply a context cleanup callback routine to be called before the context is freed. For more information, see [**PFLT\_CONTEXT\_CLEANUP\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551078).

A minifilter driver can optionally define its own callback routines for allocating and freeing contexts, instead of relying on the filter manager to perform these tasks. However, this is very rarely necessary. For more information, see [**PFLT\_CONTEXT\_ALLOCATE\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551075) and [**PFLT\_CONTEXT\_FREE\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551082).

The following code example, which is taken from the CTX sample minifilter driver, shows an array of FLT\_CONTEXT\_REGISTRATION structures that are used to register instance, file, stream, and file object (stream handle) contexts.

```cpp
const FLT_CONTEXT_REGISTRATION contextRegistration[] =
{
    { FLT_INSTANCE_CONTEXT,              //ContextType
      0,                                 //Flags
      CtxContextCleanup,                 //ContextCleanupCallback
      CTX_INSTANCE_CONTEXT_SIZE,         //Size
      CTX_INSTANCE_CONTEXT_TAG           //PoolTag
    },
    { FLT_FILE_CONTEXT,                  //ContextType
      0,                                 //Flags
      CtxContextCleanup,                 //ContextCleanupCallback
      CTX_FILE_CONTEXT_SIZE,             //Size
      CTX_FILE_CONTEXT_TAG               //PoolTag
    },
    { FLT_STREAM_CONTEXT,                //ContextType
      0,                                 //Flags
      CtxContextCleanup,                 //ContextCleanupCallback
      CTX_STREAM_CONTEXT_SIZE,           //Size
      CTX_STREAM_CONTEXT_TAG             //PoolTag
    },
    { FLT_STREAMHANDLE_CONTEXT,          //ContextType
      0,                                 //Flags
      CtxContextCleanup,                 //ContextCleanupCallback
      CTX_STREAMHANDLE_CONTEXT_SIZE,     //Size
      CTX_STREAMHANDLE_CONTEXT_TAG       //PoolTag
    },
    { FLT_CONTEXT_END }
};
```

 

 




