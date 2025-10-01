---
title: 'WinDbg: Scripting Menu'
description: "This article describes how to use scripting in the WinDbg debugger."
keywords: ["Scripting Menu", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 01/20/2020
ms.topic: how-to
---

# WinDbg: Scripting menu

This article describes how to use the scripting support in WinDbg, the debugger for Windows.

:::image type="content" source="images/windbgx-javascript-new-script.png" alt-text="Screenshot of the Scripting menu in WinDbg.":::

The WinDbg **Scripting** window features basic syntax highlighting, IntelliSense, and error recognition.

Use the ribbon buttons to:

- Create a new script.
- Open an existing script.
- Execute a script.
- Save a script.
- Unlink a script.

You can also automatically execute scripts by right-clicking in the **Scripting** window and selecting **Execute Script on Save**. When you successfully load a script, a green checkbox appears on the script title bar. If there are errors in the script, a red X appears.

## JavaScript scripting

To start using JavaScript, you must first be debugging a target. When you're ready to start working on your JavaScript, select `Load JavaScript Provider`. After that, you can create a new JavaScript by choosing between the following two types of script templates:

- **Extension script**: This script acts as an extension to the debugger. It manipulates the object model of the debugger and provides continued functionality. No action happens when you select **Execute** on the ribbon.
- **Imperative script**: This script performs an action every time that you select **Execute** on the ribbon. Such a script doesn't generally modify the object model of the debugger.

For more information about working with JavaScript, see:

- [JavaScript debugger scripting](../debugger/javascript-debugger-scripting.md)
- [Native debugger objects in JavaScript extensions](../debugger/native-objects-in-javascript-extensions.md)
- [JavaScript debugger example scripts](../debugger/javascript-debugger-example-scripts.md)

## NatVis scripting

Use **New Script** > **NatVis** to open the following blank NatVis template:

```xml
<AutoVisualizer xmlns="https://schemas.microsoft.com/vstudio/debugger/natvis/2010">
  <Type Name="">
  </Type>
</AutoVisualizer>
```

For more information about working with NatVis, see [Debugger objects in NatVis](../debugger/native-debugger-objects-in-natvis.md).

---

## Related content

- [WinDbg features](../debugger/debugging-using-windbg-preview.md)