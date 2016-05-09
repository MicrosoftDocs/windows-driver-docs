---
title: Feature Description
description: Feature Description
ms.assetid: 19c1378d-f8d8-42a2-9776-4f5bfdb9e39e
---

# Feature Description


The crash dump driver provides a new interface to add filter drivers to the crash dump stack. This interface does not follow any standard filter driver model. Instead, it exposes a proprietary interface that must be used in order to load a driver into the crash dump stack.

Crash dump filter drivers can be made part of the dump stack by adding the service name in a registry key. The crash dump driver loads these drivers when the drivers in the dump stack are loaded. A filter driver is loaded as part of both the hibernation and crash dump stacks. These filter drivers should supply a list of predefined callback routines that will be called during hibernation and crash dump.

The filter model does not allow filter drivers to be loaded only in either the hibernation or crash dump stack. After the service name is added to the filter driver list, the list will be loaded in both stacks. When the callback routines are called, a parameter is passed to indicate the callback reason. The filter driver can then determine what to do based on this parameter.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Feature%20Description%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




