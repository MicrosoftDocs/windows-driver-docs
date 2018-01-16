---
title: Building DbgEng Extensions
description: Building DbgEng Extensions
ms.assetid: e2cf8a01-2099-4ad7-98ac-1a20c76a2e0a
keywords: ["DbgEng Extensions, building", "Build utility (build.exe), building DbgEng extensions"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Building DbgEng Extensions


## <span id="ddk_building_dbgeng_extensions_dbx"></span><span id="DDK_BUILDING_DBGENG_EXTENSIONS_DBX"></span>


All debugger extensions should be compiled and built by using Visual Studio. The Build utility is no longer used with debugger extensions.

For documentation on the Building projects in Visual Studio refer to [Building C++ Projects in Visual Studio.](https://msdn.microsoft.com/library/7s88b19e.aspx)

To build an extension, use the following procedure:

**To build a debugger extension**

1.  Open the **dbgsdk.sln** sample project in Visual Studio.

2.  Check the include and lib file project settings. If *%debuggers%* represents the root of your Debugging Tools for Windows installation, they should be set as follows:

    ```
    Include Path 
    %debuggers%\sdk\inc
    Library Path
    %debuggers%\sdk\lib
    ```

    If you have moved these headers and libraries to a different location, specify that location instead.

3.  Select **Build** and then **Build Solution** from the menu in Visual Studio.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Building%20DbgEng%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




