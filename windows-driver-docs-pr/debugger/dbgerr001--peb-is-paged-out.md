---
title: dbgerr001 PEB is Paged Out
description: dbgerr001 PEB is Paged Out
ms.assetid: 60b20242-e458-4c36-b78d-17703c02b8b9
keywords: ["dbgerr001", "PEB is paged out (dbgerr001)"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# dbgerr001: PEB is Paged Out


## <span id="ddk_dbgerr001_dbg"></span><span id="DDK_DBGERR001_DBG"></span>


Debugger error **dbgerr001** displays the message "PEB is paged out." This error indicates that the process environment block (PEB) is not accessible.

To load symbols, the debugger looks at the list of modules loaded by the operating system. The pointer to the user-mode module list is one of the items stored in the PEB.

In order to reclaim memory, the Memory Manager may page out user-mode data to make space for other process or kernel mode components.

When this error occurs, it means that the debugger has detected that the PEB data structure for this process is no longer readable. Most likely, is has been paged out to disk.

Without this data structure, the debugger cannot determine what images the symbols should be loaded for.

**Note**   This only affects symbol files for the user-mode modules. Kernel-mode modules and symbols are not affected, as they are tracked in a different list.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20dbgerr001:%20PEB%20is%20Paged%20Out%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




