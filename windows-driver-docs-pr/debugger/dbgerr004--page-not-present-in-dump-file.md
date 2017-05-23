---
title: dbgerr004 Page Not Present in Dump File
description: dbgerr004 Page Not Present in Dump File
ms.assetid: e76d11fc-857b-4a40-8f41-f34f3bcade57
keywords: ["dbgerr004", "Page not present in dump file (dbgerr004)"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# dbgerr004: Page Not Present in Dump File


## <span id="ddk_dbgerr004_dbg"></span><span id="DDK_DBGERR004_DBG"></span>


Debugger error **dbgerr004** displays the message "Page *number* not present in dump file." This error indicates that the debugger needed a memory page that was not included in the dump file being debugged.

The specified *number* is the page frame number (PFN) corresponding to the location in the physical memory of the original page.

To suppress this error message, use the [**.ignore\_missing\_pages 1**](-ignore-missing-pages--suppress-missing-page-errors-.md) command. This command allows debugging to proceed, but does not display this error message.

Kernel-mode memory dumps come in three sizes, and the smaller sizes do not include all the memory pages. For details, see [Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md).

User-mode memory dumps also come in various sizes. See [User-Mode Dump Files](user-mode-dump-files.md) for details.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20dbgerr004:%20Page%20Not%20Present%20in%20Dump%20File%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




