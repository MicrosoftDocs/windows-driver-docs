---
title: Getting Contexts
description: Getting Contexts
ms.assetid: e0e659e5-6f95-4378-8764-63d96c7d07d4
keywords: ["contexts WDK file system minifilter , getting"]
---

# Getting Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


Once a minifilter driver has set a context for an object, it can get the context by calling **FltGet***Xxx***Context**, where *Xxx* is the context type.

In the following code example, taken from the SwapBuffers sample minifilter driver, the minifilter driver calls [**FltGetVolumeContext**](https://msdn.microsoft.com/library/windows/hardware/ff543189) to get a volume context:

```
status = FltGetVolumeContext(
 FltObjects->Filter,    //Filter
 FltObjects->Volume,    //Volume
                &amp;volCtx);              //Context
...
if (volCtx != NULL) {
 FltReleaseContext(volCtx);
}
```

If the call to [**FltGetVolumeContext**](https://msdn.microsoft.com/library/windows/hardware/ff543189) is successful, the *Context* parameter receives the address of the caller's volume context. **FltGetVolumeContext** increments the reference count on the *Context* pointer. Thus, when this pointer is no longer needed, the minifilter driver must release it by calling [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Getting%20Contexts%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




