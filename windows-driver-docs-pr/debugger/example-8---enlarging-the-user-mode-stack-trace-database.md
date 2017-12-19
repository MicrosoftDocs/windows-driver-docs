---
title: Example 8 Enlarging the User-Mode Stack Trace Database
description: Example 8 Enlarging the User-Mode Stack Trace Database
ms.assetid: b04f6b86-a210-4941-a4eb-a9059d9890d9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Example 8: Enlarging the User-Mode Stack Trace Database


## <span id="ddk_example_8___enlarging_the_user_mode_stack_trace_database_dtools"></span><span id="DDK_EXAMPLE_8___ENLARGING_THE_USER_MODE_STACK_TRACE_DATABASE_DTOOLS"></span>


The following GFlags command increases the maximum size of the user-mode stack trace database for myapp.exe, a fictitious program, from 8 MB to 24 MB.

The command uses the **/i** parameter to specify the image file. It uses the **/tracedb** parameter to set the maximum stack trace database size and the value 24 to indicate the size in megabytes. The command uses decimal units. (Hexadecimal units are not valid.)

```
gflags /i MyApp.exe /tracedb 24
```

As the following error message indicates, this command fails because the [Create user mode stack trace database](create-user-mode-stack-trace-database.md) (+ust) flag is not set for the MyApp image file. You cannot set the size of a trace database until you create one.

```
Failed to set the trace database size for `MyApp.exe'
```

The following commands fix the error. The first command creates a trace database for myapp.exe and the second command sets the maximum size of the trace database to 24 MB. These commands cannot be combined into a single command. The following display shows the commands and the success message from GFlags.

```
gflags /i MyApp.exe +ust

Current Registry Settings for MyApp.exe executable are: 00001000
    ust - Create user mode stack trace database

gflags /i MyApp.exe /tracedb 24

Trace database size for `MyApp.exe' set to 24 Mb.
```

GFlags can change the size of the user-mode stack trace database, but it does not display it. To display the trace database size, use registry APIs, Regedit, or Reg (reg.exe), a tool included in Windows XP and Windows Server 2003, to check the value of the **StackTraceDatabaseSizeInMB** registry entry (HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\*ImageFileName*\\**StackTraceDatabaseSizeInMB**).

(A version of Reg is included in Windows XP, but that version does not permit the **/v** and **/s** switches in the same command.)

The following command uses Reg to query the value of **StackTraceDatabaseSizeInMB**:

```
reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\MyApp.exe" /v StackTraceDatabaseSizeInMB 
```

In response, Reg displays the value of **StackTraceDatabaseSizeInMB**, which confirms that the new value, 24 (0x18), was set. This value becomes effective when you restart myapp.exe.

```
! REG.EXE VERSION 3.0

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\MyApp.exe
    StackTraceDatabaseSizeInMB  REG_DWORD       0x18
```

**Tip**   Type the **reg query** command into Notepad, then save the file as tracedb.bat. Thereafter, to display the value of **StackTraceDatabaseSizeInMB**, just type **TraceDb**.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%208:%20%20Enlarging%20the%20User-Mode%20Stack%20Trace%20Database%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




