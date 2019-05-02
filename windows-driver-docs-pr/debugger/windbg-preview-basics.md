---
title: WinDbg Preview Basics 
description: This section describes the basic capabilities of WinDbg preview debugger.
ms.date: 05/02/2019
ms.localizationpriority: medium
---

![Small logo on windbg preview](images/windbgx-preview-logo.png) 


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

WinDbg Preview has a scripting window for developing JavaScript, with error highlighting and IntelliSense.

For more information, see:

- [WinDbg Preview - Scripting](https://docs.microsoft.com/windows-hardware/drivers/debugger/windbg-scripting-preview)
- [JavaScript Debugger Scripting](https://docs.microsoft.com/windows-hardware/drivers/debugger/javascript-debugger-scripting)

The debugger team GitHub site -  https://github.com/Microsoft/WinDbg-Samples where they share the latest JavaScript (and C++) sample code.

![Screen shot of scripting menu in debugger](images/windbgx-scripting-intellisense.png)

## Time Travel Debugging (TTD) Basics

Time Travel Debugging, allows you to record an execution of your process running, then replay it later both forwards and backwards. 

For more information, see [Time Travel Debugging - Overview](https://docs.microsoft.com/windows-hardware/drivers/debugger/time-travel-debugging-overview).

To give time travel a try checkout the [Time Travel Debugging - Sample App Walkthrough](https://docs.microsoft.com/windows-hardware/drivers/debugger/time-travel-debugging-walkthrough).

![Screen shot of WinDbg Preview showing start recording checkbox](images/ttd-ribbon-buttons.png)

## TTD queries

You can use the data model to query time travel traces.  For more information, see [Introduction to Time Travel Debugging objects](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/time-travel-debugging-object-model).

For a tutorial on how to debug C++ code using TTD queries to find the problematic code, see:

 https://github.com/Microsoft/WinDbg-Samples/blob/master/TTDQueries/tutorial-instructions.md

All of the code used in the lab is available here: https://github.com/Microsoft/WinDbg-Samples/tree/master/TTDQueries/app-sample

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
