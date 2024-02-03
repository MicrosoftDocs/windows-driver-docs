---
title: WinDbg Overview
description: This section is an overview of WinDbg's major features.
keywords: ["Overview of WinDbg's major features", "WinDbg", "Overview", "Windows Debugging"]
ms.date: 04/10/2023
---

# What is WinDbg?

WinDbg is the latest version of WinDbg with more modern visuals, faster windows, a full-fledged scripting experience, built with the extensible debugger data model front and center.

> [!NOTE]
> Formerly released as *WinDbg Preview* in the Microsoft Store, *WinDbg* leverages the same underlying engine as *WinDbg (Classic)* and supports all the same commands, extensions, and workflows.

:::image type="content" source="images/windbgx-main-menu.png" alt-text="Screenshot of the main screen in WinDbg debugger.":::

## General features

- **Connection setup and recall** - Recent targets and session configurations are saved. They can be quickly restarted from the file menu.

    :::image type="content" source="images/windbgx-start-debugging-menu.png" alt-text="Screenshot of the start debugging menu in WinDbg debugger.":::

- **Dark theme** - Go to File > Settings to enable the dark theme.

    :::image type="content" source="images/windbgx-dark-theme.png" alt-text="Screenshot of WinDbg debugger with dark theme enabled.":::

- **Keyboard navigation** - Use Ctrl+Tab to easily navigate between windows with just your keyboard.

    :::image type="content" source="images/windbgx-ctrl-tab.gif" alt-text="Screenshot demonstrating the Ctrl+Tab menu in WinDbg debugger.":::

- **Dump file processor detection** - Autodetects processor architecture for easier managed debugging.

- **Performance improvements** - Tool windows load asynchronously and can be canceled. When you run a command, WinDbg can stop the loading of your locals, watch, or other windows.

## Start debugging view

- **Integrated Time Travel Debugging (TTD)** - Use the "Record with Time Travel Debugging" checkbox when launching or attaching to a process. WinDbg will set up TTD, start recording, and open the trace afterwards.

    For more information, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).

    :::image type="content" source="images/windbgx-ttd.png" alt-text="Screenshot of the process record menu in WinDbg with a Notepad process selected for recording.":::

- **Launch App packages** - Debug your universal app or background task in a single click.

    For more information, see [Launch App Package](./windbg-user-mode-preview.md#launch-app-package).

    :::image type="content" source="images/windbgx-launch-app-package.png" alt-text="Screenshot of the Launch App Package Applications tab in WinDbg with 'cal' in the search box and three apps listed.":::

- **Attach to a process** - The new attach view provides a detailed view of running processes, easier configuration, and search support.

    :::image type="content" source="images/windbgx-attach-to-a-process-zoomed.png" alt-text="Screenshot of the Attach to a Process dialog in WinDbg debugger.":::

## Improved tool windows

- **Command** - The command window has improved DML support, text highlighting, search (including Regex).

    :::image type="content" source="images/windbgx-highlighting.gif" alt-text="Screenshot of the command window in WinDbg with columns highlighted in yellow.":::

- **Source** - The source code window provides syntax highlighting and other general improvements similar to most modern text editors.

    :::image type="content" source="images/windbgx-source-window.png" alt-text="Screenshot of the source code window in WinDbg debugger with syntax highlighting.":::

- **Disassembly** - The disassembly window is also improved, the highlight of the current instruction remains where it's when you scroll.

    :::image type="content" source="images/windbgx-disassembly.png" alt-text="Screenshot of the disassembly window in WinDbg debugger.":::

- **Breakpoints** - The breakpoints window shows all your current breakpoints, a one-click toggle, and a hit count.

    For more information, see [Breakpoints](windbg-breakpoints-preview.md).

    :::image type="content" source="images/windbgx-breakpoints-window.png" alt-text="Screenshot of the breakpoint window in WinDbg debugger showing current breakpoints.":::

- **Scripting** - The new scripting window makes developing JavaScript and NatVis extensions easier, with error highlighting and IntelliSense.

    For more information, see [WinDbg - Scripting](windbg-scripting-preview.md).

    :::image type="content" source="images/windbgx-scripting-intellisense.png" alt-text="Screenshot of the scripting window in WinDbg debugger with IntelliSense and error highlighting.":::

- **Data model** - The model window provides an expandable and browsable version of `dx` and `dx -g`, letting you create powerful tables on-top of your NatVis, JavaScript, and LINQ queries.

    For more information, see [WinDbg - Data model](windbg-data-model-preview.md).

    :::image type="content" source="images/windbgx-data-model-explore-window.png" alt-text="Screenshot of the data model window in WinDbg debugger with expandable and browsable features.":::

- **Locals and watch** - The locals and watch windows are both based off the data model that is used by the `dx` command. This means they benefit from the same features as other data model windows.

- **Memory** - The memory window has highlighting and improved scrolling.

- **Logs** - This is an under the covers log of the WinDbg internals. It can be viewed for troubleshooting or to monitor long running commands.

## Providing feedback

Your feedback helps our team guide WinDbg's development and prioritize features.

To report any bugs or suggest a new feature, you can follow the feedback button in the ribbon to go to the [GitHub page](https://aka.ms/windbg/feedback) where you can file a new issue.

## Other resources

- For information on what's new in the most recent release, see [Release notes](windbg-release-notes.md).

- Review these topics to install and configure WinDbg:
  - [WinDbg – Command line startup options](windbg-command-line-preview.md)
  - [WinDbg – Settings and workspaces](windbg-setup-preview.md)
  - [WinDbg – Keyboard shortcuts](windbg-keyboard-shortcuts-preview.md)

- These topics describe how to get connected to the environment that you want to debug:
  - [WinDbg – Start a user-mode session](windbg-user-mode-preview.md)
  - [WinDbg – Start a kernel mode session](windbg-kernel-mode-preview.md)

- Watch these episodes of the [Defrag Tools](</shows/defrag-tools/>) show to see WinDbg in action:
  - [Defrag Tools #182](/shows/defrag-tools/182-windbg-preview-part-1) - Tim, Chad, and Andy go over the basics of WinDbg and some of the features.
  - [Defrag Tools #183](/shows/defrag-tools/183-windbg-preview-part-2) - Nick, Tim, and Chad use WinDbg and go over a quick demo.
  - [Defrag Tools #184](/shows/defrag-tools/184-javascript-in-windbg-preview) - Bill and Andrew walk-through the scripting features in WinDbg.
  - [Defrag Tools #185](/shows/defrag-tools/185-time-travel-debugging-introduction) - James and Ivette provide and introduction to Time Travel Debugging.
  - [Defrag Tools #186](/shows/defrag-tools/186-time-travel-debugging-advanced) - James and JCAB covers advanced Time Travel Debugging.

- Additional tips and tricks can be found in the [WinDbg blog archive](/archive/blogs/windbg/).
