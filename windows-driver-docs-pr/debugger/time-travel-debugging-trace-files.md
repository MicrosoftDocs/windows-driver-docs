---
title: Time Travel Debugging - Working with Trace Files 
description: This section describes how to work with time travel trace files 
ms.author: windowsdriverdev
ms.date: 09/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - Working with Trace Files

This section describes how to with time travel trace files .

TBD TBD TBD 

Traces can be opened after recorded

Need to share the .run file. .idx can be re-built with !index. If you don’t care about how big, share the .idx file. – TBD – What should we recommend people do.

Can be shared between others

Key positions in time 
"Now, let's say that you suspect there is a bug on a part of the code your coworker knows best. You can take note of what position in time you coworker should navigate to in order to investigate" (pick a previous position) "Then you can share this position with your coworker" 
"Let me pretend to be your coworker (Close Windbg). I get the trace file from you and I open it. (Open the trace)" 
"I can pick up debugging exactly where you suggest by navigating to that position. The command for this is !tt x:y"(run command) 
Successful recorded traces or previously loaded traces can be easily access from your Recents list as well.

o	Traces can be opened after recorded
o	Need to share the .run file. .idx can be re-built with !index. If you don’t care about how big, share the .idx file. – TBD – What should we recommend people do.
o	Can be shared between others



> Additional Content Pending

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




