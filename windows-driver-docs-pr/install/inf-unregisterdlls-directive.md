---
title: INF UnregisterDlls directive
description: An UnregisterDlls directive references one or more INF sections used to specify files that are OLE controls and require self-unregistration (self-removal).
keywords:
- INF UnregisterDlls Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF UnregisterDlls Directive
api_type:
- NA
ms.date: 07/11/2022
---

# INF UnregisterDlls directive

> [!NOTE]
> If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

An **UnregisterDlls** directive references one or more INF sections used to specify files that are OLE controls and require self-unregistration (self-removal).

```inf
[DDInstall]
  
UnregisterDlls=unregister-dll-section[,unregister-dll-section]...
```

Each INF section referenced by an **UnregisterDlls** directive must have the following entry format:

```inf
[unregister-dll-section] 
  
dirid,[subdir],filename,registration-flags[,[timeout][,argument]] 
```

An *unregister-dll-section* can have any number of entries, each on a separate line.

## Entries

*dirid*  
Specifies the destination directory ID of the file to be unregistered. For more information, see [Using Dirids](using-dirids.md).

*subdir*  
Specifies the directory path, relative to the current directory, to the file to be unregistered. If not specified, the file is in the current directory.

*filename*  
Identifies the file name of the OLE control to be unregistered.

*registration-flags*  
Indicates the registration operations to perform on the OLE control. One or both of the following flags must be specified.

**0x00000001** (FLG_REGSVR_DLLREGISTER)  
Call the **DllUnRegisterServer** function (described in the Windows SDK documentation).

**0x00000002** (FLG_REGSVR_DLLINSTALL)  
Call the OLE control's **DllInstall** function (described in the Windows SDK documentation).

*timeout*  
Specifies the time-out, in units of seconds, for an OLE Control to complete the specified unregistration calls. The default time-out is 60 seconds.

*argument*  
If the control is an executable file, this is a command string that is passed to the executable. The default argument is **/UnRegServer**.

If the control is not an executable file, this specifies the command-line argument to pass to the **DllInstall** function.

## Remarks

Each *unregister-dll-section* name must be unique to the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

For more information about OLE controls and self unregistration, see the Windows SDK documentation.

## Examples

```inf
[Dialer]
RegisterDlls = DialerRegSvr

[DialerUninstall]
UnregisterDlls = DialerRegSvr

[DialerRegSvr]
11,,avtapi.dll, 1
```

## See also

[**RegisterDlls**](inf-registerdlls-directive.md)
