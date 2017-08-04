---
title: WinDbg Preview Installation and Startup Options
description: This section describes how to install the WinDbg Preview debugger.
ms.author: windowsdriverdev
ms.date: 07/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WinDbg Preview Installation and Startup Options

## Installation

This section describes how to install the WinDbg Preview debugger.

The WinDbg Preview debugger is available in the Windows Store. 

To install it, open the Windows Store and search for "Window Debugger Preview".

Once the app is a located click to download and install it.


## Installation Location

>> TBD Need to validate this with final store app distribution.

WinDbg Preview installs to %localappdata%\dbg\UI\WinDbgX.exe. If you're trying to copy an extension so that you can easily load it, you can copy the extension to %localappdata%\dbg\EngineExtensions\ for 64-bit extensions, or %localappdata%\dbg\EngineExtensions32 for 32-bit extensions. 

You can XCopy the binaries from \\dbg\dbgx\build\[version] or \\dbg\dbgx\slow\[version] to the location of your choice, such as a thumb drive for portable use.

>> TBD

## Checking for updates

Use the *Update debugger* option on the Home menu to check for updates.


## Command line startup options

For information on the startup parameters for WinDbg Preview, see [WinDbg Command-Line Options](windbg-command-line-options).

>> TBD need to determine if all options are supported. 

You can use /? to list additional command line options.

![Screen shot of command line help output listing about 50 options](images/windbgx-start-up-options.png)


*Additional content pending*
 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




