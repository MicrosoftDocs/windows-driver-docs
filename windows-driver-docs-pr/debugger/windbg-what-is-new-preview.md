---
title: WinDbg Preview - What's New 
description: This topic provides inofmration on what's new in WinDbg preview debugger.
ms.author: domars
ms.date: 12/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# WinDbg Preview - What's New

This topic provides information on what's new in the WinDbg Preview debugger. 

For detailed information about the debugger releases, refer to the debugger tools team blog [https://blogs.msdn.microsoft.com/windbg/](https://blogs.msdn.microsoft.com/windbg/).


## 1.0.12.0

This version was the first release of WinDbg Preview. For general information on the features available in WinDbg Preview, [Debugging Using WinDbg Preview](debugging-using-windbg-preview.md).


## 1.0.13.0

This version adds Time Travel Tracing. Time Travel Debugging, allows you to record a process, then replay it later both forwards and backwards. Time Travel Debugging (TTD) can help you debug issues easier by letting you "rewind" your debugger session, instead of having to reproduce the issue until you find the bug. For more information, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).


## 1.0.14.0

This version includes these updates.

- The Start Debugging page now shows if you’re connected to a process server (DbgSrv) remote and allows you to disconnect from it.
- New pre-set layout options in the View ribbon.
- New Time Travel ribbon when debugging a time travel trace.
- Many fixes, updates, and changes to JSProvider APIs, see full release notes for details.

Known issues
- SOS will not work on x86 traces.


## 1.1712.15003.0

This version includes these updates.

- You can now query memory in TTD traces
- Settings will now be preserved across WinDbg Preview sessions
- Start-up performance improvements
- Additional bug fixes

## 1.0.1804.18003

This version includes these updates.

- Symbol status and cancellation improvements
- Experimental notes window
- Experimental faster source window
- JSProvider API version 1.2
- Minor changes and bug fixes


---
 
## See Also

[Debugging Using WinDbg Preview](debugging-using-windbg-preview.md)
 





