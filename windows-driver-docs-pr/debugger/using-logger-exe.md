---
title: Using Logger.exe
description: Using Logger.exe
ms.assetid: da2ec999-4529-49dc-855e-a7d3b15583f7
keywords: ["Logger, logger.exe", "logger.exe", "Logger, stand-alone"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Logger.exe


## <span id="ddk_using_logger_exe_dtoolq"></span><span id="DDK_USING_LOGGER_EXE_DTOOLQ"></span>


One way to activate Logger is to run the stand-alone Logger.exe program. This is essentially a very small debugger that can only take a single target. To run it, include the name of the target application on the command line:

```dbgcmd
logger Target 
```

When this is activated, it will load the specified application, and insert code into the target application that will jump off to a routine that loads and initializes Logexts.dll in the target application process. This is referred to as "injecting Logger into the target application."

The Logger.exe utility and the Logexts.dll module are the two components of this Logger vehicle. They communicate through a shared section of memory that includes the output file handles, current category mask, and a pointer to the log output buffer.

A window entitled **Logger (debugger)** will appear. This window will display the progress of Logger.

### <span id="change_settings_dialog_box"></span><span id="CHANGE_SETTINGS_DIALOG_BOX"></span>Change Settings Dialog Box

After the initialization finishes and the initial display is complete, the **Change Settings** dialog box will appear. This allows you to configure the Logger settings. The various settings are described here:

<span id="API_Settings"></span><span id="api_settings"></span><span id="API_SETTINGS"></span>**API Settings**  
This list displays the available API categories. The highlighted categories will be logged; the non-highlighted categories will not. The first time you run Logger, all categories will be highlighted. However, on subsequent runs, Logger will keep track of which categories are selected for a given target application.

If a category is disabled, the hooks for all APIs in that category will be removed so that there is no longer any performance overhead. COM hooks are not removed because they cannot be re-enabled at will.

Enabling only certain categories can be useful when you are only interested in a particular type of interaction that the program is having with Windows -- for example, file operations. This reduces the log file size and also reduces the effect that Logger has on the execution speed of the process.

<span id="Logging"></span><span id="logging"></span><span id="LOGGING"></span>**Logging**  
This section contains **Enable** and **Disable** radio buttons. Disabling logging will cause all API hooks to be removed in an effort to allow the program to run freely. COM hooks are not removed because they cannot be re-enabled at will.

<span id="Inclusion___Exclusion_List"></span><span id="inclusion___exclusion_list"></span><span id="INCLUSION___EXCLUSION_LIST"></span>**Inclusion / Exclusion List**  
This section controls the module inclusion/exclusion list. It is often desirable to log only those function calls that are made from a certain module or set of modules. To facilitate that, Logger allows you to specify a module inclusion list or, alternatively, a module exclusion list. For instance, you would use an inclusion list if you only wanted to log calls from one or two module. If you wanted to log calls made from all modules except a short list of modules, you would use an exclusion list. The modules Logexts.dll and Kernel32.dll are always excluded, since Logger is not permitted to log itself.

<span id="Flush_the_Buffer"></span><span id="flush_the_buffer"></span><span id="FLUSH_THE_BUFFER"></span>**Flush the Buffer**  
This button will flush the current output buffer. As a performance consideration, log output is flushed to disk only when the output buffer is full. By default, the buffer is 2144 bytes.

Since the buffer memory is managed by the target application, the automatic writing of the buffer to the log files on the disk will not occur if there is an access violation or some other non-recoverable error in the target application. In such cases, you should try to activate the target application's window and hit F12 to get this dialog box back, and then press **Flush the Buffer**. If this is not done, the most recently-logged functions might not appear in the log files.

<span id="Go"></span><span id="go"></span><span id="GO"></span>**Go**  
This causes the target application to begin executing.

### <span id="running_the_target_application"></span><span id="RUNNING_THE_TARGET_APPLICATION"></span>Running the Target Application

Once you have chosen the settings, click **Go**. The dialog box will close and the target application will begin to run.

If you make the target application's window active and press F12, it will break into Logger. This will cause the target application to freeze and the **Change Settings** dialog box to reappear. You can alter the settings if you wish, and then press **Go** to continue execution.

You can let the target application run for as long as you wish. If it terminates normally or due to an error, the logging will stop and cannot be restarted.

When you wish to exit, select **File | Exit** and click **Yes**. If the target application is still running, it will be terminated.

### <span id="limitations_of_logger_exe"></span><span id="LIMITATIONS_OF_LOGGER_EXE"></span>Limitations of Logger.exe

When you are running Logger through the Logger.exe tool, it will create only one output file -- an .lgv file. No text file will be written. However, a .txt file of size zero will be created; this could overwrite a text log written by the debugger previously.

The output file will always be placed in LogExts subdirectory of the desktop; this location cannot be changed.

These limitations will not apply if you are running Logger through the debugger and Logexts.dll.

 

 





