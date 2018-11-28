---
title: File System Fundamentals
description: File System Fundamentals
ms.assetid: 29f0d7cb-9574-489c-affd-31ffdce6abdc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File System Fundamentals


## <span id="ddk_file_system_fundamentals_if"></span><span id="DDK_FILE_SYSTEM_FUNDAMENTALS_IF"></span>


<div class="alert">
<strong>Note</strong>   For optimal reliability and performance, we recommend using <a href="filter-manager-and-minifilter-driver-architecture.md" data-raw-source="[file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md)">file system minifilter drivers</a> instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see <a href="advantages-of-the-filter-manager-model.md" data-raw-source="[Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md)">Advantages of the Filter Manager Model</a>. To port your legacy driver to a minifilter driver, see <a href="guidelines-for-porting-legacy-filter-drivers.md" data-raw-source="[Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md)">Guidelines for Porting Legacy Filter Drivers</a>.
</div>
 

This section introduces fundamental file system driver concepts that are important to developers of file system filter drivers. The following topics are discussed:

[What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md)

[What Happens to File Systems During System Boot](what-happens-to-file-systems-during-system-boot.md)

[Storage Volumes, Storage Device Stacks, and File System Stacks](storage-device-stacks--storage-volumes--and-file-system-stacks.md)

[Mounting a Volume](mounting-a-volume.md)

 

 




