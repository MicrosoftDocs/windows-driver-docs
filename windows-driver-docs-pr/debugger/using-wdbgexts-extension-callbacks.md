---
title: Using WdbgExts Extension Callbacks
description: Using WdbgExts Extension Callbacks
keywords: ["WdbgExts extensions, callbacks, using"]
ms.date: 05/23/2017
---

# Using WdbgExts Extension Callbacks


## <span id="ddk_using_wdbgexts_extension_callbacks_dbwx"></span><span id="DDK_USING_WDBGEXTS_EXTENSION_CALLBACKS_DBWX"></span>


When you write a WdbgExts extension DLL, you can export certain functions:

-   You must export a function named [*WinDbgExtensionDllInit*](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_extension_dll_init). When the debugger loads your extension DLL, it first calls *WinDbgExtensionDllInit* and passes it three arguments.

    -   A pointer to a **WINDBG\_EXTENSION\_APIS64** structure, which contains pointers to functions that are implemented by the debugger and declared in Wdbgexts.h. You must copy the entire structure to a global variable that you create in your DLL.
    -   A major version number. You must copy the major version number to a global variable that you create in your DLL.
    -   A minor version number. You must copy the minor version number to a global variable that you create in your DLL.

    For example, you could create global variables named ExtensionApis, SavedMajorVersion, and SavedMinorVersion as shown in the following example.

    ```cpp
    WINDBG_EXTENSION_APIS64 ExtensionApis;
    USHORT SavedMajorVersion;
    USHORT SavedMinorVersion;

    VOID WinDbgExtensionDllInit(PWINDBG_EXTENSION_APIS64 lpExtensionApis,
        USHORT MajorVersion, USHORT MinorVersion)
    {
       ExtensionApis = *lpExtensionApis;
       SavedMajorVersion = MajorVersion;
       SavedMinorVersion = MinorVersion;
        ...
    }
    ```

-   You must export a function called [*ExtensionApiVersion*](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_extension_api_version). The debugger calls this function and expects back a pointer to an **EXT\_API\_VERSION** structure that contains the version number of the extension DLL. The debugger uses this version number when executing commands like [**.chain**](../debuggercmds/-chain--list-debugger-extensions-.md) and [**version**](../debuggercmds/version--show-debugger-version-.md) that display the extension version number.

-   You can optionally export a function called [*CheckVersion*](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_check_version). The debugger calls this routine every time you use an extension command. You can use this to print out version mismatch warnings when your DLL is of a slightly different version than the debugger, but not different enough to prevent it from running.

 

