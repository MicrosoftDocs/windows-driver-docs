---
title: INF RegisterDlls directive
description: A RegisterDlls directive references one or more INF sections used to specify files that are OLE controls and require self-registration.
keywords:
- INF RegisterDlls Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF RegisterDlls Directive
api_type:
- NA
ms.date: 07/17/2023
---

# INF RegisterDlls directive

[!INCLUDE [Caution invalid INF directive](../includes/inf-directive-invalid-22h2.md)]
 
> [!NOTE]
> You can use the [Reg2inf tool](../devtest/reg2inf.md) to convert existing [INF RegisterDlls directives](../install/inf-registerdlls-directive.md) into [INF AddReg directives](../install/inf-addreg-directive.md) in order to make a driver package universal.

A **RegisterDlls** directive references one or more INF sections used to specify files that are OLE controls and require self-registration.

```inf
[DDInstall]
  
RegisterDlls=register-dll-section[,register-dll-section]...
```

Each INF section referenced by a **RegisterDlls** directive must have the following entry format:

```inf
[register-dll-section] 
  
dirid,[subdir],filename,registration-flags[,[timeout][,argument]] 
```

A *register-dll-section* can have any number of entries, each on a separate line.

## Entries

*dirid*  
Specifies the destination directory ID of the file to be registered. For more information, see [Using Dirids](using-dirids.md).

*subdir*  
Specifies the directory path, relative to the current directory, to the file to be registered. If not specified, the file is in the current directory.

*filename*  
Identifies the file name of the OLE control to be registered.

*registration-flags*  
Indicates the registration operations to perform on the OLE control. One or both of the following flags must be specified.

**0x00000001** (FLG_REGSVR_DLLREGISTER)  
Call the OLE control's **DllRegisterServer** function (described in the Windows SDK documentation).

**0x00000002** (FLG_REGSVR_DLLINSTALL)  
Call the OLE control's **DllInstall** function (described in the Windows SDK documentation).

*timeout*  
Specifies the time-out, in units of seconds, for an OLE Control to complete the specified registration calls. The default time-out is 60 seconds.

*argument*  
If the control is an executable file, this is a command string that is passed to the executable. The default argument is **/RegServer**.

If the control is not an executable file, this specifies the command-line argument to pass to the **DllInstall** function.

## Remarks

Each *register-dll-section* name must be unique to the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

The following rules apply to the use of the **RegisterDlls** directive for device installations:

- Although the syntax permits filename to be either a DLL or an executable file, for device installations only a DLL is allowed.

- The code to be registered must not prompt for user input.

- Server-side installations execute in a system context. Therefore, you must be very sure that the code being registered contains no security vulnerabilities and that file permissions prevent the code from being maliciously modified.

For more information about OLE controls and self registration, see the Windows SDK documentation.

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

[**UnregisterDlls**](inf-unregisterdlls-directive.md)
