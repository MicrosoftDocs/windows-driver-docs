---
title: C28135
description: Warning C28135 If the first argument to KeWaitForSingleObject is a local variable, the Mode parameter must be KernelMode.
ms.assetid: f42e41d7-240f-4de1-97b7-e50415aee14f
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28135


warning C28135: If the first argument to KeWaitForSingleObject is a local variable, the Mode parameter must be KernelMode

The driver is waiting in user mode. As such, the kernel stack can be swapped out during the wait. If the driver attempts to pass parameters on the stack, a system crash can result.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
KeWaitForSingleObject(&MyMutex, UserRequest, UserMode, false, NULL);
```

The following code example avoids this warning.

```
KeWaitForSingleObject(&MyMutex, UserRequest, KernelMode, false, NULL);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28135%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




