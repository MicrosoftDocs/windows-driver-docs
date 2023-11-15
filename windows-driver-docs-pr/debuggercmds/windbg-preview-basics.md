---
title: WinDbg Basics 
description: This section describes the basic capabilities of WinDbg debugger.
ms.date: 03/21/2022
---

# WinDbg Basics

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

| Title               | Description        |
| ------------------- | -------------------|
|[WinDbg - Release notes](./../debugger/debugging-using-windbg-preview.md)|What's new with WinDbg |

## The debugger data model

| Title               | Description        |
| ------------------- | -------------------|
| [dx command](./dx--display-visualizer-variables-.md) | Interactive command to display a debugger object model expression |
| [Using LINQ With the debugger objects](./../debugger/using-linq-with-the-debugger-objects.md) | SQL like query language |
| [Native Debugger Objects in NatVis](./../debugger/native-debugger-objects-in-natvis.md)| Using the objects with NatVis |
| [WinDbg - Data model](windbg-data-model-preview.md) | How to use the built in data model support in WinDbg |

## Extending the data model

| Title               | Description        |
| ------------------- | -------------------|
| [JavaScript Debugger Scripting](./../debugger/javascript-debugger-scripting.md) | How to use JavaScript to create scripts that understand debugger objects  |
| [WinDbg - Scripting](./windbg-scripting-preview.md) |Using the WinDbg built in scripting  |
| https://github.com/Microsoft/WinDbg-Samples |The debugger team GitHub site where they share the latest JavaScript (and C++) sample code. |
|[Native Debugger Objects in JavaScript Extensions](./../debugger/native-objects-in-javascript-extensions.md) | Describes how to work with common objects and provides reference information on their attributes and behaviors.|

## TTD Basics

| Title               | Description        |
| ------------------- | -------------------|
| [Time Travel Debugging - Overview](./time-travel-debugging-overview.md) | TTD Overview |
[Time Travel Debugging - Sample App Walkthrough](./time-travel-debugging-walkthrough.md) |  To give time travel a try checkout this tutorial |

## TTD queries
| Title               | Description        |
| ------------------- | -------------------|
| [Introduction to Time Travel Debugging objects](./time-travel-debugging-object-model.md). |You can use the data model to query time travel traces.  
|  https://github.com/Microsoft/WinDbg-Samples/blob/master/TTDQueries/tutorial-instructions.md |A tutorial on how to debug C++ code using TTD queries to find the problematic code |
| https://github.com/Microsoft/WinDbg-Samples/tree/master/TTDQueries/app-sample | All of the code used in the lab is available here.

## Videos

Watch these episodes of [Defrag Tools](/shows/defrag-tools) to see WinDbg in action.  

| Title               | Description        |
|-------------------- |--------------------|
| [Defrag Tools #182](/shows/defrag-tools/182-windbg-preview-part-1) |Tim, Chad, and Andy go over the basics of WinDbg and some of the features |
| [Defrag Tools #183](/shows/defrag-tools/183-windbg-preview-part-2) | Nick, Tim, and Chad use WinDbg and go over a quick demo |
| [Defrag Tools #184](/shows/defrag-tools/184-javascript-in-windbg-preview) | Bill and Andrew walk through the scripting features in WinDbg |
| [Defrag Tools #185](/shows/defrag-tools/185-time-travel-debugging-introduction) | James and Ivette provide and introduction to Time Travel Debugging |
| [Defrag Tools #186](/shows/defrag-tools/186-time-travel-debugging-advanced) | James and JCAB covers advanced Time Travel Debugging |

## Installation and getting connected

| Title                                                                 | Description             |
|-----------------------------------------------------------------------|-------------------------|
| [WinDbg – Installation](index.md)                                     | Installation directions |
| [WinDbg – Start a user-mode session](windbg-user-mode-preview.md)     | User Mode               |
| [WinDbg – Start a kernel mode session](windbg-kernel-mode-preview.md) | Kernel Mode             |
