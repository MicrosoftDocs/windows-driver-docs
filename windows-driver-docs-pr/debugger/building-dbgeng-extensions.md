---
title: Building DbgEng Extensions
description: Building DbgEng Extensions
keywords: ["DbgEng Extensions, building", "Build utility (build.exe), building DbgEng extensions"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Building DbgEng Extensions

## <span id="ddk_building_dbgeng_extensions_dbx"></span><span id="DDK_BUILDING_DBGENG_EXTENSIONS_DBX"></span>

All debugger extensions should be compiled and built by using Visual Studio. The Build utility is no longer used with debugger extensions.

For documentation on building projects in Visual Studio refer to [Visual Studio projects - C++](/cpp/build/creating-and-managing-visual-cpp-projects).

To build an extension, use the following procedure:

**To build a debugger extension**

1. Open the **dbgsdk.sln** sample project in Visual Studio.

2. Check the include and lib file project settings. If *%debuggers%* represents the root of your Debugging Tools for Windows installation, they should be set as follows:

```text
Include Path 
%debuggers%\sdk\inc
Library Path
%debuggers%\sdk\lib
```

 If you have moved these headers and libraries to a different location, specify that location instead.

3. Select **Build** and then **Build Solution** from the menu in Visual Studio.
