---
title: Introduction to File System Filter Drivers
author: windows-driver-content
description: Introduction to File System Filter Drivers
ms.assetid: 7947aaa9-57d4-4adf-8214-151a4755939b
---

# Introduction to File System Filter Drivers


## <span id="ddk_introduction_to_file_system_filter_drivers_if"></span><span id="DDK_INTRODUCTION_TO_FILE_SYSTEM_FILTER_DRIVERS_IF"></span>


<div class="alert">
<strong>Note</strong>   For optimal reliability and performance, we recommend using [file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md) instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see [Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md). To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).
</div>
 

This section introduces file system filter drivers. It includes the following topics:

[What Is a File System Filter Driver?](what-is-a-file-system-filter-driver-.md)

[File System Filter Drivers Are Not Device Drivers](file-system-filter-drivers-are-not-device-drivers.md)

[Installing a File System Filter Driver](installing-a-file-system-filter-driver.md)

[Initializing a File System Filter Driver](initializing-a-file-system-filter-driver.md)

[Attaching a Filter to a File System or Volume](attaching-a-filter-to-a-file-system-or-volume.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Introduction%20to%20File%20System%20Filter%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


