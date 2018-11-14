---
title: dbgerr005 Private Symbols Required
description: dbgerr005 Private Symbols Required
ms.assetid: 0e3b9c98-1f02-4fff-9a91-d3a7470df882
keywords: ["dbgerr005", "Private symbols required (dbgerr005)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# dbgerr005: Private Symbols Required


## <span id="ddk_dbgerr005_dbg"></span><span id="DDK_DBGERR005_DBG"></span>


Debugger error **dbgerr005** displays the message "Private symbols (symbols.pri) are required for locals." This error indicates that the debugger is unable to perform an action because private symbols are not present.

During kernel-mode debugging, the debugger needs symbols for Microsoft Windows. During user-mode debugging, the debugger needs symbols for the target application, and often needs symbols for Windows as well.

Some basic symbols, such as function names and global variables, are needed for even the most rudimentary debugging. These are called *public symbols*. Symbols such as data structure names, global variables visible in only one object file, local variables, and line number information are not always required for debugging, although they are useful for a more in-depth debugging session. These are called *private symbols*.

Many software manufacturers, including Microsoft, produce two versions of their symbol files. The version released to their customers contains only public symbols. The version used internally contains both public and private symbols.

Most debugging actions can be performed with public symbols alone. But certain actions -- such as displaying local variables -- require private symbols. When an action of this sort is attempted and private symbols are not available, this error message is displayed.

When you see this message, it is usually best to simply continue debugging. The information you were unable to obtain is probably not essential to properly debugging the target.

 

 





