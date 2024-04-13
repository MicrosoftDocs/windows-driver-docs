---
title: Writing DbgEng Extension Code
description: This section describes writing DbgEng extension code
keywords: ["DbgEng Extensions, writing"]
ms.date: 10/24/2019
---

# Writing DbgEng Extension Code

## <span id="ddk_writing_dbgeng_extension_code_dbx"></span><span id="DDK_WRITING_DBGENG_EXTENSION_CODE_DBX"></span>

[DbgEng extension](debugger-engine-and-extension-apis.md) commands can include any standard C++ code. They can also include the C++ interfaces that appear in the dbgeng.h header file, in addition to the C functions that appear in the wdbgexts.h header file.

If you intend to use functions from wdbgexts.h, you need to define KDEXT\_64BIT before wdbgexts.h is included. For example:

```cpp
#define KDEXT_64BIT
#include wdbgexts.h
#include dbgeng.h
```

For a full list of interfaces in dbgeng.h that can be used in an extension command, see [Debugger Engine Reference](debugger-engine-reference.md).

For a full list of functions in wdbgexts.h that can be used in an extension command, see [WdbgExts Functions](wdbgexts-functions.md). A number of these functions appear in 32-bit versions and 64-bit versions. Typically, the 64-bit versions end in "64" and the 32-bit versions have no numerical ending -- for example, **ReadIoSpace64** and **ReadIoSpace**. When calling a wdbgexts.h function from a DbgEng extension, you should always use the function name ending in "64". This is because the [debugger engine](introduction.md#debugger-engine) always uses 64-bit pointers internally, regardless of the target platform.

If you include wdbgexts.h in your DbgEng extension, you should call [**GetWindbgExtensionApis64**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getwindbgextensionapis64) during the initialization of your extension DLL (see [*DebugExtensionInitialize*](/windows-hardware/drivers/ddi/dbgeng/nc-dbgeng-pdebug_extension_initialize)).

**Note**   You must not attempt to call any DbgHelp or ImageHlp routines from any debugger extension. Calling these routines is not supported and may cause a variety of problems.
