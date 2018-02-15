---
title: Setting Symbol and Executable Image Paths in KD
description: Setting Symbol and Executable Image Paths in KD
ms.assetid: AF1D0A9A-2A5C-4E69-8F8A-EF74027F6742
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Symbol and Executable Image Paths in KD


## <span id="ddk_symbol_path_dbg"></span><span id="DDK_SYMBOL_PATH_DBG"></span>Symbol Path


The symbol path specifies the directories where the symbol files are located. For more information about symbols and symbol files, see [Symbols](symbols.md).

**Note**   If you are connected to the Internet or a corporate network, the most efficient way to access symbols is to use a symbol server. You can use a symbol server by using the srv\* or symsrv\* string within your symbol path. For more information about symbol servers, see [Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md).

 

To control the symbol path in KD, do one of the following:

-   Enter the [**.sympath (Set Symbol Path)**](-sympath--set-symbol-path-.md) command. If you are using a symbol server, the [**.symfix (Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command is similar to **.sympath** but saves you typing.

-   When you start the debugger, use the **-y** command-line option. See [**KD Command-Line Options**](kd-command-line-options.md).

-   Before you start the debugger, use the \_NT\_SYMBOL\_PATH and \_NT\_ALT\_SYMBOL\_PATH [environment variables](environment-variables.md) to set the path. The symbol path is created by appending \_NT\_SYMBOL\_PATH after \_NT\_ALT\_SYMBOL\_PATH. (Typically, the path is set through the \_NT\_SYMBOL\_PATH. However, you might want to use \_NT\_ALT\_SYMBOL\_PATH to override these settings in special cases, such as when you have private versions of shared symbol files.)

    **Note**  If you use the **-sins** command-line option, the debugger ignores the symbol path environment variable.

     

## <span id="Executable_Image_Path"></span><span id="executable_image_path"></span><span id="EXECUTABLE_IMAGE_PATH"></span>Executable Image Path


### <span id="ddk_executable_image_path_dbg"></span><span id="DDK_EXECUTABLE_IMAGE_PATH_DBG"></span>

An executable file is a binary file that the processor can run. These files typically have the .exe, .dll, or .sys file name extension. Executable files are also known as modules, especially when executable files are described as units of a larger application. Before the Windows operating system runs an executable file, it loads it into memory. The copy of the executable file in memory is called the executable image or the image.

**Note**   These terms are sometimes used imprecisely. For example, some documents might use "image" for the actual file on the disk. Also, Windows-based applications refer to the executable name, which typically includes the file name extension. But these applications refer to the module name, which does not include the file name extension.
Also, the Windows kernel and HAL have special module names. For example, the **nt** module corresponds to the Ntoskrnl.exe file.

 

The executable image path specifies the directories that the binary executable files are located in.

In most situations, the debugger knows the location of the executable files, so you do not have to set the path for this file.

However, there are situations when this path is required. For example, kernel-mode [small memory dump](small-memory-dump.md) files do not contain all of the executable files that exist in memory at the time of a stop error (that is, a crash). Similarly, user-mode minidump files do not contain the application binaries. If you set the path of the executable files, the debugger can find these binary files.

The debugger's executable image path is a string that consists of multiple directory paths, separated by semicolons. Relative paths are supported. However, unless you always start the debugger from the same directory, you should add a drive letter or a network share before each path. Network shares are also supported. The debugger searches the executable image path recursively. That is, the debugger searches the subdirectories of each directory that is listed in this path.

To control the executable image path in KD, do one of the following:

-   Enter the [**.exepath (Set Executable Path)**](-exepath--set-executable-path-.md) command.

-   When you start the debugger, use the **-i** command-line option. See [**KD Command-Line Options**](kd-command-line-options.md).

-   Before you start the debugger, use the \_NT\_EXECUTABLE\_IMAGE\_PATH [environment variable](environment-variables.md) to set the path.

    **Note**  If you use the **-sins** command-line option, the debugger ignores the executable image path environment variable.

     

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Symbol%20and%20Executable%20Image%20Paths%20in%20KD%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




