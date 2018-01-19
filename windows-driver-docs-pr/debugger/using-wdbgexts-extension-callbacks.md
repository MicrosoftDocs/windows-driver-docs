---
title: Using WdbgExts Extension Callbacks
description: Using WdbgExts Extension Callbacks
ms.assetid: b9a2f30a-b09c-43eb-b105-a6b0ffdb1342
keywords: ["WdbgExts extensions, callbacks, using"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using WdbgExts Extension Callbacks


## <span id="ddk_using_wdbgexts_extension_callbacks_dbwx"></span><span id="DDK_USING_WDBGEXTS_EXTENSION_CALLBACKS_DBWX"></span>


When you write a WdbgExts extension DLL, you can export certain functions:

-   You must export a function named [*WinDbgExtensionDllInit*](https://msdn.microsoft.com/library/windows/hardware/ff561303). When the debugger loads your extension DLL, it first calls *WinDbgExtensionDllInit* and passes it three arguments.

    -   A pointer to a **WINDBG\_EXTENSION\_APIS64** structure, which contains pointers to functions that are implemented by the debugger and declared in Wdbgexts.h. You must copy the entire structure to a global variable that you create in your DLL.
    -   A major version number. You must copy the major version number to a global variable that you create in your DLL.
    -   A minor version number. You must copy the minor version number to a global variable that you create in your DLL.

    For example, you could create global variables named ExtensionApis, SavedMajorVersion, and SavedMinorVersion as shown in the following example.

    ```ManagedCPlusPlus
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

-   You must export a function called [*ExtensionApiVersion*](https://msdn.microsoft.com/library/windows/hardware/ff543968). The debugger calls this function and expects back a pointer to an **EXT\_API\_VERSION** structure that contains the version number of the extension DLL. The debugger uses this version number when executing commands like [**.chain**](-chain--list-debugger-extensions-.md) and [**version**](version--show-debugger-version-.md) that display the extension version number.

-   You can optionally export a function called [*CheckVersion*](https://msdn.microsoft.com/library/windows/hardware/ff539096). The debugger calls this routine every time you use an extension command. You can use this to print out version mismatch warnings when your DLL is of a slightly different version than the debugger, but not different enough to prevent it from running.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20WdbgExts%20Extension%20Callbacks%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




