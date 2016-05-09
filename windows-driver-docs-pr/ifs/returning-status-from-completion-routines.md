---
title: Returning Status from Completion Routines
author: windows-driver-content
description: Returning Status from Completion Routines
ms.assetid: fb12720b-10fe-43ab-ade7-c1b09d00d922
keywords: ["IRP completion routines WDK file system , returning status", "status values WDK file system", "success status values WDK file system", "returning status WDK file system"]
---

# Returning Status from Completion Routines


## <span id="ddk_returning_status_from_completion_routines_if"></span><span id="DDK_RETURNING_STATUS_FROM_COMPLETION_ROUTINES_IF"></span>


A file system filter driver completion routine normally returns one of the following two NTSTATUS values to the caller:

-   STATUS\_SUCCESS

-   STATUS\_MORE\_PROCESSING\_REQUIRED

STATUS\_SUCCESS indicates that the driver is finished with the IRP and allows the I/O Manager to continue completion processing on the IRP.

STATUS\_MORE\_PROCESSING\_REQUIRED halts the I/O Manager's completion processing on the IRP.

If any other NTSTATUS value is returned, the I/O Manager resets it to STATUS\_SUCCESS.

For more information about returning STATUS\_MORE\_PROCESSING\_REQUIRED, see [Constraints on Completion Routines](constraints-on-completion-routines.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Returning%20Status%20from%20Completion%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


