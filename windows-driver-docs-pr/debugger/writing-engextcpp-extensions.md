---
title: Writing EngExtCpp Extensions
description: Writing EngExtCpp Extensions
ms.assetid: ac8684f9-26a3-415f-9d96-938ebda29a27
keywords: ["EngExtCpp extensions, writing"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Writing EngExtCpp Extensions


## <span id="ddk_writing_dbgeng_extension_code_dbx"></span><span id="DDK_WRITING_DBGENG_EXTENSION_CODE_DBX"></span>


The EngExtCpp extension library can include any standard C++ code. It can also include the C++ interfaces that appear in the engextcpp.h and dbgeng.h header files, in addition to the C functions that appear in the wdbgexts.h header file. Both dbgeng.h and wdbgexts.h are included from engextcpp.h.

For a full list of interfaces in dbgeng.h that can be used in an extension command, see [Debugger Engine Reference](https://msdn.microsoft.com/library/windows/hardware/ff540540).

For a full list of functions in wdbgexts.h that can be used in an extension command, see [WdbgExts Functions](https://msdn.microsoft.com/library/windows/hardware/ff561258). A number of these functions appear in 32-bit versions and 64-bit versions. Typically, the 64-bit versions end in "64" and the 32-bit versions have no numerical ending -- for example, **ReadIoSpace64** and **ReadIoSpace**. When calling a wdbgexts.h function from a DbgEng extension, you should always use the function name ending in "64". This is because the [debugger engine](introduction.md#debugger-engine) always uses 64-bit pointers internally, regardless of the target platform. When including wdbgexts.h, engextcpp.h selects the 64-bit version of the API. The **ExtensionApis** global variable used by the WDbgExts API is automatically initialized on entry to a EngExtCpp method and cleared on exit.

When an EngExtCpp extension is used with remote DbgEng interfaces, the WDbgExts interfaces will not be available and the **ExtensionApis** structure can be zeroed. If an EngExtCpp extension is expected to function in such an environment, it should avoid using the WDbgExts API.

**Note**   You must not attempt to call any DbgHelp or ImageHlp routines from any debugger extension. Calling these routines is not supported and may cause a variety of problems.

 

 

 





