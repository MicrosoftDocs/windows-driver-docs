---
title: Time Travel Debugging - Overview
description: This section describes time travel debugging.
ms.author: domars
ms.date: 09/18/2017
ms.localizationpriority: medium
---

![Small time travel logo showing clock](images/ttd-time-travel-debugging-logo.png) 

# Time Travel Debugging - Overview


## What is Time Travel Debugging?

Time Travel Debugging, is a tool that allows you to record an execution of your process running, then replay it later both forwards and backwards. Time Travel Debugging (TTD) can help you debug issues easier by letting you "rewind" your debugger session, instead of having to reproduce the issue until you find the bug. 
 
TTD allows you to go back in time to better understand the conditions that lead up to the bug and replay it multiple times to learn how best to fix the problem. 

TTD can have advantages over crash dump files, which often are missing the code execution that led up to the ultimate failure.  

In the event you can't figure out the issue yourself, you can share the trace with a co-worker and they can look at exactly what you're looking at. This can allow for easier collaboration than live debugging, as the recorded instructions are the same, where the address locations and code execution will be different on different PCs. You can also share a specific point in time to help your co-worker figure out where to start. 

TTD is efficient and works to add as little as possible overhead as it captures code execution in trace files.  

TTD includes a set of debugger data model objects to allow you to query the trace using LINQ. For example, you can use TTD objects to locate when a specific code module was loaded or locate all of the exceptions. 

![Example screen shot of WinDbg preview showing time travel command and cdog app](images/ttd-windbgx-screen-shot-example-cdog-app.png)

##  Comparison of Debugging Tools

This table summarizes the pros and cons of the different debugging solutions available.


|          Approach           |                                                      Pros                                                       |                                                                                                               Cons                                                                                                                |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       Live debugging        |   Interactive experience, sees flow of execution, can change target state, familiar tool in familiar setting.   | Disrupts the user experience, may require effort to reproduce the issue repeatedly, may impact security, not always an option on production systems.  With repro difficult to work back from point of failure to determine cause. |
|            Dumps            |                            No coding upfront, low-intrusiveness, based on triggers.                             |                                                          Successive snapshot or live dumps provide a simple “over time” view. Overhead is essentially zero if not used.                                                           |
|      Telemetry & logs       |            Lightweight, often tied to business scenarios / user actions, machine learning friendly.             |                                                         Issues arise in unexpected code paths (with no telemetry). Lack of data depth, statically compiled into the code.                                                         |
| Time Travel Debugging (TTD) | Great at complex bugs, no coding upfront, offline repeatable debugging, analysis friendly, captures everything. |                                                                 Large overhead at record time. May collect more data that is needed. Data files can become large.                                                                 |

## TTD Availability 

TTD is available on Windows 10 after installing the WinDbg Preview app from the Store.  WinDbg Preview is a brand-new version of WinDbg with more modern visuals, faster windows, a full-fledged scripting experience, with built in support for the extensible debugger data model. For more information on downloading WinDbg Preview from the store, see [Debugging Using WinDbg Preview](debugging-using-windbg-preview.md).


## Trace file basics 

### Trace file size

The trace file can get big and the user of TTD needs to make sure that there is adequate free space available. If you record a program for even a few minutes, the trace files can quickly grow to be several gigabytes. TTD does not set a maximum size of trace files to allow for complex long running scenarios. Quickly re-creating the issue, will keep the trace file size as small as possible.

### Trace and index files

A trace (.RUN) file stores the code execution during recording. 

Once the recording is stopped, an index (.IDX) file is created to allow for faster access to the trace information. Index files are also created automatically when WinDbg Preview opens the trace file.

Index files can also be large, typically twice as large as the trace file.  

You can recreate the index file from the trace file using the !tt.index command.

```dbgcmd
0:000> !tt.index
Successfully created the index in 10ms.
```

Recording errors and other recording output is written to a WinDbg log file.

All of the output files are stored in a location configured by the user. The default location is in the users document folder. For example, for User1 the TTD files would be stored here:

```console
C:\Users\User1\Documents
```

For more information on working the trace files, see [Time Travel Debugging - Working with trace files](time-travel-debugging-trace-file-information.md).

## Getting started with TTD

Review these topics to record and replay a trace file as well as for information on working with trace files and troubleshooting.

- [Time Travel Debugging - Record a trace](time-travel-debugging-record.md)
- [Time Travel Debugging - Replay a trace](time-travel-debugging-replay.md)
- [Time Travel Debugging - Working with trace files](time-travel-debugging-trace-file-information.md)
- [Time Travel Debugging - Troubleshooting](time-travel-debugging-troubleshooting.md)
- [Time Travel Debugging - Sample App Walkthrough](time-travel-debugging-walkthrough.md)

These topics describe additional advanced functionality in time travel debugging. 

- [Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)
- [Time Travel Debugging - JavaScript Automation](time-travel-debugging-javascript-automation.md)


## Things to look out for 

### Anti-virus incompatibilities 

You may encounter incompatibilities because of how TTD hooks into process to record them. Typically issues arise with anti-virus or other system software that is attempting to track and shadow system memory calls. If you run into issues of with recording, such as an insufficient permission message, try temporarily disabling any anti-virus software.  

Other utilities that attempt to block memory access, can also be problematic, for example, the Microsoft Enhanced Mitigation Experience Toolkit. For more information about EMET, see [The Enhanced Mitigation Experience Toolkit](https://support.microsoft.com/help/2458544/the-enhanced-mitigation-experience-toolkit).

Another example of an environment that conflicts with TTD, would be the electron application framework. In this case the trace may record, but a deadlock or crash of the process being recorded is also possible.

### User mode only

TTD currently supports only user mode operation, so tracing a kernel mode process is not possible. 

### Read-only playback

You can travel back in time, but you can't change history. You can use read memory commands, but you can't use commands that modify or write to memory.

### System Protected Processes

Some Windows system protected processes, such as Protected Process Light (PPL) process are protected, so the TTD cannot inject itself into the protected process to allow for the recording of the code execution.

### Trace file errors

There are some cases where trace file errors can occur. For more information, see [Time Travel Debugging - Troubleshooting](time-travel-debugging-troubleshooting.md).


## Advanced Features of Time Travel Debugging

Here's some of the most notable TTD advanced features.

### Debugger data model support

- **Built in data model support** - TTD includes data model support. Using LINQ queries to analyze application failures can be a powerful tool. You can use the data model window in WinDbg  Preview to work with an expandable and browsable version of ‘dx’ and ‘dx -g’, letting you create tables using NatVis, JavaScript, and LINQ queries. 

For general information about the debugger data model, see [WinDbg Preview - Data model](windbg-data-model-preview.md). For information about working with the TTD debugger object model, see [Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md).

### Scripting support  

- **Scripting Automation** - Scripting support for JavaScript and NatVis allows for the automation of problem investigation. For more information, see 
[Time Travel Debugging - JavaScript Automation](time-travel-debugging-javascript-automation.md).

For general information about working with JavaScript and NatVis, see [WinDbg Preview - Scripting](windbg-scripting-preview.md).


## <span id="providingfeedback"></span>Providing feedback

Your feedback will help guide time travel development priorities going forward. 

- If you have feedback such as a feature that you really want to see or a bug that makes something difficult, use the Feedback Hub.

![Screen shot of feedback hub showing feedback options including the add new feedback button](images/windbgx-feedback.png)


## TTD Latest News

For the latest news, tips, and tricks from the debugger dev team, refer to the debugger tools team blog.
[https://blogs.msdn.microsoft.com/windbg/](https://blogs.msdn.microsoft.com/windbg/)


--- 





