---
title: Using the Debugger and Logexts.dll
description: Using the Debugger and Logexts.dll
ms.assetid: 7f7d3ca2-9b40-41ce-b66c-4367b93a7ff7
keywords: ["Logger, logexts.dll", "Logger, CDB", "Logger, WinDbg", "logexts.dll"]
---

# Using the Debugger and Logexts.dll


## <span id="ddk_using_the_debugger_and_logexts_dll_dtoolq"></span><span id="DDK_USING_THE_DEBUGGER_AND_LOGEXTS_DLL_DTOOLQ"></span>


One way to activate Logger is to start CDB or WinDbg and attach to a user-mode target application as usual. Then, use the [**!logexts.logi**](https://msdn.microsoft.com/library/windows/hardware/ff564005) or [**!logexts.loge**](https://msdn.microsoft.com/library/windows/hardware/ff564002) extension command.

This will insert code at the current breakpoint that will jump off to a routine that loads and initializes Logexts.dll in the target application process. This is referred to as "injecting Logger into the target application."

There will actually be two instances of Logexts.dll running, since this module is both a debugger extension DLL and the program that is injected into the target application. The debugger and target instances of Logexts.dll communicate through a shared section of memory that includes the output file handles, current category mask, and a pointer to the log output buffer.

### <span id="attaching_to_the_target_application"></span><span id="ATTACHING_TO_THE_TARGET_APPLICATION"></span>Attaching to the Target Application

For information about attaching the debugger to the target application, see [Debugging a User-Mode Process Using WinDbg](debugging-a-user-mode-process-using-windbg.md) or [Debugging a User-Mode Process Using CDB](debugging-a-user-mode-process-using-cdb.md).

### <span id="using_the_logger_extension_commands"></span><span id="USING_THE_LOGGER_EXTENSION_COMMANDS"></span>Using the Logger Extension Commands

For the full syntax of each extension, see its reference page.

<span id="_LOGEXTS.LOGI"></span>[**!logexts.logi**](https://msdn.microsoft.com/library/windows/hardware/ff564005)  
Injects Logger into the target application. This initializes logging, but does not enable it.

<span id="_LOGEXTS.LOGE"></span>[**!logexts.loge**](https://msdn.microsoft.com/library/windows/hardware/ff564002)  
Enables logging. If [**!logexts.logi**](https://msdn.microsoft.com/library/windows/hardware/ff564005) has not been used, this extension will initialize and then enable logging.

<span id="_LOGEXTS.LOGD"></span>[**!logexts.logd**](https://msdn.microsoft.com/library/windows/hardware/ff564001)  
Disables logging. This will cause all API hooks to be removed in an effort to allow the program to run freely. COM hooks are not removed because they cannot be re-enabled at will.

<span id="_LOGEXTS.LOGO"></span>[**!logexts.logo**](https://msdn.microsoft.com/library/windows/hardware/ff564009)  
Displays or modifies output options. Three types of output are possible: messages sent directly to the debugger, a text file, or an .lgv file. The .lgv file contains much more information than the other two; it can be read with [LogViewer](logviewer.md).

If you disable the text file output, a .txt file of size zero will still be created. This may overwrite a previously-saved text file in the same location.

<span id="_LOGEXTS.LOGC"></span>[**!logexts.logc**](https://msdn.microsoft.com/library/windows/hardware/ff563998)  
Displays available API categories, controls which categories will be logged and which will not, and displays the APIs that are contained in any category.

If a category is disabled, the hooks for all APIs in that category will be removed so that there is no longer any performance overhead. COM hooks are not removed because they cannot be re-enabled at will.

Enabling only certain categories can be useful when you are only interested in a particular type of interaction that the program is having with Windows -- for example, file operations. This reduces the log file size and also reduces the effect that Logger has on the execution speed of the process.

<span id="_LOGEXTS.LOGB"></span>[**!logexts.logb**](https://msdn.microsoft.com/library/windows/hardware/ff563996)  
Displays or flushes the current output buffer. As a performance consideration, log output is flushed to disk only when the output buffer is full. By default, the buffer is 2144 bytes.

Since the buffer memory is managed by the target application, the automatic writing of the buffer to the log files on the disk will not occur if there is an access violation or some other non-recoverable error in the target application. In such cases, you should use this command to manually flush the buffer to the disk, or else the most recently-logged APIs may not appear in the log files.

<span id="_LOGEXTS.LOGM"></span>[**!logexts.logm**](https://msdn.microsoft.com/library/windows/hardware/ff564007)  
Displays or creates a module inclusion/exclusion list. It is often desirable to only log those API calls that are made from a certain module or set of modules. To facilitate that, Logger allows you to specify a module inclusion list or, alternatively, a module exclusion list. For instance, you would use an inclusion list if you only wanted to log calls from one or two modules. If you wanted to log calls made from all modules except a short list of modules, you would use an exclusion list. The modules Logexts.dll and Kernel32.dll are always excluded, since Logger is not permitted to log itself.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20the%20Debugger%20and%20Logexts.dll%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




