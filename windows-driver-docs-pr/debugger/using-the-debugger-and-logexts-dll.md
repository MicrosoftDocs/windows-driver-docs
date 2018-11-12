---
title: Using the Debugger and Logexts.dll
description: Using the Debugger and Logexts.dll
ms.assetid: 7f7d3ca2-9b40-41ce-b66c-4367b93a7ff7
keywords: ["Logger, logexts.dll", "Logger, CDB", "Logger, WinDbg", "logexts.dll"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using the Debugger and Logexts.dll


## <span id="ddk_using_the_debugger_and_logexts_dll_dtoolq"></span><span id="DDK_USING_THE_DEBUGGER_AND_LOGEXTS_DLL_DTOOLQ"></span>


One way to activate Logger is to start CDB or WinDbg and attach to a user-mode target application as usual. Then, use the [**!logexts.logi**](-logexts-logi.md) or [**!logexts.loge**](-logexts-loge.md) extension command.

This will insert code at the current breakpoint that will jump off to a routine that loads and initializes Logexts.dll in the target application process. This is referred to as "injecting Logger into the target application."

There will actually be two instances of Logexts.dll running, since this module is both a debugger extension DLL and the program that is injected into the target application. The debugger and target instances of Logexts.dll communicate through a shared section of memory that includes the output file handles, current category mask, and a pointer to the log output buffer.

### <span id="attaching_to_the_target_application"></span><span id="ATTACHING_TO_THE_TARGET_APPLICATION"></span>Attaching to the Target Application

For information about attaching the debugger to the target application, see [Debugging a User-Mode Process Using WinDbg](debugging-a-user-mode-process-using-windbg.md) or [Debugging a User-Mode Process Using CDB](debugging-a-user-mode-process-using-cdb.md).

### <span id="using_the_logger_extension_commands"></span><span id="USING_THE_LOGGER_EXTENSION_COMMANDS"></span>Using the Logger Extension Commands

For the full syntax of each extension, see its reference page.

<span id="_LOGEXTS.LOGI"></span>[**!logexts.logi**](-logexts-logi.md)  
Injects Logger into the target application. This initializes logging, but does not enable it.

<span id="_LOGEXTS.LOGE"></span>[**!logexts.loge**](-logexts-loge.md)  
Enables logging. If [**!logexts.logi**](-logexts-logi.md) has not been used, this extension will initialize and then enable logging.

<span id="_LOGEXTS.LOGD"></span>[**!logexts.logd**](-logexts-logd.md)  
Disables logging. This will cause all API hooks to be removed in an effort to allow the program to run freely. COM hooks are not removed because they cannot be re-enabled at will.

<span id="_LOGEXTS.LOGO"></span>[**!logexts.logo**](-logexts-logo.md)  
Displays or modifies output options. Three types of output are possible: messages sent directly to the debugger, a text file, or an .lgv file. The .lgv file contains much more information than the other two; it can be read with [LogViewer](logviewer.md).

If you disable the text file output, a .txt file of size zero will still be created. This may overwrite a previously-saved text file in the same location.

<span id="_LOGEXTS.LOGC"></span>[**!logexts.logc**](-logexts-logc.md)  
Displays available API categories, controls which categories will be logged and which will not, and displays the APIs that are contained in any category.

If a category is disabled, the hooks for all APIs in that category will be removed so that there is no longer any performance overhead. COM hooks are not removed because they cannot be re-enabled at will.

Enabling only certain categories can be useful when you are only interested in a particular type of interaction that the program is having with Windows -- for example, file operations. This reduces the log file size and also reduces the effect that Logger has on the execution speed of the process.

<span id="_LOGEXTS.LOGB"></span>[**!logexts.logb**](-logexts-logb.md)  
Displays or flushes the current output buffer. As a performance consideration, log output is flushed to disk only when the output buffer is full. By default, the buffer is 2144 bytes.

Since the buffer memory is managed by the target application, the automatic writing of the buffer to the log files on the disk will not occur if there is an access violation or some other non-recoverable error in the target application. In such cases, you should use this command to manually flush the buffer to the disk, or else the most recently-logged APIs may not appear in the log files.

<span id="_LOGEXTS.LOGM"></span>[**!logexts.logm**](-logexts-logm.md)  
Displays or creates a module inclusion/exclusion list. It is often desirable to only log those API calls that are made from a certain module or set of modules. To facilitate that, Logger allows you to specify a module inclusion list or, alternatively, a module exclusion list. For instance, you would use an inclusion list if you only wanted to log calls from one or two modules. If you wanted to log calls made from all modules except a short list of modules, you would use an exclusion list. The modules Logexts.dll and Kernel32.dll are always excluded, since Logger is not permitted to log itself.

 

 





