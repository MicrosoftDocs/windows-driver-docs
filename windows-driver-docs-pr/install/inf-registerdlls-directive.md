---
title: INF RegisterDlls Directive
description: A RegisterDlls directive references one or more INF sections used to specify files that are OLE controls and require self-registration.
ms.assetid: 59da13e6-f801-4efe-8cd3-d0305e503c24
keywords:
- INF RegisterDlls Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF RegisterDlls Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF RegisterDlls Directive


**Note**  If you are building a universal or mobile driver package, this directive is not valid. You can use the [Reg2inf tool](../devtest/reg2inf.md) to convert existing [INF RegisterDlls directives](../install/inf-registerdlls-directive.md) into [INF AddReg directives](../install/inf-addreg-directive.md) in order to make a driver package universal.  For more info, see [Using a Universal INF File](using-a-universal-inf-file.md).

A **RegisterDlls** directive references one or more INF sections used to specify files that are OLE controls and require self-registration.

```cpp
[DDInstall]
  
RegisterDlls=register-dll-section[,register-dll-section]...
```

Each INF section referenced by a **RegisterDlls** directive must have the following entry format:

```cpp
[register-dll-section] 
  
dirid,[subdir],filename,registration-flags[,[timeout][,argument]] 
```

A *register-dll-section* can have any number of entries, each on a separate line.

## Entries


<a href="" id="dirid"></a>*dirid*  
Specifies the destination directory ID of the file to be registered. For more information, see [Using Dirids](using-dirids.md).

<a href="" id="subdir"></a>*subdir*  
Specifies the directory path, relative to the current directory, to the file to be registered. If not specified, the file is in the current directory.

<a href="" id="filename"></a>*filename*  
Identifies the file name of the OLE control to be registered.

<a href="" id="registration-flags"></a>*registration-flags*  
Indicates the registration operations to perform on the OLE control. One or both of the following flags must be specified.

<a href="" id="0x00000001--flg-regsvr-dllregister-"></a>**0x00000001** (FLG_REGSVR_DLLREGISTER)  
Call the OLE control's **DllRegisterServer** function (described in the Windows SDK documentation).

<a href="" id="0x00000002--flg-regsvr-dllinstall--"></a>**0x00000002** (FLG_REGSVR_DLLINSTALL)   
Call the OLE control's **DllInstall** function (described in the Windows SDK documentation).

<a href="" id="timeout"></a>*timeout*  
Specifies the time-out, in units of seconds, for an OLE Control to complete the specified registration calls. The default time-out is 60 seconds.

<a href="" id="argument"></a>*argument*  
If the control is an executable file, this is a command string that is passed to the executable. The default argument is **/RegServer**.

If the control is not an executable file, this specifies the command-line argument to pass to the **DllInstall** function.

Remarks
-------

Each *register-dll-section* name must be unique to the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

The following rules apply to the use of the **RegisterDlls** directive for device installations:

-   Although the syntax permits filename to be either a DLL or an executable file, for device installations only a DLL is allowed.
-   The code to be registered must not prompt for user input.
-   Server-side installations execute in a system context. Therefore, you must be very sure that the code being registered contains no security vulnerabilities and that file permissions prevent the code from being maliciously modified.

For more information about OLE controls and self registration, see the Windows SDK documentation.

Examples
--------

```cpp
[Dialer]
RegisterDlls = DialerRegSvr
[DialerUninstall]
UnregisterDlls = DialerRegSvr
[DialerRegSvr]
11,,avtapi.dll, 1
```

## See also


[**UnregisterDlls**](inf-unregisterdlls-directive.md)

 

 






