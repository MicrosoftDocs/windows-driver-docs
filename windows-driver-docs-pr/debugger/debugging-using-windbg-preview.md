---
title: Debugging Using WinDbg Preview
description: This section describes how to perform basic debugging tasks using the WinDbg preview debugger.
---

# Debugging Using WinDbg Preview

Welcome to the WinDbg Preview. This next gen debugger is being developed with the debugger communiyt in mind. Use the feedback button to provide feedback.

For the latest news, refer to the debugger tools team blog, located here.
[https://blogs.msdn.microsoft.com/windbg/](https://blogs.msdn.microsoft.com/windbg/)

This section describes how to perform basic debugging tasks using the WinDbg debugger.

Review these topics to install and configure.

- [WinDbg Preview Installation](windbg-install-preview.md)
- [WinDbg Preview Setup – settings and workspaces](windbg-setup-preview.md)
- [Coexisting with the classic WinDbg debugger](windbg-coexist-preview.md)

These topics describe how to get connected to the environment that you want to debug. 

- [Debugging a User-Mode Process Using WinDbg](windbg-user-mode-preview.md)
-  (debugging-a-user-mode-process-using-windbg.md)
- [Attaching to a kernel process.md](windbg-kernel-mode-preview.md)
-   [Live Kernel-Mode Debugging Using WinDbg](performing-kernel-mode-debugging-using-windbg.md)

These topics describe how to complete common tasks, organized by the menu tabs.

- [View](windbg-view-preview.md)
- [Breakpoints](windbg-breakpoints-preview.md)
-   [Setting Breakpoints in WinDbg](setting-breakpoints-in-windbg.md)
- [Data Model](windbg-data-model-preview.md)
- [Scripting](windbg-scripting-preview.md)
- [Logs](windbg-logs-preview.md)
-   [Keeping a Log File in WinDbg](keeping-a-log-file-in-windbg.md)


# Providing Feedback

Your feedback will guide the debugger tool development effort going forward. 

- If you have feedback such as a feature that you really want to see, use the Feedback Hub.
- If you see a bug or unexpected behavior - Send-a-frown, and/or use the Feedback Hub and check the “This is a bug” check box.
- If you really like a feature  -  hit send-a-smile and tell us!
- TBD >> newsgroup - use the existing one?


# Features of the next generation debugger

The WinDbg Preview is the next generation debugger with a contemporary interface. The UI has been completely rewritten using the Microsoft Windows Presentation Foundation (WPF). For more information, see 
[XAML Overview (WPF)](https://docs.microsoft.com/en-us/dotnet/framework/wpf/advanced/xaml-overview-wpf). 

![Screen shot of main screen in debugger](/images/windbgx-main-menu.png)

### Backwards Compatability 

Because the underling debugger engine is the same, all of the previous debugger commands and debugger extensions continue to work.

### General Features

- **Easier Connection Setup and Recall** - The WinDbg Preview includes the ability to recall previous session configuration information.
- **Update notifications** - When new updates are available, a banner will be displayed notifying you that an update is available.
- **In product feedback channel** - Your feedback will guide the development effort going forward. For more information, see [Providing Feedback](#providing-feedback)
- **Dump file processor detection** -Auto-detect dump processor architecture for managed dumps.
- TBD >> **UI Extensibility** - The UI can be extended to add new windows and functionality to WinDbg Preview.  
- **Performance Improvments** Windows now load asynchronously and can be canceled - When you run another command, WinDbgNext will stop the loading of your locals, watch, or other windows.


### View  

- **Disassembly Window Improvements** - The disassembly window is also improved, the highlight of the current instruction remains where it is when you scroll. 
- **Memory Window Improvements** - The memory window has highlighting and improved scrolling.
- **Data model visualization** - The locals and watch windows are both based off of the data model that is used by the dx command. This means the locals and watch windows will benefit from any NatVis or JavaScript extensions you have loaded, and can even support full LINQ queries, just like the dx command. 

For more information, see [View](windbg-view-preview.md).

![Screen shot of view screen in debugger](/images/windbgx-view-menu.png)


### Command, memory and source windows  

- **Command window** - The command window provides easy access to toggle DML and clear the debugger command window. All current debugger commands are compatible with and continue to work in WinDbg Preview.
- **Memory Window** - The memory Window
- **Source Window** - 
![Screen shot of other windows in debugger](/images/windbgx-other-windows-menu.png)


### Breakpoints 

- **Enable/Disable Breakpoints** - The breakpoints window shows all your current breakpoints and provides easy access to enabling and disabling them. 
- **Hit Count** - The breakpoint window keep a running total of each time the breakpoint is hit.

For more information, see [Breakpoints](windbg-breakpoints-preview.md).

![Screen shot of breakpoint screen in debugger](/images/windbgx-breakpoint-menu.png)


### Data Model 

- **Built in data model support** - WinDbg Preview is written with built in data model support and the data model is available through out the debugger.
- **Model window** - The model window gives you an expandable and browsable version of ‘dx’ and ‘dx -g’, letting you create powerful tables on-top of your NatVis, JavaScript, and LINQ queries. 

For more information, see  [Data Model](windbg-data-model-preview.md)
.

### Scripting  

- **Script development UI** - A lot of people have taken advantage of JavaScript and NatVis support in WinDbg, adn there is now a scripting window to make that process easier, with error highlighting, Intellisense abd debugging. 

For more information, see [Scripting](windbg-scripting-preview.md).


### Logs  

- **1** -
- **2** -

For more information, see [Logs](windbg-logs-preview.md)


************************************
>> TBD - Possible post August release content
************************************

-   [Opening a Dump File Using WinDbg](opening-a-crash-dump-file-using-windbg.md)
-   [Ending a Debugging Session in WinDbg](ending-a-debugging-session-in-windbg.md)
-   [Setting Symbol and Executable Image Paths in WinDbg](setting-symbol-and-source-paths-in-windbg.md)
-   [Remote Debugging Using WinDbg](remode-debugging-using-windbg.md)
-   [Entering Debugger Commands in WinDbg](debugger-command-window.md)
-   [Using the Command Browser Window in WinDbg](command-browser-window.md)

View
-   [Viewing the Call Stack in WinDbg](calls-window.md)

-   [Viewing and Editing Registers in WinDbg](registers-window.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




