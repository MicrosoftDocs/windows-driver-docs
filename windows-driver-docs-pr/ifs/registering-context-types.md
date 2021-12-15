---
title: Registering context types
description: Registering Context Types
keywords:
- contexts WDK file system minifilter , registering types
- registering context types
- FLT_CONTEXT_REGISTRATION
ms.date: 10/25/2021
---

# Registering context types

A minifilter driver must first register each type of context that it uses. Once a minifilter has registered the context types that it uses, it can [create a context](creating-contexts.md).

## Steps to register a context type

A minifilter calls [**FltRegisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltregisterfilter) from its [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine to register each type of context that it uses. Before calling **FltRegisterFilter**, the minifilter driver does the following:

- Creates a variable-length array of [**FLT_CONTEXT_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_context_registration) structures. The order of elements in this array does not matter; however, the last element in the array must be {FLT_CONTEXT_END}.
- Stores a pointer to the created array in the **ContextRegistration** member of the [**FLT_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration) structure. The minifilter passes this structure in the *Registration* parameter of [**FltRegisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltregisterfilter).

For each context type that the minifilter driver uses, it must supply at least one context definition. The definition is in the form of a [**FLT_CONTEXT_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_context_registration) structure, where each structure defines the type, size, and other information for the context.

When the minifilter driver calls [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext) to create a new context, the filter manager uses the **Size** parameter, as well as the **Size** and **Flags** members of the FLT_CONTEXT_REGISTRATION structure, to select the context definition to be used:

- For fixed-size contexts, the **Size** member of the FLT_CONTEXT_REGISTRATION structure specifies the size, in bytes, of the portion of the context structure that is defined by the minifilter driver. The maximum size for a context is MAXUSHORT (64 KB). Zero is a valid size value. The filter manager implements fixed-size contexts using lookaside lists. The filter manager creates two lookaside lists for each size value: one paged and one nonpaged.

- For variable-size contexts, the **Size** member must be set to FLT_VARIABLE_SIZED_CONTEXTS. The filter manager allocates variable-size contexts directly from paged or nonpaged pool.

In the **Flags** member of the FLT_CONTEXT_REGISTRATION structure, the FLTFL_CONTEXT_REGISTRATION_NO_EXACT_SIZE_MATCH flag can be specified. If the minifilter driver uses fixed-size contexts and this flag is specified, the filter manager allocates a context from the lookaside list if the context's size is greater than or equal to the requested size. Otherwise, the context's size must be equal to the requested size.

For a given context type, the minifilter driver can supply up to three fixed-size context definitions, each with a different size, and one variable-size definition. For more information, see [**FLT_CONTEXT_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_context_registration).

## Minifilter callback routines for context management

The minifilter driver can optionally supply the following context-related callback routines, which are stored in the [**FLT_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration) structure that is passed as a parameter to [**FltRegisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltregisterfilter):

| Callback routine | Description |
| ---------------- | ----------- |
| [**PFLT_CONTEXT_ALLOCATE_CALLBACK**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_context_allocate_callback) | On very rare occasion, a minifilter might need to define its own callback routine to allocate contexts, rather than rely on the filter manager. |
|  [**PFLT_CONTEXT_CLEANUP_CALLBACK**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_context_cleanup_callback) | A minifilter's cleanup routine to be called before the context is freed. |
| [**PFLT_CONTEXT_FREE_CALLBACK**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_context_free_callback) | On very rare occasion, a minifilter might need to define its own callback routine to free contexts, rather than rely on the filter manager. |

## Context registration code example

The following code example, which is taken from the [CTX sample minifilter driver](https://github.com/microsoft/Windows-driver-samples/tree/master/filesys/miniFilter/ctx), shows an array of **FLT_CONTEXT_REGISTRATION** structures that are used to register instance, file, stream, and file object (stream handle) contexts.

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
