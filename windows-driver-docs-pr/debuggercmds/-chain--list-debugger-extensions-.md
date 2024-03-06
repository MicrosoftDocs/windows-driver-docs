---
title: .chain (List Debugger Extensions)
description: The .chain command lists all loaded debugger extensions in their default search order.
keywords: [".chain (List Debugger Extensions) Windows Debugging"]
ms.date: 08/30/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- .chain (List Debugger Extensions)
api_type:
- NA
---

# .chain (List Debugger Extensions)

The **.chain** command lists all loaded debugger extensions in their default search order.

```dbgsyntax
.chain
.chain /D
```

## Parameters

**/D**

Displays the output using [Debugger Markup Language](../debugger/debugger-markup-language-commands.md). In the output, each listed module is a link that you can click to get information about the extensions that are implemented by the module.

### Environment

| Item      | Description            |
|-----------|------------------------|
| Modes     | User mode, kernel mode |
| Targets   | Live, crash dump       |
| Platforms | All                    |

### Additional Information

For details on loading, unloading, and controlling extensions, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md). For details on executing extension commands and an explanation of the default search order, see [Using Debugger Extension Commands](using-debugger-extension-commands.md).
