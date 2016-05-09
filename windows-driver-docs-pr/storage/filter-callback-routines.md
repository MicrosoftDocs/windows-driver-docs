---
title: Filter Callback Routines
description: Filter Callback Routines
ms.assetid: 3d9f874c-f026-40fc-a97d-0d4cefa3d1f9
---

# Filter Callback Routines


The crash dump driver supports the following callback routines in a crash dump filter driver. These callback routines are not mandatory, so a crash dump filter driver is free to implement only a callback routine that is required to add the desired functionality.

[**Dump\_Start**](https://msdn.microsoft.com/library/windows/hardware/ff552767)

[**Dump\_Write**](https://msdn.microsoft.com/library/windows/hardware/ff553709)

[**Dump\_Read**](https://msdn.microsoft.com/library/windows/hardware/hh439713)

[**Dump\_Finish**](https://msdn.microsoft.com/library/windows/hardware/ff552764)

[**Dump\_Unload**](https://msdn.microsoft.com/library/windows/hardware/ff552773)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Filter%20Callback%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




