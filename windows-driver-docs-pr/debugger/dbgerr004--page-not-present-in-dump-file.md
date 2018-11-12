---
title: dbgerr004 Page Not Present in Dump File
description: dbgerr004 Page Not Present in Dump File
ms.assetid: e76d11fc-857b-4a40-8f41-f34f3bcade57
keywords: ["dbgerr004", "Page not present in dump file (dbgerr004)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# dbgerr004: Page Not Present in Dump File


## <span id="ddk_dbgerr004_dbg"></span><span id="DDK_DBGERR004_DBG"></span>


Debugger error **dbgerr004** displays the message "Page *number* not present in dump file." This error indicates that the debugger needed a memory page that was not included in the dump file being debugged.

The specified *number* is the page frame number (PFN) corresponding to the location in the physical memory of the original page.

To suppress this error message, use the [**.ignore\_missing\_pages 1**](-ignore-missing-pages--suppress-missing-page-errors-.md) command. This command allows debugging to proceed, but does not display this error message.

Kernel-mode memory dumps come in three sizes, and the smaller sizes do not include all the memory pages. For details, see [Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md).

User-mode memory dumps also come in various sizes. See [User-Mode Dump Files](user-mode-dump-files.md) for details.

 

 





