---
title: Choosing a Driver Model
description: Microsoft Windows provides a variety of driver models that you can use to write drivers.
keywords:
- driver model
- driver design
ms.date: 08/06/2021
---

# Choosing a driver model


Microsoft Windows provides a variety of driver models that you can use to write drivers. The strategy for choosing the best driver model depends on the type of driver you are planning to write. Here are the options:

-   Device function driver
-   Device filter driver
-   Software driver
-   File system filter driver
-   File system driver

For a discussion about the differences between the various types of drivers, see [What is a driver?](what-is-a-driver-.md) and [Device nodes and device stacks](device-nodes-and-device-stacks.md). The following sections explain how to choose a model for each type of driver.

## Choosing a driver model for a device function driver


As you design a hardware device, one of the first things to consider is whether you need to write a function driver. Ask the following questions:

Can you avoid writing a driver entirely?
If you must write a function driver, what is the best driver model to use?
To answer these questions, determine where your device fits in the list of technologies described in [Device and driver technologies](../device-and-driver-technologies.md). See the documentation for that particular technology to determine whether you need to write a function driver and to learn about which driver models are available for your device.

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

Not every technology listed in [Device and driver technologies](../device-and-driver-technologies.md) has a dedicated minidriver model. The documentation for a particular technology might advise you to use the [Kernel-Mode Driver Framework (KMDF)](../wdf/index.md); the documentation for another technology might advise you to use the [User-Mode Driver Framework (UMDF)](../wdf/index.md). The key point is that you should start by studying the documentation for your specific device technology. If your device technology has a minidriver model, you must use the minidriver model. Otherwise follow the advice in the your technology-specific documentation about whether to use the UMDF, KMDF, or the Windows Driver Model (WDM).

## Choosing a driver model for a device filter driver


Frequently several drivers participate in a single I/O request (like reading data from a device). The drivers are layered in a stack, and the conventional way to visualize the stack is with the first driver at the top and the last driver at the bottom. The stack has one function driver and can also have filter drivers. For a discussion about function drivers and filter drivers, see [What is a driver?](what-is-a-driver-.md) and [Device nodes and device stacks](device-nodes-and-device-stacks.md).

If you are preparing to write a filter driver for a device, determine where your device fits in the list of technologies described in [Device and driver technologies](../device-and-driver-technologies.md). Check to see whether the documentation for your particular device technology has any guidance on choosing a filter driver model. If the documentation for your device technology does not offer this guidance, then first consider using UMDF as your driver model. If your filter driver needs access to data structures that are not available through UMDF, consider using KMDF as your driver model. In the extremely rare case that your driver needs access to data structures not available through KMDF, use WDM as your driver model.

## Choosing a driver model for a software driver


A driver that is not associated with a device is called a *software driver*. For a discussion about software drivers, see the [What is a driver?](what-is-a-driver-.md) topic. Software drivers are useful because they can run in kernel mode, which gives them access to protected operating system data. For information about processor modes, see [User mode and kernel mode](user-mode-and-kernel-mode.md).

For a software driver, your two options are KMDF and the legacy Windows NT driver model. With both KMDF and the legacy Windows NT model, you can write your driver without being concerned about Plug and Play (PnP) and power management. You can concentrate instead on your driver's primary tasks. With KMDF, you do not have to be concerned with PnP and power because the framework handles PnP and power for you. With the legacy Windows NT model, you do not have to be concerned about PnP and power because kernel-mode services operate in an environment that is completely independent from PnP and power management.

Our recommendation is that you use KMDF, especially if you are already familiar with it. If you want your driver to be completely independent from PnP and power management, use the legacy Windows NT model. If you need to write a software driver that is aware of power transitions or PnP events, you cannot use the legacy Windows NT model; you must use KMDF.

**Note**  In the very rare case that you need to write a software driver that is aware of PnP or power events, and your driver needs access to data that is not available through KMDF, you must use WDM.

## Choosing a driver model for a file system driver


For help with choosing a model for a file system driver, see [File system driver samples](../samples/file-system-driver-samples.md). Note that file system drivers can be quite complex and may require knowledge of advanced concepts for driver development.


## Choosing a driver model for a file system filter driver


For help with choosing a model for a file system filter driver, see File system minifilter drivers and [File system filter drivers](../ifs/index.md#file-system-filter-drivers).

## Choosing a driver model for a file system minifilter driver


For help choosing a model for a file system minifilter driver, see [File System Minifilter Drivers](../ifs/filter-manager-concepts.md).

## Related topics


[Kernel-Mode Driver Framework](../wdf/index.md)

[User-Mode Driver Framework](../wdf/index.md)

 

