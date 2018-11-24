---
title: Returning Status from Completion Routines
description: Returning Status from Completion Routines
ms.assetid: fb12720b-10fe-43ab-ade7-c1b09d00d922
keywords:
- IRP completion routines WDK file system , returning status
- status values WDK file system
- success status values WDK file system
- returning status WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




