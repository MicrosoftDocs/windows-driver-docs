---
title: Tracking Per-Stream Context in a Legacy File System Filter Driver
author: windows-driver-content
description: Tracking Per-Stream Context in a Legacy File System Filter Driver
ms.assetid: d908ee30-a433-460c-8c14-883702b4f810
keywords: ["context tracking WDK file system"]
---

# Tracking Per-Stream Context in a Legacy File System Filter Driver


## <span id="ddk_tracking_per_stream_context_in_a_file_system_filter_driver_if"></span><span id="DDK_TRACKING_PER_STREAM_CONTEXT_IN_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


**Note**  For optimal reliability and performance, we recommend using [file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md) instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see [Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md). To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

 

This section covers per-stream context tracking in Microsoft Windows XP and later OS versions. The following topics are discussed:

[File Streams, Stream Contexts, and Per-Stream Contexts](file-streams--stream-contexts--and-per-stream-contexts.md)

[Creating and Using Per-Stream Context Structures](creating-and-using-per-stream-context-structures.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Tracking%20Per-Stream%20Context%20in%20a%20Legacy%20File%20System%20Filter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


