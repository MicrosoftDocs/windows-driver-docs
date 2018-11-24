---
title: Getting Contexts
description: Getting Contexts
ms.assetid: e0e659e5-6f95-4378-8764-63d96c7d07d4
keywords:
- contexts WDK file system minifilter , getting
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


Once a minifilter driver has set a context for an object, it can get the context by calling **FltGet***Xxx***Context**, where *Xxx* is the context type.

In the following code example, taken from the SwapBuffers sample minifilter driver, the minifilter driver calls [**FltGetVolumeContext**](https://msdn.microsoft.com/library/windows/hardware/ff543189) to get a volume context:

```cpp
status = FltGetVolumeContext(
 FltObjects->Filter,    //Filter
 FltObjects->Volume,    //Volume
                &volCtx);              //Context
...
if (volCtx != NULL) {
 FltReleaseContext(volCtx);
}
```

If the call to [**FltGetVolumeContext**](https://msdn.microsoft.com/library/windows/hardware/ff543189) is successful, the *Context* parameter receives the address of the caller's volume context. **FltGetVolumeContext** increments the reference count on the *Context* pointer. Thus, when this pointer is no longer needed, the minifilter driver must release it by calling [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314).

 

 




