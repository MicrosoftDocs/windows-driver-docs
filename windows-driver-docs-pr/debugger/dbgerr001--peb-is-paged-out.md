---
title: dbgerr001 PEB is Paged Out
description: dbgerr001 PEB is Paged Out
ms.assetid: 60b20242-e458-4c36-b78d-17703c02b8b9
keywords: ["dbgerr001", "PEB is paged out (dbgerr001)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# dbgerr001: PEB is Paged Out


## <span id="ddk_dbgerr001_dbg"></span><span id="DDK_DBGERR001_DBG"></span>


Debugger error **dbgerr001** displays the message "PEB is paged out." This error indicates that the process environment block (PEB) is not accessible.

To load symbols, the debugger looks at the list of modules loaded by the operating system. The pointer to the user-mode module list is one of the items stored in the PEB.

In order to reclaim memory, the Memory Manager may page out user-mode data to make space for other process or kernel mode components.

When this error occurs, it means that the debugger has detected that the PEB data structure for this process is no longer readable. Most likely, is has been paged out to disk.

Without this data structure, the debugger cannot determine what images the symbols should be loaded for.

**Note**   This only affects symbol files for the user-mode modules. Kernel-mode modules and symbols are not affected, as they are tracked in a different list.

 

 

 





