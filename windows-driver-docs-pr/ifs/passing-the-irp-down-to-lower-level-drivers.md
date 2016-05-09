---
title: Passing the IRP Down to Lower-Level Drivers
description: Passing the IRP Down to Lower-Level Drivers
ms.assetid: 9a8e72fb-b0a8-4026-8606-57fa03344146
keywords: ["IRP dispatch routines WDK file system , passing IRP down", "passing IRPs down device stack WDK"]
---

# Passing the IRP Down to Lower-Level Drivers


## <span id="ddk_passing_the_irp_down_to_lower_level_drivers_if"></span><span id="DDK_PASSING_THE_IRP_DOWN_TO_LOWER_LEVEL_DRIVERS_IF"></span>


By default every dispatch routine, after checking the IRP's target device object, must pass the IRP down to the next-lower-level device driver by calling [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336). It is especially important that your filter driver pass down any IRPs that it does not recognize instead of simply failing them. Failing unfamiliar IRPs can cause the operating system itself to fail in unexpected ways. For example, failing IRP\_MJ\_PNP requests in a file system filter driver can interfere with power management by preventing system hibernation. This is true despite the fact that file system filter drivers are not involved in power management and do not receive [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) requests.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Passing%20the%20IRP%20Down%20to%20Lower-Level%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




