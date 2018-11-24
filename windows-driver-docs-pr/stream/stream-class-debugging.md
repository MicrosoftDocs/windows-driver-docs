---
title: Stream Class Debugging
description: Stream Class Debugging
ms.assetid: 544b922b-58e4-4cbb-a76c-d8e13ae17e55
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , debugging
- streaming minidrivers WDK Windows 2000 Kernel , debugging
- minidrivers WDK Windows 2000 Kernel Streaming , debugging
- debugging stream class minidrivers WDK Windows 2000 Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stream Class Debugging





Use the checked (debug) version of *stream.sys* to print out informative messages about the status of the minidriver and ASSERT when errors in the minidriver are encountered.

The following, additional tips can be used when debugging stream class minidrivers:

-   When debugging with the wdeb386 debugger (or with Softice) on Windows Me systems, debugging information is available by breaking into the debugger, typing .NTKERN, and then selecting option D. This displays the debug log, which shows entries in chronological order. When debugging with Windows 2000, the debug information is printed to the debug terminal in real time.

-   To adjust the output level of the debugger, load *stream.sys* symbols (*stream.sym* for Windows Me and *stream.sys* for Windows 2000) and modify the *StreamDebug* variable with "e StreamDebug *xx*". The default is 00, which prints only severe errors. Set it to FF to print all messages.

-   Minidrivers can print their own messages, using *stream.sys* facilities previously described, by calling [**StreamClassDebugPrint**](https://msdn.microsoft.com/library/windows/hardware/ff568235). Note that the output level as previously described must be set to be greater than or equal to the output level chosen in the call.

 

 




