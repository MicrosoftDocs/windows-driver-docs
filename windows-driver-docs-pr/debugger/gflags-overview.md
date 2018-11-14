---
title: GFlags Overview
description: GFlags Overview
ms.assetid: fa5c48bf-c0d0-4010-a101-381c692082bf
keywords: ["GFlags, overview"]
ms.author: domars
ms.date: 06/12/2018
ms.localizationpriority: medium
---

# GFlags Overview


## <span id="ddk_gflags_overview_dtools"></span><span id="DDK_GFLAGS_OVERVIEW_DTOOLS"></span>


GFlags (gflags.exe), the Global Flags Editor, enables and disables advanced internal system diagnostic and troubleshooting features. You can run GFlags from a Command Prompt window or use its graphical user interface dialog box.

For information on how to install and locate gflags.exe, see [GFlags](gflags.md).


Use GFlags to activate the following features:

<span id="Registry"></span><span id="registry"></span><span id="REGISTRY"></span>Registry  
Set system-wide debugging features for all processes running on the computer. These settings are stored in the **GlobalFlag** registry entry (**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\GlobalFlag**). They take effect when you restart Windows and remain effective until you change them and restart again.

<span id="Kernel_flag_settings"></span><span id="kernel_flag_settings"></span><span id="KERNEL_FLAG_SETTINGS"></span>Kernel flag settings  
Set debugging features for this session. These settings are effective immediately, but are lost when Windows shuts down. The settings affect all processes started after this command completes.

<span id="Image_file_settings"></span><span id="image_file_settings"></span><span id="IMAGE_FILE_SETTINGS"></span>Image file settings  
Set debugging features for a particular program. These settings are stored in a GlobalFlag registry entry for each program (**HKEY\_LOCAL\_MACHINE\\ SOFTWARE\\ Microsoft\\ Windows NT\\ CurrentVersion\\ Image File Execution Options\\ *ImageFileName*\\ GlobalFlag**). They take effect when you restart the program and remain effective until you change them.

<span id="Debugger"></span><span id="debugger"></span><span id="DEBUGGER"></span>Debugger  
Specify that a particular program always runs in a debugger. This setting is stored in the registry. It is effective immediately and remains effective until you change it. (This feature is available only in the **Global Flags** dialog box.)

<span id="Launch"></span><span id="launch"></span><span id="LAUNCH"></span>Launch  
Run a program with the specified debugging settings. The debugging settings are effective until the program stops. (This feature is available only from the **Global Flags** dialog box.)

<span id="Special_Pool"></span><span id="special_pool"></span><span id="SPECIAL_POOL"></span>Special Pool  
Request that allocation with a specified pool tag or of a specified size are filled from the special pool. This feature helps you to detect and identify the source of errors in kernel pool use, such as writing beyond the allocated memory space, or referring to memory that has already been freed.

Beginning in Windows Vista, you can enable, disable, and configure the special pool feature (**Kernel Special Pool Tag**) as a kernel flags setting, which does not require a reboot, or as a registry setting, which requires a reboot.

<span id="Page_heap_verification"></span><span id="page_heap_verification"></span><span id="PAGE_HEAP_VERIFICATION"></span>Page heap verification  
Enable, disable, and configure page heap verification for a program. When enabled, page heap monitors dynamic heap memory operations, including allocation and free operations, and causes a debugger break when it detects a heap error.

<span id="Silent_process_exit"></span><span id="silent_process_exit"></span><span id="SILENT_PROCESS_EXIT"></span>Silent process exit  
Enable, disable, and configure monitoring and reporting of silent exits for a process. You can specify actions that occur when a process exits silently, including notification, event logging, and creation of dump files. For more information, see [Monitoring Silent Process Exit](registry-entries-for-silent-process-exit.md).

 

 





