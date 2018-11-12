---
title: Debug Resolve Unqualified Symbols
description: Debug Resolve Unqualified Symbols
ms.assetid: 8b935640-a01d-46e8-a9e4-08f20e293196
keywords: ["Debug Resolve Unqualified Symbols"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debug | Resolve Unqualified Symbols


Select **Resolve Unqualified Symbols** on the **Debug** menu to resolve symbols that have no module prefix.

If you clear **Resolve Unqualified Symbols**, the debugger cannot resolve symbols that have no module prefix. If you do not select **Resolve Unqualified Symbols** and a variable that has no prefix is not already loaded, the debugger does not load any additional symbols to resolve it. You can still use unqualified symbols when this option is clear, but only if they have been previously loaded.

Although we always recommend that you use module qualifiers, you can clear the **Resolve Unqualified Symbols** option to avoid loading symbols that resolve incorrect or misspelled symbols when module qualifiers are not used.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about symbols, loading symbols, and verifying symbols, see [Symbols](symbols.md).

 

 





