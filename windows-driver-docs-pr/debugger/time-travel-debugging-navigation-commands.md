---
title: time travel navigation commands
description: This section describes the time travel navigation commands.
ms.author: windowsdriverdev
ms.date: 09/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time travel navigation commands

This section describes the time travel navigation commands.


## </span><span id="P"></span> p- (Step Back)

The p command executes the previous single instruction or source line. When subroutine calls or interrupts occur, they are treated as a single step. You can invoke this command using the **Step Over Back**  button on the **Home** ribbon in WinDbg Preview.
 

## </span><span id="T"></span> t- (Trace Back)

The t command executes the previous single instruction or source line. When subroutine calls or interrupts occur, each of their steps is also traced. You can invoke this command using the **Step Into Back**  button on the **Home** ribbon in WinDbg Preview.


## </span><span id="Go"></span> g- (Go Back)

The g command starts executing the current process in reverse. Execution will halt at the end of the program, when BreakAddress is hit, or when another event causes the debugger to stop. You can invoke this command using the **Go Back**  button on the **Home** ribbon in WinDbg Preview.


## </span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

The time travel navigation commands only work with time travel traces. For more information about time travel, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20HID%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





