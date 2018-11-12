---
title: Other Symbol Stores
description: Other Symbol Stores
ms.assetid: 65bb4291-c56a-4837-ac45-6751ebdbd579
keywords: ["symbol stores, writing your own symbol store"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Other Symbol Stores


## <span id="ddk_using_other_symbol_stores_dbg"></span><span id="DDK_USING_OTHER_SYMBOL_STORES_DBG"></span>


It is possible to write your own symbol store creation program, rather than using SymStore.

Since SymStore transactions are all logged in CSV-format text files, you can leverage any existing SymStore log files for use in your own database program.

If you plan to use the SymSrv program provided with Debugging Tools for Windows package, it is recommended that you use SymStore as well. Updates to these two programs will always be released together, and therefore their versions will always match.

 

 





