---
title: Setting Symbol and Executable Image Paths in WinDbg
description: Setting Symbol and Executable Image Paths in WinDbg
ms.assetid: 8EA2509E-0B47-4D28-B934-F1F58F5CFC45
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Setting Symbol and Executable Image Paths in WinDbg


## <span id="ddk_symbol_path_dbg"></span><span id="DDK_SYMBOL_PATH_DBG"></span>Symbol Path


The symbol path specifies the directories where the symbol files are located. For more information about symbols and symbol files, see [Symbols](symbols.md).

**Note**   If you are connected to the Internet or a corporate network, the most efficient way to access symbols is to use a symbol server. You can use a symbol server by using the srv\* or symsrv\* string within your symbol path. For more information about symbol servers, see [Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md).

 

To control the symbol path in WinDbg, do one of the following:

-   Choose **Symbol File Path** from the **File** menu or press CTRL+S.

-   Use the [**.sympath (Set Symbol Path)**](-sympath--set-symbol-path-.md) command. If you are using a symbol server, the [**.symfix (Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command is similar to **.sympath** but saves you typing.

-   When you start the debugger, use the **-y** command-line option. See [**WinDbg Command-Line Options**](windbg-command-line-options.md).

-   Before you start the debugger, use the \_NT\_SYMBOL\_PATH and \_NT\_ALT\_SYMBOL\_PATH [environment variables](environment-variables.md) to set the path. The symbol path is created by appending \_NT\_SYMBOL\_PATH after \_NT\_ALT\_SYMBOL\_PATH. (Typically, the path is set through the \_NT\_SYMBOL\_PATH. However, you might want to use \_NT\_ALT\_SYMBOL\_PATH to override these settings in special cases, such as when you have private versions of shared symbol files.) If you try to add an invalid directory through these environment variables, the debugger ignores this directory.

    **Note**  If you use the -**sins** command-line option, the debugger ignores the symbol path environment variable.

     

## <span id="Executable_Image_Path"></span><span id="executable_image_path"></span><span id="EXECUTABLE_IMAGE_PATH"></span>Executable Image Path


### <span id="ddk_executable_image_path_dbg"></span><span id="DDK_EXECUTABLE_IMAGE_PATH_DBG"></span>

An executable file is a binary file that the processor can run. These files typically have the .exe, .dll, or .sys file name extension. Executable files are also known as modules, especially when executable files are described as units of a larger application. Before the Windows operating system runs an executable file, it loads it into memory. The copy of the executable file in memory is called the executable image or the image.

**Note**   These terms are sometimes used imprecisely. For example, some documents might use "image" for the actual file on the disk. Also, the Windows kernel and HAL have special module names. For example, the **nt** module corresponds to the Ntoskrnl.exe file.

 

The executable image path specifies the directories that the binary executable files are located in.

In most situations, the debugger knows the location of the executable files, so you do not have to set the path for this file.

However, there are situations when this path is required. For example, kernel-mode [small memory dump](small-memory-dump.md) files do not contain all of the executable files that exist in memory at the time of a stop error (that is, a crash). Similarly, user-mode minidump files do not contain the application binaries. If you set the path of the executable files, the debugger can find these binary files.

The debugger's executable image path is a string that consists of multiple directory paths, separated by semicolons. Relative paths are supported. However, unless you always start the debugger from the same directory, you should add a drive letter or a network share before each path. Network shares are also supported. The debugger searches the executable image path recursively. That is, the debugger searches the subdirectories of each directory that is listed in this path.

To control the executable image path in WinDbg, do one of the following:

-   Choose **Image File Path** from the **File** menu, or press CTRL+I.

-   Use the [**.exepath (Set Executable Path)**](-exepath--set-executable-path-.md) command.

-   When you start the debugger, use the **-i** command-line option. See [**WinDbg Command-Line Options**](windbg-command-line-options.md).

-   Before you start the debugger, use the \_NT\_EXECUTABLE\_IMAGE\_PATH [environment variable](environment-variables.md) to set the path.

    **Note**  If you use the **-sins** command-line option, the debugger ignores the executable image path environment variable.

     

 

 





