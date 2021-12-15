---
title: Reg2inf
description: Reg2inf is a tool that converts registry keys to make a driver package universal.
ms.date: 04/28/2020
---

# Reg2inf
 
The Driver Package INF Registry Conversion Tool (`reg2inf.exe`) tool converts a registry key and its values or a COM .dll implementing a [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver) routine into a set of [INF AddReg directives](../install/inf-addreg-directive.md) for inclusion into a driver package INF file.  This tool is particularly useful for converting existing [INF RegisterDlls directives](../install/inf-registerdlls-directive.md) into INF AddReg directives in order to make an INF file universal.  For more info about universal INF files, see [Using a Universal INF File](../install/using-a-universal-inf-file.md).
 
Starting in Windows 10 version 1709, the tool ships as part of the WDK 10 installation. You can find it in the \tools subdirectory of your WDK 10 installation, for example `c:\Program Files(x86)\Windows Kits\10\tools\`. 

While Reg2inf attempts to generate a COM registration, it may not capture the full registry state that the COM registration provides. As always, you should inspect the output of the tool for completeness and correctness, and test the results. 

## Running Reg2inf from the command line 
 
This section lists the command line options for Reg2inf.

```
USAGE: reg2inf.exe [/key <path> | /dll <filename>] [/targetkey <path>]

/key <registry key path>
    Process a specific registry key, e.g.: reg2inf /key HKEY_LOCAL_MACHINE\SOFTWARE\Fabrikam
/dll <module filename>
    Process a COM DLL module that implements DllRegisterServer entrypoint, typically called by regsvr32 or legacy INF RegisterDlls directive in order to register COM class under HKEY_CLASSES_ROOT, e.g.: reg2inf /dll %SystemRoot%\System32\fabkobj.dll
/targetkey <registry key path>
    Remap target registry key to be under a different base key path, e.g.: reg2inf /key HKLM\SYSTEM\Temp /targetkey HKR\Parameters
```

**Note** Reg2inf requires that the full path length must not exceed 259 characters. 

## Registering a COM component in an INF file

The following snippet shows how to register a simple COM class using INF AddReg syntax, as produced by Reg2inf:

```cpp
[ComClass_AddReg]
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084},,,"Sample Class"
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}\InprocServer32,,%REG_EXPAND_SZ%,"%13%\comobj.dll"
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}\InprocServer32,ThreadingModel,,"Both"
```
