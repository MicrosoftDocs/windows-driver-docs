---
title: Reg2inf
description: Reg2inf is a tool that converts registry keys to make a driver package universal.
ms.date: 07/25/2023
---

# Reg2inf

The driver package INF registry conversion tool (`reg2inf.exe`) converts a registry key and its values or a COM .dll implementing a **[DllRegisterServer](/windows/win32/api/olectl/nf-olectl-dllregisterserver)** routine into a set of [INF AddReg directives](../install/inf-addreg-directive.md) or [INF DDInstall.COM section](../install/inf-ddinstall-com-section.md) for in-proc COM servers for inclusion into a driver package INF file. This tool is particularly useful for converting existing [INF RegisterDlls directives](../install/inf-registerdlls-directive.md) into INF AddReg directives or INF DDInstall.COM sections in order to make an INF file universal. For more info about universal INF files, see [Using a Universal INF File](../install/using-a-universal-inf-file.md).

Starting in Windows 10 version 1709, the tool ships as part of the WDK 10 installation. You can find it in the `\tools` subdirectory of your WDK 10 installation, for example `C:\Program Files(x86)\Windows Kits\10\tools\`.

While Reg2inf attempts to generate a COM registration, it may not capture the full registry state that the COM registration provides. As always, you should inspect the output of the tool for completeness and correctness and test the results.

## Running Reg2inf from the command line

This section lists the command line options for Reg2inf.

``` cmd
USAGE: reg2inf.exe [/downlevel]  [/key <path> | /dll <filename>] [/targetkey <path>]

/downlevel
    Ignores DDInstall.COM syntax style and prints the output only through AddReg directives. Should be used only for Windows 11 version older than <TBD>

/key <registry key path>
    Process a specific registry key, for example: reg2inf /key HKEY_LOCAL_MACHINE\SOFTWARE\Fabrikam

/dll <module filename>
    Process a COM DLL module that implements DllRegisterServer entrypoint, typically called by regsvr32 or legacy INF RegisterDlls directive in order to register COM class under HKEY_CLASSES_ROOT, for example: reg2inf /dll %SystemRoot%\System32\fabkobj.dll

/targetkey <registry key path>
    Remap target registry key to be under a different base key path, for example: reg2inf /key HKLM\SYSTEM\Temp /targetkey HKR\Parameters

```

> [!NOTE]
> Reg2inf requires that the full path length must not exceed 259 characters.

## Registering a COM component in an INF file

The following snippet shows how to register a simple COM class using INF DDInstall.COM syntax, as produced by Reg2inf *without* the `/downlevel` parameter:

``` inf
[SimpleCom.COM]
AddComServer = COM_Server,,SimpleCom_Install

[SimpleCom_Install]
ServerType = 1
ServerBinary = %13%\comobj.dll
AddComClass = Sample Class,{92FCF37F-F6C7-4F8A-AA09-1A14BA118084},,SimpleCom_Class_Install

[SimpleCom_Class_Install]
ThreadingModel = Both
```

The following snippet shows how to register a simple COM class using INF AddReg syntax, as produced by Reg2inf *with* the `/downlevel` parameter:

```inf
[ComClass_AddReg]
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084},,,"Sample Class"
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}\InprocServer32,,%REG_EXPAND_SZ%,"%13%\comobj.dll"
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}\InprocServer32,ThreadingModel,,"Both"
```
