---
title: Logging Driver Errors
description: Logging Driver Errors
ms.assetid: 7deb2a9a-70aa-4660-a0c8-e118e03eef3b
keywords:
- error logs WDK display
- errors WDK display
- logging errors WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Logging Driver Errors


The Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) records display driver-related errors, assertions, warnings, and events to a log in memory (in *Watchdog.sys*).

In addition to recording information to a log, by default, the checked-build version of the DirectX graphics kernel subsystem breaks into the attached debugger if errors or assertions occur. By default, the free-build version of the DirectX graphics kernel subsystem only records errors and assertions to the log and does not break into the debugger if errors or assertions occur. You can change this default behavior by first creating the following REG\_DWORD entries in the registry:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Logging\BreakOnAssertion
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Logging\BreakOnError
```

To make the debugger start if errors or assertions occur, you should set the value of **BreakOnError** or **BreakOnAssertion** to 1 (TRUE) respectively. To make the debugger not start if errors or assertions occur, you should set the value of **BreakOnError** or **BreakOnAssertion** to 0 (FALSE) respectively.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Logging%20Driver%20Errors%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




