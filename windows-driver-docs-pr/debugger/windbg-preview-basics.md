---
title: WinDbg Preview Basics 
description: This section describes the basic capabilities of WinDbg preview debugger.
ms.date: 05/01/2019
ms.localizationpriority: medium
---

![Small logo on windbg preview](images/windbgx-preview-logo.png) 

# WinDbg Preview Basics 

WinDbg Preview is a brand-new version of WinDbg with more modern visuals, faster windows, a full-fledged scripting experience, built with the extensible debugger data model front and center. 

## What's new with WinDbg Preview 

For the latest information to see  https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugging-using-windbg-preview

## What's the debugger data model 

So probably https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/native-debugger-objects-in-natvis and https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/using-linq-with-the-debugger-objects


## Extending the data model 

https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/javascript-debugger-scripting

and our GitHub


## Time Travel Debugging (TTD) Basics 

https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/time-travel-debugging-walkthrough

	TTD queries - Link to https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/time-travel-debugging-object-model


## Major Features of WinDbg Preview

Here's some of the most notable things that have changed or are new.

![Main screen in debugger](images/windbgx-main-menu.png)


### Windowing improvements

- **Disassembly Window Improvements** - The disassembly window is also improved, the highlight of the current instruction remains where it is when you scroll. 

    ![Disassembly windows in Debugger](images/windbgx-disassembly.png)


For more information, see [WinDbg Preview - View menu](windbg-view-preview.md).

- **Command window** - Use the command window provides easy access to toggle DML and clear the debugger command window. All current debugger commands are compatible with and continue to work in WinDbg Preview.


### Dark theme 

Use **File** > **Settings** to enable the dark theme.

![Screen shot showing dark theme](images/windbgx-dark-theme.png)


### Ribbon Quick Access

Just pin the buttons you use the most and you can collapse the ribbon to save screen real estate. 
 
![Screen shot showing a ribon with pinned items](images/windbgx-quick-access.png)



### Highlighting

The command window has two new highlighting features. Selecting any text will give a subtle highlight to any other instances of that text. You can then hit "Highlight/Un-highlight" or Ctrl+Alt+H to persist the highlighting. 

![Screen shot showing columns highlighted in yellow](images/windbgx-highlighting.gif)


### Integrated Time Travel Debugging (TTD)

If you need a TTD trace of your application, just check the "Record process with Time Travel Debugging" box when launching or attaching. WinDbgNext will set it up for TTD and open the trace when you're done recording.

![Screen shot showing ctrl tab menu](images/windbgx-ttd.png)

For more information, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).


### Enhanced data model support

- **Built in data model support** - WinDbg Preview is written with built in data model support and the data model is available through out the debugger.
- **Model window** - The model window gives you an expandable and browsable version of ‘dx’ and ‘dx -g’, letting you create powerful tables on-top of your NatVis, JavaScript, and LINQ queries. 

For more information, see [WinDbg Preview - Data model](windbg-data-model-preview.md).

![Screen shot of data model menu in debugger](images/windbgx-data-model-menu.png)


### New scripting development UI 

- **Script development UI** - There is now a purpose built scripting window to make developing JavaScript and NatVis scripts easier, with error highlighting and IntelliSense.

![Screen shot of scripting menu in debugger](images/windbgx-scripting-intellisense.png)

For more information, see [WinDbg Preview - Scripting](windbg-scripting-preview.md).


## Videos

Watch these episodes of the [Defrag Tools](https://channel9.msdn.com/Shows/Defrag-Tools) show to see Windbg Preview in action.  
- [Defrag Tools #182](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-182-WinDbg-Preview-Part-1) - Tim, Chad, and Andy go over the basics of WinDbg Preview and some of the features.
- [Defrag Tools #183](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-183-WinDbg-Preview-Part-2) - Nick, Tim, and Chad use WinDbg Preview and go over a quick demo.
- [Defrag Tools #184](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-184-JavaScript-in-WinDbg-Preview) - Bill and Andrew walk through the scripting features in WinDbg Preview.
- [Defrag Tools #185](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-185-Time-Travel-Debugging-Introduction) - James and Ivette provide and introduction to Time Travel Debugging.
- [Defrag Tools #186](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-186-Time-Travel-Debugging-Advanced) - James and JCAB covers advanced Time Travel Debugging.

## Next Steps

For information on what's new in the most recent release, see [WinDbg Preview - What's New](windbg-what-is-new-preview.md).

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


--- 





