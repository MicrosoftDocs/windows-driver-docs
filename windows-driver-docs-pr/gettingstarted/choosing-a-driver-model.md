---
title: Choosing a driver model
description: Microsoft Windows provides a variety of driver models that you can use to write drivers.
ms.assetid: 67de6453-969e-4b4d-a72e-de132b20b022
keywords:
- driver model
- driver design
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Choosing a driver model


Microsoft Windows provides a variety of driver models that you can use to write drivers. The strategy for choosing the best driver model depends on the type of driver you are planning to write. Here are the options:

-   Device function driver
-   Device filter driver
-   Software driver
-   File system filter driver
-   File system driver

For a discussion about the differences between the various types of drivers, see [What is a driver?](what-is-a-driver-.md) and [Device nodes and device stacks](device-nodes-and-device-stacks.md). The following sections explain how to choose a model for each type of driver.

## <span id="choosing_a_driver_model_for_a_device_function_driver"></span><span id="CHOOSING_A_DRIVER_MODEL_FOR_A_DEVICE_FUNCTION_DRIVER"></span>Choosing a driver model for a device function driver


As you design a hardware device, one of the first things to consider is whether you need to write a function driver. Ask the following questions:

Can you avoid writing a driver entirely?
If you must write a function driver, what is the best driver model to use?
To answer these questions, determine where your device fits in the list of technologies described in [Device and driver technologies](https://msdn.microsoft.com/library/windows/hardware/ff557557). See the documentation for that particular technology to determine whether you need to write a function driver and to learn about which driver models are available for your device.

Some of the individual technologies have minidriver models. In a minidriver model, the device driver consists of two parts: one that handles general tasks, and one that handles device-specific tasks. Typically, Microsoft writes the general portion and the device manufacturer writes the device-specific portion. The device specific portions have a variety of names, most of which share the prefix *mini*. Here are some of the names used in minidriver models:

-   Display miniport driver
-   Audio miniport driver
-   Battery miniclass driver
-   Bluetooth protocol driver
-   HID minidriver
-   WIA minidriver
-   NDIS miniport driver
-   Storage miniport driver
-   Streaming minidriver

For an overview of minidriver models, see [Minidrivers and driver pairs](minidrivers-and-driver-pairs.md).

Not every technology listed in [Device and driver technologies](https://msdn.microsoft.com/library/windows/hardware/ff557557) has a dedicated minidriver model. The documentation for a particular technology might advise you to use the [Kernel-Mode Driver Framework (KMDF)](https://msdn.microsoft.com/library/windows/hardware/ff557565); the documentation for another technology might advise you to use the [User-Mode Driver Framework (UMDF)](https://msdn.microsoft.com/library/windows/hardware/ff557565). The key point is that you should start by studying the documentation for your specific device technology. If your device technology has a minidriver model, you must use the minidriver model. Otherwise follow the advice in the your technology-specific documentation about whether to use the UMDF, KMDF, or the Windows Driver Model (WDM).

## <span id="Choosing_a_driver_model_for_a_device_filter_driver"></span><span id="choosing_a_driver_model_for_a_device_filter_driver"></span><span id="CHOOSING_A_DRIVER_MODEL_FOR_A_DEVICE_FILTER_DRIVER"></span>Choosing a driver model for a device filter driver


Frequently several drivers participate in a single I/O request (like reading data from a device). The drivers are layered in a stack, and the conventional way to visualize the stack is with the first driver at the top and the last driver at the bottom. The stack has one function driver and can also have filter drivers. For a discussion about function drivers and filter drivers, see [What is a driver?](what-is-a-driver-.md) and [Device nodes and device stacks](device-nodes-and-device-stacks.md).

If you are preparing to write a filter driver for a device, determine where your device fits in the list of technologies described in [Device and driver technologies](https://msdn.microsoft.com/library/windows/hardware/ff557557). Check to see whether the documentation for your particular device technology has any guidance on choosing a filter driver model. If the documentation for your device technology does not offer this guidance, then first consider using UMDF as your driver model. If your filter driver needs access to data structures that are not available through UMDF, consider using KMDF as your driver model. In the extremely rare case that your driver needs access to data structures not available through KMDF, use WDM as your driver model.

## <span id="Choosing_a_driver_model_for_a_software_driver"></span><span id="choosing_a_driver_model_for_a_software_driver"></span><span id="CHOOSING_A_DRIVER_MODEL_FOR_A_SOFTWARE_DRIVER"></span>Choosing a driver model for a software driver


A driver that is not associated with a device is called a *software driver*. For a discussion about software drivers, see the [What is a driver?](what-is-a-driver-.md) topic. Software drivers are useful because they can run in kernel mode, which gives them access to protected operating system data. For information about processor modes, see [User mode and kernel mode](user-mode-and-kernel-mode.md).

For a software driver, your two options are KMDF and the kernel-modeWindows NT driver model. With both KMDF and the kernel-modeWindows NT model, you can write your driver without being concerned about Plug and Play (PnP) and power management. You can concentrate instead on your driver's primary tasks. With KMDF, you do not have to be concerned with PnP and power because the framework handles PnP and power for you. With the kernel-modeWindows NT model, you do not have to be concerned about PnP and power because kernel-mode services operate in an environment that is completely independent from PnP and power management.

Our recommendation is that you use KMDF, especially if you are already familiar with it. If you want your driver to be completely independent from PnP and power management, use the kernel-modeWindows NT model. If you need to write a software driver that is aware of power transitions or PnP events, you cannot use the kernel-modeWindows NT model; you must use KMDF.

**Note**  In the very rare case that you need to write a software driver that is aware of PnP or power events, and your driver needs access to data that is not available through KMDF, you must use WDM.

 

## <span id="Choosing_a_driver_model_for_a_file_system_filter_driver"></span><span id="choosing_a_driver_model_for_a_file_system_filter_driver"></span><span id="CHOOSING_A_DRIVER_MODEL_FOR_A_FILE_SYSTEM_FILTER_DRIVER"></span>Choosing a driver model for a file system filter driver


For help with choosing a model for a file system filter driver, see File system minifilter drivers and [File system filter drivers](https://msdn.microsoft.com/library/windows/hardware/ff540382).

## <span id="Choosing_a_driver_model_for_a_file_system_driver"></span><span id="choosing_a_driver_model_for_a_file_system_driver"></span><span id="CHOOSING_A_DRIVER_MODEL_FOR_A_FILE_SYSTEM_DRIVER"></span>Choosing a driver model for a file system driver


For help choosing a model for a file system driver, see [File System Minifilter Drivers](https://msdn.microsoft.com/library/windows/hardware/ff540402).

## <span id="related_topics"></span>Related topics


[Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff557565)

[User-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff557565)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wdkgetstart\wdkgetstart]:%20Choosing%20a%20driver%20model%20%20RELEASE:%20%281/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





