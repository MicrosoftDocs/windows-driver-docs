---
title: Installing Windows Symbol Files
description: Installing Windows Symbol Files
ms.assetid: fbafb14c-9b92-47c5-9954-5c5ba2301c47
keywords: ["symbols, Windows", "symbols, user-mode"]
ms.author: domars
ms.date: 03/26/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing Windows Symbol Files


## <span id="ddk_installing_windows_symbol_files_dbg"></span><span id="DDK_INSTALLING_WINDOWS_SYMBOL_FILES_DBG"></span>


Before you debug the Windows kernel or a driver or application running on Windows, you need access to the proper symbol files.

The easiest way to get Windows symbols is to use the Microsoft Symbol Server. The symbol server makes symbols available to your debugging tools as needed. After a symbol file is downloaded from the symbol server it is cached on the local computer for quick access. Additional versions of Windows not listed here, are available on the Microsoft Symbol Server. 

You can connect to the Microsoft Symbol Server with one simple use of the [**.symfix (Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command. For full details, see [Microsoft Public Symbols](microsoft-public-symbols.md).

If you plan to install symbols manually, it is crucial that you remember this basic rule: *the symbol files on the host computer are required to match the version of Windows installed on the target computer.*  

If you plan to perform user-mode debugging on the same computer as the target application, then install the symbol files that match the version of Windows running on that system. If you are analyzing a memory dump file, then the version of symbol files needed on the debug computer are those that match the version of the operating system that produced the dump file, not necessarily those matching the version of the operating system on the machine running the debug session.

**Note**   If you are going to use your host computer to debug several different target computers, you may need symbols for more than one build of Windows. In this case, be sure to install each symbol collection in a distinct directory path.


If you are debugging from a Windows computer attached to a network, it may be useful to install symbols for a variety of different builds on a network server. Microsoft debuggers will accept a network path (*\\\\server\\share\\dir*) as a valid symbol directory path. This avoids the need for each debugging computer on the network to install the symbol files separately.

Symbol files stored on a crashed target computer are not usable by the debugger on the host computer.

**To install Windows symbol files**

1.  Make sure you have sufficient space on the disk drive of the host computer.

2.  Open [Download Windows Symbol Packages](http://go.microsoft.com/fwlink/p/?linkid=17363).

3.  Follow the links to download and install the desired symbol package.


### <span id="installing_user_mode_symbols"></span><span id="INSTALLING_USER_MODE_SYMBOLS"></span>Installing User-Mode Symbols

If you are going to debug a user-mode application, you need to install the symbols for this application as well.

You can debug an application if you have its symbols but not Windows symbols. However, your results will be much more limited. You will still be able to step through the application code, but any debugger activity which requires analysis of the kernel (such as getting a stack trace) is likely to fail.

 

 





