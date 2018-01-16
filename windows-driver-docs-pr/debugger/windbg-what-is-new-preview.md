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

---
 
## See Also

[Debugging Using WinDbg Preview](debugging-using-windbg-preview.md)
 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




