---
title: Freeing Contexts
description: Freeing Contexts
ms.assetid: e2b87662-c1bd-45a7-82a3-29817f7692fc
keywords: ["contexts WDK file system minifilter , freeing", "freeing contexts"]
---

# Freeing Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


A context is freed after it is deleted and all outstanding references to it have been released.

There is one exception to this rule: if a context has been created but has not been set by calling **FltSet***Xxx***Context**, it does not need to be deleted. It is freed when its reference count reaches zero. (See the code example in [Releasing Contexts](releasing-contexts.md).)

When a minifilter driver registers its context types, each context definition can optionally include a context cleanup callback routine to be called before the context is freed. For more information, see [**PFLT\_CONTEXT\_CLEANUP\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551078).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Freeing%20Contexts%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




