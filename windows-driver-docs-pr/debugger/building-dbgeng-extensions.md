---
title: Building DbgEng Extensions
description: Building DbgEng Extensions
ms.assetid: e2cf8a01-2099-4ad7-98ac-1a20c76a2e0a
keywords: ["DbgEng Extensions, building", "Build utility (build.exe), building DbgEng extensions"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Building DbgEng Extensions


## <span id="ddk_building_dbgeng_extensions_dbx"></span><span id="DDK_BUILDING_DBGENG_EXTENSIONS_DBX"></span>


All debugger extensions should be compiled and built by using Visual Studio. The Build utility is no longer used with debugger extensions.

For documentation on the Building projects in Visual Studio refer to [Building C++ Projects in Visual Studio.](https://msdn.microsoft.com/library/7s88b19e.aspx)

To build an extension, use the following procedure:

**To build a debugger extension**

1.  Open the **dbgsdk.sln** sample project in Visual Studio.

2.  Check the include and lib file project settings. If *%debuggers%* represents the root of your Debugging Tools for Windows installation, they should be set as follows:

    ```text
    Include Path 
    %debuggers%\sdk\inc
    Library Path
    %debuggers%\sdk\lib
    ```

    If you have moved these headers and libraries to a different location, specify that location instead.

3.  Select **Build** and then **Build Solution** from the menu in Visual Studio.

 

 





