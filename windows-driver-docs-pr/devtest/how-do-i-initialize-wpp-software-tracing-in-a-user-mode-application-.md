---
title: How do I initialize WPP software tracing in a user-mode application
description: How do I initialize WPP software tracing in a user-mode application
ms.assetid: 1f1ab873-a1c3-4915-af31-ab74c1898fcb
---

# How do I initialize WPP software tracing in a user-mode application?


You can initialize WPP tracing in a user-mode application by calling the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro to initialize WPP software tracing.

To avoid errors, you should call the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro at a point in your source code where no tracing attempts have been previously made.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20initialize%20WPP%20software%20tracing%20in%20a%20user-mode%20application?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




