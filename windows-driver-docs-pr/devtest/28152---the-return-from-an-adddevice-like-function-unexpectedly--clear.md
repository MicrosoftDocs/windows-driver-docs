---
title: C28152
description: Warning C28152 The return from an AddDevice-like function unexpectedly DO\_DEVICE\_INITIALIZING.
ms.assetid: df2b68dc-b22b-4aaa-b1ba-b34bfdd9b886
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28152


warning C28152: The return from an AddDevice-like function unexpectedly DO\_DEVICE\_INITIALIZING

The driver has returned from its **AddDevice** routine, or a similar utility routine, but the **DO\_DEVICE\_INITIALIZING** bit of the **Flags** word (**DeviceObject-&gt;Flags**) in the **DeviceObject** routine is not cleared.

The **AddDevice** routine must contain code similar to the following to clear the **DO\_DEVICE\_INITIALIZING** flag.

```
FunctionalDeviceObject->Flags &= ~DO_DEVICE_INITIALIZING;
```

For more information about **AddDevice** routines, see [AddDevice Routines in Function or Filter Drivers](https://msdn.microsoft.com/library/windows/hardware/ff540529)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28152%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




