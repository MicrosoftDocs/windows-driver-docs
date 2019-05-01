---
title: WinDbg Preview Basics 
description: This section describes the basic capabilities of WinDbg preview debugger.
ms.date: 05/01/2019
ms.localizationpriority: medium
---

![Small logo on windbg preview](images/windbgx-preview-logo.png) 

# WinDbg Preview Basics 

WinDbg Preview is a new version of WinDbg with more modern visuals, faster windows, a full-fledged scripting experience, built with the extensible debugger data model front and center. WinDbg supports low levels of kernel debugging not currently possible using Visual Studio.

## What's new with WinDbg Preview 

For the latest information on what's new, see [WinDbg Preview - What's New](https://docs.microsoft.com/windows-hardware/drivers/debugger/debugging-using-windbg-preview)

## The debugger data model

The debugger data model is an extensible object model that is central to the way in which new debugger extensions (including those in JavaScript, NatVis, and C++) both consume information from the debugger and produce information that can be accessed from the debugger.

You can use the [dx command](https://docs.microsoft.com/windows-hardware/drivers/debugger/dx--display-visualizer-variables-) to display a debugger object model expression and you can work with the
[Native Debugger Objects in NatVis](https://docs.microsoft.com/windows-hardware/drivers/debugger/native-debugger-objects-in-natvis). 

You can also learn about [Using LINQ With the debugger objects](https://docs.microsoft.com/windows-hardware/drivers/debugger/using-linq-with-the-debugger-objects).

You can use the built in data model support in WinDbg Preview, see [WinDbg Preview - Data model](windbg-data-model-preview.md).

![Screen shot of data model menu in debugger](images/windbgx-data-model-menu.png)


## Extending the data model

WinDbg Preview has a scripting window to make developing JavaScript scripts easier, with error highlighting and IntelliSense.

For more information, see:

- [WinDbg Preview - Scripting](https://docs.microsoft.com/windows-hardware/drivers/debugger/windbg-scripting-preview)
- [JavaScript Debugger Scripting](https://docs.microsoft.com/windows-hardware/drivers/debugger/javascript-debugger-scripting)

The debugger team GitHub site -  https://github.com/Microsoft/WinDbg-Samples where they share the latest JavaScript (and C++) sample code.

![Screen shot of scripting menu in debugger](images/windbgx-scripting-intellisense.png)

## Time Travel Debugging (TTD) Basics

Time Travel Debugging, allows you to record an execution of your process running, then replay it later both forwards and backwards. Time Travel Debugging (TTD) can help you debug issues easier by letting you "rewind" your debugger session, instead of having to reproduce the issue until you find the bug.

For more information, see [Time Travel Debugging - Overview](https://docs.microsoft.com/windows-hardware/drivers/debugger/time-travel-debugging-overview).

To give time travel a try checkout the [Time Travel Debugging - Sample App Walkthrough](https://docs.microsoft.com/windows-hardware/drivers/debugger/time-travel-debugging-walkthrough).

![Screen shot of WinDbg Preview showing start recording checkbox](images/ttd-ribbon-buttons.png)

## TTD queries

Using the data model to query time travel traces is a powerful tool to answer questions like these.
- At what point in time in the trace did a specific code module load?
- When were threads created/terminated in the trace?
- What are the longest running threads in the trace?

For more information, see [Introduction to Time Travel Debugging objects](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/time-travel-debugging-object-model).

For a tutorial on how to debug C++ code using TTD queries to find the problematic code, see:

 https://github.com/Microsoft/WinDbg-Samples/blob/master/TTDQueries/tutorial-instructions.md

All of the code used in the lab is available here: https://github.com/Microsoft/WinDbg-Samples/tree/master/TTDQueries/app-sample



## WinDbg Preview Quick Tips

### Dark theme 

Use **File** > **Settings** to enable the dark theme.

![Screen shot showing dark theme](images/windbgx-dark-theme.png)

### Highlighting

The command window has two new highlighting features. Selecting any text will give a subtle highlight to any other instances of that text. You can then hit "Highlight/Un-highlight" or Ctrl+Alt+H to persist the highlighting. 

![Screen shot showing columns highlighted in yellow](images/windbgx-highlighting.gif)

### Ribbon Quick Access

Just pin the buttons you use the most and you can collapse the ribbon to save screen real estate. 
 
![Screen shot showing a ribon with pinned items](images/windbgx-quick-access.png)


### Disassembly Window Scrolling

Highlights the current instruction and it remains where it is when you scroll.

![Disassembly windows in Debugger](images/windbgx-disassembly.png)

## Videos

Watch these episodes of [Defrag Tools](https://channel9.msdn.com/Shows/Defrag-Tools) to see Windbg Preview in action.  
- [Defrag Tools #182](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-182-WinDbg-Preview-Part-1) - Tim, Chad, and Andy go over the basics of WinDbg Preview and some of the features.
- [Defrag Tools #183](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-183-WinDbg-Preview-Part-2) - Nick, Tim, and Chad use WinDbg Preview and go over a quick demo.
- [Defrag Tools #184](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-184-JavaScript-in-WinDbg-Preview) - Bill and Andrew walk through the scripting features in WinDbg Preview.
- [Defrag Tools #185](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-185-Time-Travel-Debugging-Introduction) - James and Ivette provide and introduction to Time Travel Debugging.
- [Defrag Tools #186](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-186-Time-Travel-Debugging-Advanced) - James and JCAB covers advanced Time Travel Debugging.


## Next Steps

To install, see [WinDbg Preview – Installation](windbg-install-preview.md)

To get connected to the environment that you want to debug see [WinDbg Preview – Start a user-mode session](windbg-user-mode-preview.md) and [WinDbg Preview – Start a kernel mode session](windbg-kernel-mode-preview.md).

![Main screen in debugger](images/windbgx-main-menu.png)

