---
title: Accessing Local Variables
description: Accessing Local Variables
ms.assetid: 0aab3fdf-fe0c-46ad-aa2f-90992811b001
keywords: ["local variables, accessing"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Accessing Local Variables


## <span id="ddk_debugging_bios_code_dbg"></span><span id="DDK_DEBUGGING_BIOS_CODE_DBG"></span>


Local variables, like global variables, are stored in the symbol files. And as with global variables, the debugger interprets their names as addresses. They can be read and written in the same manner as global variables. However, if you need to indicate to a command that a symbol is local, precede the symbol with a dollar sign ( $ ) and an exclamation point ( ! ), as in `$!var`.

Visual Studio and WinDbg provide user interface elements that you can use (in addition to commands) to view and edit local variables. For more information, see [Viewing and Editing Memory and Registers in Visual Studio](viewing-memory--variables--and-registers-in-visual-studio.md) and [Viewing and Editing Local Variables in WinDbg](locals-window.md).

You can also use the following methods to display, change, and use local variables:

-   The [**dv (Display Local Variables)**](dv--display-local-variables-.md) command displays the names and values of all local variables.

-   The [**!for\_each\_local**](-for-each-local.md) extension enables you to execute a single command repeatedly, once for each local variable.

However, there is one primary difference between local and global variables. When an application is executing, the meaning of local variables depends on the location of the program counter, because the scope of such variables extends only to the function in which they are defined.

The debugger interprets local variables according to the [local context](changing-contexts.md#local-context). By default, this context matches the location of the program counter. But the debugger can change the context. For more information about the local context, see Local Context.

When the local context is changed, the Locals window is immediately updated to reflect the new collection of local variables. The [**dv**](dv--display-local-variables-.md) command also shows the new variables. All of these variable names are then interpreted correctly by the memory commands that are described earlier. You can then read or write to these variables.

 

 





