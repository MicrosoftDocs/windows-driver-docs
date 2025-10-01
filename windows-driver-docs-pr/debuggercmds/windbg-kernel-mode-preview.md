---
title: 'WinDbg: Start a Kernel Mode Session'
description: "This article describes how to start a kernel mode session with WinDbg."
keywords: ["Starting a kernel mode session", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 01/09/2020
ms.topic: how-to
---

# WinDbg: Start a kernel mode session

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This article describes how to start a kernel mode session with WinDbg, the debugger for Windows.

The process is similar to how it was done with previous versions of WinDbg. Select the tab for the type of transport that you're using, fill in the required fields, and select **OK**.

> [!NOTE]
> Local kernel debugging requires WinDbg to start with elevated privileges.

:::image type="content" source="images/windbgx-attach-to-kernel.png" alt-text="Screenshot of the Start debugging pane with the Attach to kernel menu showing the Net tab.":::

On the **Paste** tab, you can paste in custom connection strings.

If you aren't familiar with how to set up a debugger kernel-mode session, see [Get started with WinDbg (kernel mode)](../debugger/getting-started-with-windbg--kernel-mode-.md).

## Related content

- [WinDbg features](../debugger/debugging-using-windbg-preview.md)