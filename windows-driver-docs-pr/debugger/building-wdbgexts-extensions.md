---
title: Building WdbgExts Extensions
description: Building WdbgExts Extensions
ms.assetid: a3923de6-bed5-40e0-a9cb-99e0f4354448
keywords: ["Build utility (build.exe), building WdbgExts extensions", "WdbgExts extensions, building", "WdbgExts extensions, compiling"]
ms.author: domars
ms.date: 10/22/2018
ms.localizationpriority: medium
---

# Building WdbgExts Extensions


## <span id="ddk_building_wdbgexts_extensions_dbwx"></span><span id="DDK_BUILDING_WDBGEXTS_EXTENSIONS_DBWX"></span>


All debugger extensions should be compiled and built with the Build utility. The Build utility is included in the Windows Driver Kit (WDK) and in earlier versions of the Windows DDK.

Note the following points:

-  The WDK has several different build environment windows. Each of these has a corresponding shortcut placed in the **Start** menu when the WDK is installed. To build a debugger extension, you must use the latest Windows build environment, regardless of what platform you will be running the extension on.

-  The Build utility is usually not able to compile code that is located in a directory path that contains spaces. Your extension code should be located in a directory whose full path contains no spaces. (In particular, this means that if you install Debugging Tools for Windows to the default location -- Program Files\\Debugging Tools for Windows -- you will not be able to build the sample extensions.)

**To build a debugger extension**

1. Open the window for the latest Windows build environment. (You can choose either the "free" version or the "checked" version -- they will give identical results unless you have put **\#ifdef DBG** statements in your code.)

2. Set the variable \_NT\_TARGET\_VERSION to indicate the oldest version of Windows on which you want to run the extension. \_NT\_TARGET\_VERSION can be set to the following values.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Value</th>
    <th align="left">Versions of Windows</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>_NT_TARGET_VERSION_WIN2K</p></td>
    <td align="left"><p>Windows 2000 and later.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>_NT_TARGET_VERSION_WINXP</p></td>
    <td align="left"><p>Windows XP and later.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>_NT_TARGET_VERSION_WS03</p></td>
    <td align="left"><p>Windows Server 2003 and later.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>_NT_TARGET_VERSION_LONGHORN</p></td>
    <td align="left"><p>Windows Vista and later.</p></td>
    </tr>
    </tbody>
    </table>

     

 If \_NT\_TARGET\_VERSION is not set, the extension will only run on the version of Windows for which the build window was opened (and later versions). For example, putting the following line in your Sources file will build an extension that will run on Windows:
    ```console
    _NT_TARGET_VERSION = $(_NT_TARGET_VERSION_WINXP) 
    ```

3. Set the DBGSDK\_INC\_PATH and DBGSDK\_LIB\_PATH environment variables to specify the paths to the debugger SDK headers and the debugger SDK libraries, respectively. If *%debuggers%* represents the root of your Debugging Tools for Windows installation, these variables should be set as follows:

    ```console
    set DBGSDK_INC_PATH=%debuggers%\sdk\inc
    set DBGSDK_LIB_PATH=%debuggers%\sdk\lib
    ```

    If you have moved these headers and libraries to a different location, specify that location instead.

4. Change the current directory to the directory that contains your extension's Dirs file or Sources file.

5. Run the Build utility:

    ```console
    build -cZMg
    ```

For a full explanation of these steps, and for a description of how to create a Dirs file and a Sources file, see the Build utility documentation in the WDK.

 

 





