---
title: "!logexts.logm"
description: "The !logexts.logm extension creates or displays a module inclusion list or a module exclusion list."
keywords: ["!logexts.logm Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- logexts.logm
api_type:
- NA
---

# !logexts.logm


The **!logexts.logm** extension creates or displays a module inclusion list or a module exclusion list.

```dbgcmd
!logexts.logm i Modules 
!logexts.logm x Modules 
!logexts.logm 
```

## Parameters


<span id="_______i______"></span><span id="_______I______"></span> **i**   
Causes Logger to use a module inclusion list. It will consist of the specified *Modules*.

<span id="_______x______"></span><span id="_______X______"></span> **x**   
Causes Logger to use a module exclusion list. It will consist of Logexts.dll, kernel32.dll, and the specified *Modules*.

<span id="_______Modules______"></span><span id="_______modules______"></span><span id="_______MODULES______"></span> *Modules*   
Specifies the modules to be included or excluded. This list is not cumulative; each use of this command creates an entirely new list. If multiple modules are listed, separate them with spaces. An asterisk (\*) can be used to indicate all modules.

## DLL

Logexts.dll

 

## Additional Information

For more information, see [Logger and LogViewer](../debugger/logger-and-logviewer.md).

## Remarks

With no parameters, the **!logexts.logm** extension displays the current inclusion list or exclusion list.

The extensions **!logexts.logm x \\*** and **!logexts.logm i** are equivalent: they result in a completely empty inclusion list.

The extensions **!logexts.logm i \\*** and **!logexts.logm x** are equivalent: they result in an exclusion list that contains only Logexts.dll and kernel32.dll. These two modules are always excluded, because Logger is not permitted to log itself.

Here are some examples:

```dbgcmd
0:001> !logm
Excluded modules:
  LOGEXTS.DLL      [mandatory]
  KERNEL32.DLL     [mandatory]
  USER32.DLL
  GDI32.DLL
  ADVAPI32.DLL

0:001> !logm x winmine.exe
Excluded modules:
  Logexts.dll      [mandatory]
  kernel32.dll     [mandatory]
  winmine.exe

0:001> !logm x user32.dll gdi32.dll
Excluded modules:
  Logexts.dll      [mandatory]
  kernel32.dll     [mandatory]
  user32.dll
  gdi32.dll

0:001> !logm i winmine.exe mymodule2.dll
Included modules:
  winmine.exe
  mymodule2.dll
```

