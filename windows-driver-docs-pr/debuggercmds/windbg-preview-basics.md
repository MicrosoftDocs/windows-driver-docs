---
title: "WinDbg Basics"
description: "This article describes the basic capabilities of WinDbg debugger."
keywords: ["Summary", "WinDbg", "basic capabilities of WinDbg", "Windows Debugging"]
ms.date: 03/21/2022
ms.topic: overview
---

# WinDbg basics

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

| Title               | Description        |
| ------------------- | -------------------|
|[WinDbg: Release notes](./../debugger/debugging-using-windbg-preview.md)|What's new with WinDbg. |

## The debugger data model

| Title               | Description        |
| ------------------- | -------------------|
| [dx command](./dx--display-visualizer-variables-.md) | Use this interactive command to display a debugger object model expression. |
| [Using LINQ With the debugger objects](./../debugger/using-linq-with-the-debugger-objects.md) | Use a SQL-like query language. |
| [Native debugger objects in NatVis](./../debugger/native-debugger-objects-in-natvis.md)| Use the objects with NatVis. |
| [WinDbg: Data model](windbg-data-model-preview.md) | Use the built-in data model support in WinDbg. |

## Extend the data model

| Title               | Description        |
| ------------------- | -------------------|
| [JavaScript debugger scripting](./../debugger/javascript-debugger-scripting.md) | Use JavaScript to create scripts that understand debugger objects.  |
| [WinDbg: Scripting](./windbg-scripting-preview.md) | Use the WinDbg built-in scripting.  |
| https://github.com/Microsoft/WinDbg-Samples | Access the debugger team GitHub site where they share the latest JavaScript (and C++) sample code. |
|[Native debugger objects in JavaScript extensions](./../debugger/native-objects-in-javascript-extensions.md) | Learn how to work with common objects and gain reference information on their attributes and behaviors.|

## TTD basics

| Title               | Description        |
| ------------------- | -------------------|
| [Time Travel Debugging: Overview](./time-travel-debugging-overview.md) | Time Travel Debugging (TTD) overview. |
[Time Travel Debugging: Sample app walkthrough](./time-travel-debugging-walkthrough.md) | Time travel tutorial. |

## TTD queries

| Title               | Description        |
| ------------------- | -------------------|
| [Introduction to Time Travel Debugging objects](./time-travel-debugging-object-model.md). | The data model used to query time travel traces.
|  https://github.com/Microsoft/WinDbg-Samples/blob/master/TTDQueries/tutorial-instructions.md | A tutorial on how to debug C++ code by using TTD queries to find the problematic code. |
| https://github.com/Microsoft/WinDbg-Samples/tree/master/TTDQueries/app-sample | All the code used in the lab is available here.

## Videos

Watch these episodes of [Defrag Tools](/shows/defrag-tools) to see WinDbg in action.

| Title               | Description        |
|-------------------- |--------------------|
| [Defrag Tools #182](/shows/defrag-tools/182-windbg-preview-part-1) |Tim, Chad, and Andy go over the basics of WinDbg and some of the features. |
| [Defrag Tools #183](/shows/defrag-tools/183-windbg-preview-part-2) | Nick, Tim, and Chad use WinDbg and go over a quick demo. |
| [Defrag Tools #184](/shows/defrag-tools/184-javascript-in-windbg-preview) | Bill and Andrew walk through the scripting features in WinDbg. |
| [Defrag Tools #185](/shows/defrag-tools/185-time-travel-debugging-introduction) | James and Ivette introduce TTD. |
| [Defrag Tools #186](/shows/defrag-tools/186-time-travel-debugging-advanced) | James and JCAB cover advanced TTD. |

## Installation and connection

| Title                                                                 | Description             |
|-----------------------------------------------------------------------|-------------------------|
| [WinDbg: Installation](index.md)                                     | Installation directions |
| [WinDbg: Start a user-mode session](windbg-user-mode-preview.md)     | User mode               |
| [WinDbg: Start a kernel mode session](windbg-kernel-mode-preview.md) | Kernel mode             |