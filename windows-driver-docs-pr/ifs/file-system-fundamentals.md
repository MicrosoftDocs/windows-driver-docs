---
title: File System Fundamentals
author: windows-driver-content
description: File System Fundamentals
ms.assetid: 29f0d7cb-9574-489c-affd-31ffdce6abdc
---

# File System Fundamentals


## <span id="ddk_file_system_fundamentals_if"></span><span id="DDK_FILE_SYSTEM_FUNDAMENTALS_IF"></span>


**Note**  For optimal reliability and performance, we recommend using [file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md) instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see [Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md). To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

 

This section introduces fundamental file system driver concepts that are important to developers of file system filter drivers. The following topics are discussed:

[What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md)

[What Happens to File Systems During System Boot](what-happens-to-file-systems-during-system-boot.md)

[Storage Volumes, Storage Device Stacks, and File System Stacks](storage-device-stacks--storage-volumes--and-file-system-stacks.md)

[Mounting a Volume](mounting-a-volume.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20File%20System%20Fundamentals%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


