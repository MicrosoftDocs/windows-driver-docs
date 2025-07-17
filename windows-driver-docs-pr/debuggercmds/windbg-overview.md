---
title: Windows Debugger WinDbg Overview
description: Explore the Windows Debugger (WinDbg), including general features and tool windows.
keywords: ["Overview of WinDbg's major features", "WinDbg", "Overview", "Windows Debugging"]
ms.date: 07/17/2025
ms.topic: concept-article
---

# What is WinDbg?

WinDbg is the latest version of the Windows Debugger that offers more modern visuals, faster windows, and a full-fledged scripting experience. WinDbug is built with the extensible debugger data model front and center.

> [!NOTE]
> WinDbg was previously released as **WinDbg Preview** in the Microsoft Store. WinDbg uses the same underlying engine as **WinDbg (Classic)**. It supports all the same commands, extensions, and workflows.

:::image type="content" source="images/windbgx-main-menu.png" border="false" alt-text="Screenshot of the main screen in WinDbg debugger.":::

## Access prominent features

Improve your debugging experience with the many features and programming benefits provided in WinDbg:

- **Connection setup and recall** - Save recent targets and session configurations. You can quickly restart saved items from the **File** menu.

    :::image type="content" source="images/windbgx-start-debugging-menu.png" border="false" alt-text="Screenshot of the start debugging screen in WinDbg debugger.":::

- **Dark theme** - Enable user interface (UI) preferences like dark theme under **File** > **Settings**.

   <!-- The following image shows a Microsoft email alias, DOMARS, which might be considered a security issue. -->

    :::image type="content" source="images/windbgx-dark-theme.png" border="false" alt-text="Screenshot of WinDbg debugger with dark theme enabled.":::

- **Keyboard navigation** - Use keyboard shortcuts like **Ctrl** + **Tab**, which lets you easily navigate between windows.

    :::image type="content" source="images/windbgx-ctrl-tab.gif" border="false" alt-text="Animation that shows how to use the Ctrl+Tab shortcut keys to navigate in WinDbg debugger.":::

- **Dump file processor detection** - Take advantage of autodetection for your processor architecture and quickly set up managed debugging.

- **Performance improvements** - Work with tool windows that load asynchronously and cancel them as needed. When you run a command, WinDbg can stop the loading of your locals, watch, or other windows.

## Start debugging

Get started debugging in WinDbg with the following features:

- **Integrated Time Travel Debugging (TTD)** - Select the **Record with Time Travel Debugging** option when you launch or attach to a process. WinDbg sets up TTD, starts recording, and opens the trace afterward.

    For more information, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).

    :::image type="content" source="images/windbgx-ttd.png" border="false" alt-text="Screenshot of the Process record dialog in WinDbg with a Notepad process selected for recording.":::

- **Launch App packages** - Debug your universal app or background task with a single mouse click.

    For more information, see [Launch App Package](./windbg-user-mode-preview.md#launch-app-package).

    :::image type="content" source="images/windbgx-launch-app-package.png" border="false" alt-text="Screenshot of the Launch App Package - Applications tab in WinDbg with 'cal' in the search box and three apps listed.":::

- **Attach to a process** - Use the Attach view to get a detailed summary of running processes, access easier configuration, and search support.

    :::image type="content" source="images/windbgx-attach-to-a-process-zoomed.png" border="false" alt-text="Screenshot of the Attach to a Process dialog in WinDbg debugger.":::

## Work with tool windows

Take advantage of the many improvements to the tool windows in WinDbg:

The **Command** window offers improved DML support, text highlighting, and search (including Regex).

:::image type="content" source="images/windbgx-highlighting.gif" border="false" alt-text="Animation that shows how to use the command window in WinDbg, including highlighting columns in yellow.":::

The **Source code** window provides syntax highlighting and other general improvements similar to most modern text editors.

:::image type="content" source="images/windbgx-source-window.png" border="false" alt-text="Screenshot of the Source code window in WinDbg debugger with syntax highlighting.":::

The **Disassembly** windows maintains the highlight on the current instruction as you scroll.

:::image type="content" source="images/windbgx-disassembly.png" border="false" alt-text="Screenshot of the Disassembly window in WinDbg debugger.":::

The **Breakpoints** window shows all your current breakpoints, a one-click toggle, and a hit count. For more information, see [WinDbg - Breakpoints](windbg-breakpoints-preview.md).

:::image type="content" source="images/windbgx-breakpoints-window.png" border="false" alt-text="Screenshot of the Breakpoint window in WinDbg debugger showing current breakpoints.":::

The **Scripting** window makes it easier for you to develop JavaScript and NatVis extensions, and use error highlighting and IntelliSense. For more information, see [WinDbg - Scripting](windbg-scripting-preview.md).

:::image type="content" source="images/windbgx-scripting-intellisense.png" alt-text="Screenshot of the Scripting window in WinDbg debugger with IntelliSense and error highlighting.":::

The **Data model** window provides an expandable and browsable version of the `dx` and `dx -g` commands. This feature helps you create powerful tables on-top of your NatVis, JavaScript, and LINQ queries. For more information, see [WinDbg - Data model](windbg-data-model-preview.md).

:::image type="content" source="images/windbgx-data-model-explore-window.png" border="false" alt-text="Screenshot of the data model window in WinDbg debugger with expandable and browsable features.":::

The **Locals** and **Watch** windows are both based off the data model used by the `dx` command. They benefit from the same features as other data model windows.

The **Memory** window has highlighting and improved scrolling.

The **Logs** feature provides an under-the-covers log of the WinDbg internals. You can view the logs for troubleshooting or to monitor long running commands.

## Explore WinDbg in action

Watch the following episodes of the [Defrag Tools](</shows/defrag-tools/>) show and see WinDbg in action:

- [Defrag Tools #182](/shows/defrag-tools/182-windbg-preview-part-1) - Tim, Chad, and Andy go over the basics of WinDbg and some of the features.
- [Defrag Tools #183](/shows/defrag-tools/183-windbg-preview-part-2) - Nick, Tim, and Chad use WinDbg and go through a quick demo.
- [Defrag Tools #184](/shows/defrag-tools/184-javascript-in-windbg-preview) - Bill and Andrew walk through the scripting features (JavaScript) in WinDbg.
- [Defrag Tools #185](/shows/defrag-tools/185-time-travel-debugging-introduction) - James and Ivette provide an introduction to Time Travel Debugging.
- [Defrag Tools #186](/shows/defrag-tools/186-time-travel-debugging-advanced) - James and JCAB cover advanced Time Travel Debugging.

## Install and configure WinDbg

Review the following article for information about installing and configuring WinDbg:

- [WinDbg – Command line startup options](windbg-command-line-preview.md)
- [WinDbg – Settings and workspaces](windbg-setup-preview.md)
- [WinDbg – Keyboard shortcuts](windbg-keyboard-shortcuts.md)

## Provide feedback

Your feedback helps the Microsoft team guide WinDbg's development and prioritize features.

To report bugs or suggest features, select **Feedback** in the ribbon to go to the [WinDbg-Feedback page](https://github.com/microsoft/WinDbg-Feedback/issues) on GitHub where you can file a new issue.

## Related articles

- [Release notes](windbg-release-notes.md)
- [WinDbg – Start a user-mode session](windbg-user-mode-preview.md)
- [WinDbg – Start a kernel mode session](windbg-kernel-mode-preview.md)
- [WinDbg blog archive](/archive/blogs/windbg/)
