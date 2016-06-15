---
title: Types of Device Objects Used by File System Filter Drivers
author: windows-driver-content
description: Types of Device Objects Used by File System Filter Drivers
ms.assetid: e5662c95-71a0-49f8-a9d5-a03e2de1f426
keywords: ["target device objects WDK file system", "filter device objects WDK file system", "device objects WDK file system", "control device objects WDK file system", "CDOs WDK file system", "FDOs WDK file system"]
---

# Types of Device Objects Used by File System Filter Drivers


## <span id="ddk_types_of_file_system_filter_driver_device_objects_if"></span><span id="DDK_TYPES_OF_FILE_SYSTEM_FILTER_DRIVER_DEVICE_OBJECTS_IF"></span>


To write effective dispatch routines for IRPs and fast I/O requests, it is important to understand the various types of target device objects through which your filter driver can receive these requests.

Unlike drivers for Plug and Play (PnP) devices, such as disk drives, file system filter drivers do not create functional or physical device objects. Instead, they create control device objects and filter device objects. The *control device object* (CDO) represents the filter driver to the system and to user-mode applications. The *filter device object* (filter DO) performs the actual work of filtering a specific file system or volume. A file system filter driver normally creates one CDO and one or more filter DOs.

For each type of I/O request received by your filter driver, the target device object can be one or more of the following:

-   The filter driver's CDO, which is not attached to a driver stack

-   A filter device object that is chained above a file system CDO in the global file system queue

-   A filter device object that is chained above a mounted file system volume device object (VDO)

A filter driver can register only one set of dispatch routines for IRPs and one for fast I/O requests. Thus, each type of request must be handled by a single routine. This routine must ascertain which of the target device objects listed above received the request, so that it can handle the request appropriately.

This section includes:

[The Filter Driver's Control Device Object](the-filter-driver-s-control-device-object.md)

[Filter Device Object Attached to a File System](filter-device-object-attached-to-a-file-system.md)

[Filter Device Object Attached to a Volume](filter-device-object-attached-to-a-volume.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Types%20of%20Device%20Objects%20Used%20by%20File%20System%20Filter%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


