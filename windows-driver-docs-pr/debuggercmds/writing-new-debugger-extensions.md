---
title: "Writing New Debugger Extensions"
description: "Writing New Debugger Extensions"
keywords: ["extension commands ( commands), writing extensions", "writing extension commands", "dbgeng.h header file, writing extension commands", "wdbgexts.h header file, writing extension commands"]
ms.date: 05/23/2017
---

# Writing New Debugger Extensions

You can create your own debugging commands by writing an extension DLL. For example, you might want to write a command to display a complex data structure, or a command that will stop and start the target depending on the value of certain variables or memory locations.

There are two different types of debugger extensions:

- *DbgEng extensions*. These are based on the prototypes in the dbgeng.h header file, and also those in the wdbgexts.h header file.

- *WdbgExts extensions*. These are based on the prototypes in the wdbgexts.h header file alone.

For information about how to write debugger extensions, see [Writing DbgEng Extensions](../debugger/writing-dbgeng-extensions.md) and [Writing WdbgExts Extensions](../debugger/writing-wdbgexts-extensions.md).

