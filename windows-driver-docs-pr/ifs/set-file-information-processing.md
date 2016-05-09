---
title: Set File Information Processing
description: Set File Information Processing
ms.assetid: bda94e8d-0be1-4730-a82e-4aa4d3763cce
keywords: ["security WDK file systems , semantic model checks", "semantic model checks WDK file systems , set file information processing", "set file information processing WDK file systems"]
---

# Set File Information Processing


## <span id="ddk_set_file_information_processing_if"></span><span id="DDK_SET_FILE_INFORMATION_PROCESSING_IF"></span>


The I/O manager executes some additional checks for a subset of the information classes supported by [**IRP\_MJ\_SET\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549366). Specifically, for FileRenameInformation, FileLinkInformation and FileMoveClusterInformation, the I/O manager issues an open to the parent directory of the target name to ensure that the user has access to create a child under that parent before it sends down the IRP\_MJ\_SET\_INFORMATION request to the file system.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Set%20File%20Information%20Processing%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




