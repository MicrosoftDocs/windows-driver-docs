---
title: SymStore
description: SymStore
keywords: ["SymStore, features", "SymStore, using", "symbol stores, SymStore (symstore.exe)"]
ms.date: 03/27/2018
ms.localizationpriority: medium
---

# SymStore


## <span id="ddk_using_symstore_dbg"></span><span id="DDK_USING_SYMSTORE_DBG"></span>

SymStore (symstore.exe) is a tool for creating symbol stores. It is included in the Debugging Tools for Windows. For more information, see [Download Debugging Tools for Windows](debugger-download-tools.md).

SymStore stores symbols in a format that enables the debugger to look up the symbols based on the time stamp and size of the image (for a .dbg or executable file), or signature and age (for a .pdb file). The advantage of the symbol store over the traditional symbol storage format is that all symbols can be stored or referenced on the same server and retrieved by the debugger without any prior knowledge of which product contains the corresponding symbol.

Note that multiple versions of .pdb symbol files (for example, public and private versions) cannot be stored on the same server, because they each contain the same signature and age.

This section includes:

[SymStore Transactions](symstore-transactions.md)

[File System References and Symbol Files](file-system-references-and-symbol-files.md)

[Symbol Storage Format](symbol-storage-format.md)

 

 





