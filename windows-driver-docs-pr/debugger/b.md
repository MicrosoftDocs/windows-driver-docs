---
title: B (Windows Debugger Glossary)
description: Glossary page - B
Robots: noindex, nofollow
ms.assetid: 5ba110fc-1a12-4cbd-adc9-ef9441e257cb
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# B


<span id="blue_screen"></span><span id="BLUE_SCREEN"></span>**blue screen**  
The blue character-mode screen displayed after a bug check occurs.

<span id="breakpoint"></span><span id="BREAKPOINT"></span>**breakpoint**  
A location in the target or a target operation which will cause an event when triggered.

For more information, see [Using Breakpoints](using-breakpoints.md).

<span id="breakpoint_id"></span><span id="BREAKPOINT_ID"></span>**breakpoint ID**  
The unique identifier for a breakpoint.

For more information, see [Using Breakpoints](using-breakpoints.md).

<span id="breakpoint_type"></span><span id="BREAKPOINT_TYPE"></span>**breakpoint type**  
The method used to implement the breakpoint. There are two types of breakpoints: processor breakpoints and software breakpoints.

<span id="break_status"></span><span id="BREAK_STATUS"></span>**break status**  
A setting that influences how the debugger engine proceeds after an event. The break status indicates whether the event should break into the debugger, have a notification printed to the debugger console, or be ignored. The break status is part of an event filter.

See also [*handling status*](h.md#handling-status).

For more information, see the topics [Controlling Exceptions and Events](controlling-exceptions-and-events.md) and [Event Filters](event-filters.md).

<span id="bug_check"></span><span id="BUG_CHECK"></span>**bug check**  
When Windows encounters hardware problems, inconsistencies within data necessary for its operation, or other severe errors, it shuts down and displays error information on a blue character-mode screen.

This shutdown is known variously as a bug check, kernel error, system crash, stop error, or, occasionally, trap. The screen display itself is referred to as a blue screen or stop screen. The most important information shown on the screen is a message code which gives information about the crash; this is known as a bug check code or stop code.

WinDbg or KD can configure the system so that a debugger is automatically contacted when such an error occurs. Alternatively, the system can be instructed to automatically reboot in case of such an error.

For more information, see [Bug Checks (Blue Screens)](bug-checks--blue-screens-.md).

<span id="bug_check_code"></span><span id="BUG_CHECK_CODE"></span>**bug check code**  
The hexadecimal code indicating a specific type of bug check .

 

 





