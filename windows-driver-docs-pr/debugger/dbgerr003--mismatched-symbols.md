---
title: dbgerr003 Mismatched Symbols
description: dbgerr003 Mismatched Symbols
ms.assetid: 95251f5a-5479-4dc8-b3bb-4eb6096bdb6e
keywords: ["dbgerr003", "Mismatched symbols (dbgerr003)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# dbgerr003: Mismatched Symbols


## <span id="ddk_dbgerr003_dbg"></span><span id="DDK_DBGERR003_DBG"></span>


Debugger error **dbgerr003** displays the message "*File* has mismatched symbols." This error indicates that DbgHelp found the symbol file represented by File, but that the symbol file is not the correct version, or that DbgHelp cannot confirm that the symbol file is the correct version.

The debugger might load the specified symbol file despite this error, depending on other requirements in the path.

 

 





