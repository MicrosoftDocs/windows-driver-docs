---
title: Tracking Per-Stream Context in a Legacy File System Filter Driver
description: Tracking Per-Stream Context in a Legacy File System Filter Driver
ms.assetid: d908ee30-a433-460c-8c14-883702b4f810
keywords:
- context tracking WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tracking Per-Stream Context in a Legacy File System Filter Driver


## <span id="ddk_tracking_per_stream_context_in_a_file_system_filter_driver_if"></span><span id="DDK_TRACKING_PER_STREAM_CONTEXT_IN_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


<div class="alert">
<strong>Note</strong>   For optimal reliability and performance, we recommend using <a href="filter-manager-and-minifilter-driver-architecture.md" data-raw-source="[file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md)">file system minifilter drivers</a> instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see <a href="advantages-of-the-filter-manager-model.md" data-raw-source="[Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md)">Advantages of the Filter Manager Model</a>. To port your legacy driver to a minifilter driver, see <a href="guidelines-for-porting-legacy-filter-drivers.md" data-raw-source="[Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md)">Guidelines for Porting Legacy Filter Drivers</a>.
</div>
 

This section covers per-stream context tracking in Microsoft Windows XP and later OS versions. The following topics are discussed:

[File Streams, Stream Contexts, and Per-Stream Contexts](file-streams--stream-contexts--and-per-stream-contexts.md)

[Creating and Using Per-Stream Context Structures](creating-and-using-per-stream-context-structures.md)

 

 




