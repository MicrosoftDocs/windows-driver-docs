---
title: GFlags Details
description: GFlags Details
keywords: ["GFlags, details"]
ms.date: 04/12/2019
---

# GFlags Details

GFlags enables and disables system features by editing the Windows registry and internal settings. This section explains the operation of GFlags in detail and includes tips for using GFlags most efficiently.

## General Information

- To display the GFlags dialog box, at the command line, type **gflags** (with no parameters).

- GFlags system-level registry settings appear in the registry immediately, but do not take effect until you restart the system.

- GFlags image file registry settings appear in the registry immediately, but do not take effect until you restart the process.

- The debugger and launch features in the GFlags dialog box are program specific. You can only set them on one image file at a time.

### Flag Details

- To clear all flags, set the flag to -FFFFFFFF. Setting the flag to 0 adds 0 to the current flag value.

- When you set the flags for an image file to FFFFFFFF (0xFFFFFFFF), Windows clears all flags for the image file and deletes the **GlobalFlag** entry in the image file registry key. The image file registry key is retained.

### Dialog Box and Command Line

You can run GFlags by using its handy dialog box or from the command line. Most features are available in both forms, with the following exceptions.

#### Dialog box only

- Launch. Start a program using the specified flags.

- Run the program in a debugger.

- [Special Pool](special-pool.md) on systems prior to Windows Vista. On Windows Vista and later versions of Windows, you can configure the Special Pool feature at the command line or in the Gflags dialog box.

#### Command line only

- Set the size of the user mode stack trace database (/tracedb).

- Set page heap verification options.

### Registry Information

GFlags settings that are saved between sessions are stored in the registry. You can use the registry APIs, Regedit, or reg.exe to query or change these values. The following table lists the types of settings and where they are stored in the registry.

|Type of setting|Registry location|
|----|----|
|Systemwide settings ("Registry")|HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\\**GlobalFlag**|
|Program-specific settings ("Image file") for all users of the computer.|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\\*ImageFileName*\\**GlobalFlag**|
|Silent exit settings for a specific program ("Silent Process Exit") for all users of the computer.|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\\***ImageFileName***|
|Page heap options for an image file for all users of the computer|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\\*ImageFileName*\\**PageHeapFlags**
|User mode stack trace database size (**tracedb**)|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\\*ImageFileName*\\**StackTraceDatabaseSizeInMb**|
|Create user mode stack trace database (ust, 0x1000) for an image file|Windows adds the image file name to the value of the USTEnabled registry entry (HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\\**USTEnabled**).
|Load image using large pages if possible|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\\*ImageFileName*\\**UseLargePages**.
|Special Pool (Kernel Special Pool Tag)|HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\\**PoolTag**|
Verify Start / Verify End|HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PoolTagOverruns. The **Verify Start** option sets the value to 0. The **Verify End** option sets the value to 1.
|Debugger for an image file|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\\*ImageFileName*\\**Debugger**
|Object Reference Tracing|HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Kernel\\**ObTraceProcessName**, **ObTracePermanent** and **ObTracePoolTags**
