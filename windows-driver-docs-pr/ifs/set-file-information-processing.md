---
title: Set File Information Processing
description: Set File Information Processing
keywords:
- security WDK file systems , semantic model checks
- semantic model checks WDK file systems , set file information processing
- set file information processing WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Set File Information Processing


## <span id="ddk_set_file_information_processing_if"></span><span id="DDK_SET_FILE_INFORMATION_PROCESSING_IF"></span>


The I/O manager executes some additional checks for a subset of the information classes supported by [**IRP\_MJ\_SET\_INFORMATION**](./irp-mj-set-information.md). Specifically, for FileRenameInformation, FileLinkInformation and FileMoveClusterInformation, the I/O manager issues an open to the parent directory of the target name to ensure that the user has access to create a child under that parent before it sends down the IRP\_MJ\_SET\_INFORMATION request to the file system.

 

