---
title: Writing EngExtCpp Extensions
description: Writing EngExtCpp Extensions
ms.assetid: ac8684f9-26a3-415f-9d96-938ebda29a27
keywords: ["EngExtCpp extensions, writing"]
---

# Writing EngExtCpp Extensions


## <span id="ddk_writing_dbgeng_extension_code_dbx"></span><span id="DDK_WRITING_DBGENG_EXTENSION_CODE_DBX"></span>


The EngExtCpp extension library can include any standard C++ code. It can also include the C++ interfaces that appear in the engextcpp.h and dbgeng.h header files, in addition to the C functions that appear in the wdbgexts.h header file. Both dbgeng.h and wdbgexts.h are included from engextcpp.h.

For a full list of interfaces in dbgeng.h that can be used in an extension command, see [Debugger Engine Reference](https://msdn.microsoft.com/library/windows/hardware/ff540540).

For a full list of functions in wdbgexts.h that can be used in an extension command, see [WdbgExts Functions](https://msdn.microsoft.com/library/windows/hardware/ff561258). A number of these functions appear in 32-bit versions and 64-bit versions. Typically, the 64-bit versions end in "64" and the 32-bit versions have no numerical ending -- for example, **ReadIoSpace64** and **ReadIoSpace**. When calling a wdbgexts.h function from a DbgEng extension, you should always use the function name ending in "64". This is because the [debugger engine](introduction.md#debugger-engine) always uses 64-bit pointers internally, regardless of the target platform. When including wdbgexts.h, engextcpp.h selects the 64-bit version of the API. The **ExtensionApis** global variable used by the WDbgExts API is automatically initialized on entry to a EngExtCpp method and cleared on exit.

When an EngExtCpp extension is used with remote DbgEng interfaces, the WDbgExts interfaces will not be available and the **ExtensionApis** structure can be zeroed. If an EngExtCpp extension is expected to function in such an environment, it should avoid using the WDbgExts API.

**Note**   You must not attempt to call any DbgHelp or ImageHlp routines from any debugger extension. Calling these routines is not supported and may cause a variety of problems.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Writing%20EngExtCpp%20Extensions%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




