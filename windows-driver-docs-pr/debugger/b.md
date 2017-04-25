---
title: B
description: Glossary page
Robots: noindex, nofollow
ms.assetid: 5ba110fc-1a12-4cbd-adc9-ef9441e257cb
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20B%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




