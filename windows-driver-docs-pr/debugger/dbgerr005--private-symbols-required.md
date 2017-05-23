---
title: dbgerr005 Private Symbols Required
description: dbgerr005 Private Symbols Required
ms.assetid: 0e3b9c98-1f02-4fff-9a91-d3a7470df882
keywords: ["dbgerr005", "Private symbols required (dbgerr005)"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# dbgerr005: Private Symbols Required


## <span id="ddk_dbgerr005_dbg"></span><span id="DDK_DBGERR005_DBG"></span>


Debugger error **dbgerr005** displays the message "Private symbols (symbols.pri) are required for locals." This error indicates that the debugger is unable to perform an action because private symbols are not present.

During kernel-mode debugging, the debugger needs symbols for Microsoft Windows. During user-mode debugging, the debugger needs symbols for the target application, and often needs symbols for Windows as well.

Some basic symbols, such as function names and global variables, are needed for even the most rudimentary debugging. These are called *public symbols*. Symbols such as data structure names, global variables visible in only one object file, local variables, and line number information are not always required for debugging, although they are useful for a more in-depth debugging session. These are called *private symbols*.

Many software manufacturers, including Microsoft, produce two versions of their symbol files. The version released to their customers contains only public symbols. The version used internally contains both public and private symbols.

Most debugging actions can be performed with public symbols alone. But certain actions -- such as displaying local variables -- require private symbols. When an action of this sort is attempted and private symbols are not available, this error message is displayed.

When you see this message, it is usually best to simply continue debugging. The information you were unable to obtain is probably not essential to properly debugging the target.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20dbgerr005:%20Private%20Symbols%20Required%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




