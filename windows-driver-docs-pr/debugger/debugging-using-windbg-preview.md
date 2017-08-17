---
title: Debugging Using WinDbg Preview
description: This section describes how to perform basic debugging tasks using the WinDbg preview debugger.
ms.author: windowsdriverdev
ms.date: 08/17/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Debugging Using WinDbg Preview 

WinDbg Preview is a brand new version of WinDbg with more modern visuals, more performant windows, a full-fledged scripting experience, built with the extensible debugger data model front and center. WinDbg Preview is using the same underlying engine as WinDbg today, so all the commands, extensions, and workflows you're used to will still work as they did before.

For information on what's new in the most recent release, see [WinDbg Preview - What's New](windbg-what-is-new-preview.md).

For the latest news, tips, and tricks from the debugger dev team, refer to the debugger tools team blog.
[https://blogs.msdn.microsoft.com/windbg/](https://blogs.msdn.microsoft.com/windbg/)


Review these topics to install and configure WinDbg Preview.

- [WinDbg Preview – Installation](windbg-install-preview.md)
- [WinDbg Preview – Command line startup options](windbg-command-line-preview.md)
- [WinDbg Preview – Settings and workspaces](windbg-setup-preview.md)
- [WinDbg Preview – Keyboard shortcuts](windbg-keyboard-shortcuts-preview.md)

These topics describe how to get connected to the environment that you want to debug. 

- [WinDbg Preview – Start a user-mode session](windbg-user-mode-preview.md)
- [WinDbg Preview – Start a kernel mode session](windbg-kernel-mode-preview.md)

These topics describe some common tasks, organized by the menu tabs.

- [WinDbg Preview – File menu](windbg-file-preview.md)
- [WinDbg Preview – Home menu](windbg-home-preview.md)
- [WinDbg Preview – View menu](windbg-view-preview.md)
- [WinDbg Preview – Breakpoints](windbg-breakpoints-preview.md)
- [WinDbg Preview – Data model](windbg-data-model-preview.md)
- [WinDbg Preview – Scripting](windbg-scripting-preview.md)


## <span id="providingfeedback"></span>Providing feedback

Your feedback will help guide WinDbg's development going forward. 

- If you have feedback such as a feature that you really want to see or a bug that makes something difficult, use the Feedback Hub.

![Screen shot of feedback hub showing feedback options including the add new feedback button](images/windbgx-feedback.png)


## Major Features of WinDbg Preview

Here's some of the most notable things that have changed or are new.

![Main screen in debugger](images/windbgx-main-menu.png)


### Backwards compatibility 

Because the underling debugger engine is the same, all of the previous debugger commands and debugger extensions continue to work.

### General features
- **Easier Connection Setup and Recall** - The WinDbg Preview includes the ability to recall previous session configuration information.

![Screen shot of main screen in debugger](images/windbgx-start-debugging-menu.png)

- **Easy feedback channel** - Your feedback will guide the development effort going forward. For more information, see [Providing Feedback](#providing-feedback)
- **Dump file processor detection** -Auto-detects processor architecture for easier managed debugging.
- **Performance Improvements** Windows now load asynchronously and can be canceled - When you run another command, WinDbg Preview will stop the loading of your locals, watch, or other windows.


### Windowing improvements

- **Disassembly Window Improvements** - The disassembly window is also improved, the highlight of the current instruction remains where it is when you scroll. 
- **Memory window improvements** - The memory window has highlighting and improved scrolling.
- **Locals and watch data model visualization** - The locals and watch windows are both based off of the data model that is used by the dx command. This means the locals and watch windows will benefit from any NatVis or JavaScript extensions you have loaded, and can even support full LINQ queries, just like the dx command. 
- **Logs** - This is a under the covers log of the WinDbg Preview internals. It can be viewed for troubleshooting or to monitor long running processes. 

For more information, see [WinDbg Preview - View menu](windbg-view-preview.md).

![View menu in debugger](images/windbgx-view-menu.png)

- **Command window** - Use the command window provides easy access to toggle DML and clear the debugger command window. All current debugger commands are compatible with and continue to work in WinDbg Preview.
- **Source window** - Use the source windows to work with source code files, the new source windows should look more similar to the source windows you're used to seeing in every other modern editor.

### Enhanced breakpoint tracking  

- **Enable/Disable breakpoints** - The breakpoints window shows all your current breakpoints and provides easy access to enabling and disabling them. 
- **Hit count** - The breakpoint window keep a running total of each time the breakpoint is hit.

For more information, see [Breakpoints](windbg-breakpoints-preview.md).


### Enhanced data model support

- **Built in data model support** - WinDbg Preview is written with built in data model support and the data model is available through out the debugger.
- **Model window** - The model window gives you an expandable and browsable version of ‘dx’ and ‘dx -g’, letting you create powerful tables on-top of your NatVis, JavaScript, and LINQ queries. 

For more information, see [WinDbg Preview - Data model](windbg-data-model-preview.md).

![Screen shot of data model menu in debugger](images/windbgx-data-model-menu.png)


### New Scripting development UI 

- **Script development UI** - There is now a purpose built scripting window to make developing JavaScript and NatVis scripts easier, with error highlighting and IntelliSense.

For more information, see [WinDbg Preview - Scripting](windbg-scripting-preview.md).

![Screen shot of scripting menu in debugger](images/windbgx-scripting-menu.png)


--- 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




