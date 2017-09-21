---
title: Introduction to Time Travel Debugging objects
description: This section describes the debugger model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Introduction to Time Travel Debugging objects
There are two debugger extensions that add TTD data two the debugger object model: TTDExt and TTDAnalyze. The model objects can be accessed through `dx`, WinDbg Preview's model windows, and JavaScript. Both of these extensions are automatically loaded when debugging a time travel trace.

## TTDExt.dll
The primary objects added by TTDExt can be found in the *TTD* namespace off of any *Process* object. For example, `@$curprocess.TTD`.

### Children
| Object | Description |
| --- | --- |
| Lifetime | A [TTD range object](time-travel-debugging-range-objects.md) describing the lifetime of the entire trace. |
| Threads | Contains a collection of [TTD thread objects](time-travel-debugging-thread-objects.md), one for every thread throughout the lifetime of the trace. |
| Events | Contains a collection of [TTD event objects](time-travel-debugging-event-objects.md), one for every event in the trace. |

### Methods
| Method | Description |
| --- | --- |
| SetPosition() | Takes an integer between 0 and 100 or string as input and jumps the trace to that location. |

## TTDAnalyze.dll
The primary objects added by TTDAnalyze can be found in the *TTD* namespace off of any *Session* object. For example, `@$cursession.TTD`.

### Children
| Objects | Description |
| --- | --- |
| Data | TODO|
| Utility | TODO |

### Methods
| Method | Description |
| --- | --- |
| Calls() | TODO|

## See Also
TODO
