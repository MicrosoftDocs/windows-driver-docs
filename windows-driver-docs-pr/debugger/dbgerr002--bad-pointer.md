---
title: dbgerr002 Bad Pointer
description: dbgerr002 Bad Pointer
ms.assetid: d5f2404e-3e7d-4de2-a772-0d42169eb9ad
keywords: ["dbgerr002", "Bad pointer (dbgerr002)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# dbgerr002: Bad Pointer


## <span id="ddk_dbgerr002_dbg"></span><span id="DDK_DBGERR002_DBG"></span>


Debugger error **dbgerr002** displays the message "Bad pointer." This error indicates a problem retrieving a symbol file.

The symbol server has the file indexed, but is being redirected to another location to find the file. No file is accessible at this other location.

Two common causes of this problem are:

-   The path is a UNC path, and the computer containing this server is not available.

-   The path indicates a directory or file that has been deleted.

If your symbol store was created by using SymStore, you can find the full path to this file by examining file.ptr. For details, see [Using SymStore](symstore.md).

 

 





