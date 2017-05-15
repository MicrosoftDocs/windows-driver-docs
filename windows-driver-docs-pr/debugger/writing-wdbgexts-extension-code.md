---
title: Writing WdbgExts Extension Code
description: Writing WdbgExts Extension Code
ms.assetid: bb37ea19-8355-42f3-aca5-32cc2b3be3b2
keywords: ["WdbgExts extensions", "extensions, WdbgExts"]
---

# Writing WdbgExts Extension Code


## <span id="ddk_writing_wdbgexts_extension_code_dbwx"></span><span id="DDK_WRITING_WDBGEXTS_EXTENSION_CODE_DBWX"></span>


WdbgExts extension commands can call any standard C function, as well as the debugger-related functions that appear in the WdbgExts.h header file.

The WdbgExts functions are intended for use in debugger extension commands only. They are useful for controlling and inspecting the computer or application that is being debugged. The WdbgExts.h header file should be included by any code that is calling these WdbgExts functions.

A number of these functions have 32-bit versions as well as 64-bit versions. Typically, the names of the 64-bit WdbgExts functions end in "64," for example **ReadIoSpace64**. The 32-bit versions have no numerical ending, for example, **ReadIoSpace**. If you are using 64-bit pointers, you should use the function name ending in "64"; if you are using 32-bit pointers, you should use the "undecorated" function name. 64-bit pointers are recommended for any extension that you are writing. See [32-Bit Pointers and 64-Bit Pointers](32-bit-pointers-and-64-bit-pointers.md) for details.

WdbgExts extensions cannot use the C++ interfaces that appear in the DbgEng.h header file. If you wish to use these interfaces, you should write a DbgEng extension or an EngExtCpp extension instead. Both DbgEng extensions and EngExtCpp extensions can use all the interfaces in DbgEng.h as well as those in WdbgExts.h. For details, see [Writing DbgEng Extensions](writing-dbgeng-extensions.md) and [Writing EngExtCpp Extensions](writing-engextcpp-extensions.md).

**Note**   You must not attempt to call any DbgHelp or ImageHlp routines from a debugger extension. This is not supported and may cause a variety of problems.

 

The following topics give an overview of various categories of WdbgExts functions:

[WdbgExts Input and Output](wdbgexts-input-and-output.md)

[WdbgExts Memory Access](wdbgexts-memory-access.md)

[WdbgExts Threads and Processes](wdbgexts-threads-and-processes.md)

[WdbgExts Symbols](wdbgexts-symbols.md)

[WdbgExts Target Information](wdbgexts-target-information.md)

For a full list of these functions, see [WdbgExts Functions](https://msdn.microsoft.com/library/windows/hardware/ff561258).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Writing%20WdbgExts%20Extension%20Code%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




