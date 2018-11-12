---
title: Example 8 Enlarging the User-Mode Stack Trace Database
description: Example 8 Enlarging the User-Mode Stack Trace Database
ms.assetid: b04f6b86-a210-4941-a4eb-a9059d9890d9
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 8: Enlarging the User-Mode Stack Trace Database


## <span id="ddk_example_8___enlarging_the_user_mode_stack_trace_database_dtools"></span><span id="DDK_EXAMPLE_8___ENLARGING_THE_USER_MODE_STACK_TRACE_DATABASE_DTOOLS"></span>


The following GFlags command increases the maximum size of the user-mode stack trace database for myapp.exe, a fictitious program, from 8 MB to 24 MB.

The command uses the **/i** parameter to specify the image file. It uses the **/tracedb** parameter to set the maximum stack trace database size and the value 24 to indicate the size in megabytes. The command uses decimal units. (Hexadecimal units are not valid.)

```console
gflags /i MyApp.exe /tracedb 24
```

As the following error message indicates, this command fails because the [Create user mode stack trace database](create-user-mode-stack-trace-database.md) (+ust) flag is not set for the MyApp image file. You cannot set the size of a trace database until you create one.

```console
Failed to set the trace database size for `MyApp.exe'
```

The following commands fix the error. The first command creates a trace database for myapp.exe and the second command sets the maximum size of the trace database to 24 MB. These commands cannot be combined into a single command. The following display shows the commands and the success message from GFlags.

```console
gflags /i MyApp.exe +ust

Current Registry Settings for MyApp.exe executable are: 00001000
    ust - Create user mode stack trace database

gflags /i MyApp.exe /tracedb 24

Trace database size for `MyApp.exe' set to 24 Mb.
```

GFlags can change the size of the user-mode stack trace database, but it does not display it. To display the trace database size, use registry APIs, Regedit, or Reg (reg.exe), a tool included in Windows XP and Windows Server 2003, to check the value of the **StackTraceDatabaseSizeInMB** registry entry (HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\*ImageFileName*\\**StackTraceDatabaseSizeInMB**).

(A version of Reg is included in Windows XP, but that version does not permit the **/v** and **/s** switches in the same command.)

The following command uses Reg to query the value of **StackTraceDatabaseSizeInMB**:

```console
reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\MyApp.exe" /v StackTraceDatabaseSizeInMB 
```

In response, Reg displays the value of **StackTraceDatabaseSizeInMB**, which confirms that the new value, 24 (0x18), was set. This value becomes effective when you restart myapp.exe.

```console
! REG.EXE VERSION 3.0

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\MyApp.exe
    StackTraceDatabaseSizeInMB  REG_DWORD       0x18
```

**Tip**   Type the **reg query** command into Notepad, then save the file as tracedb.bat. Thereafter, to display the value of **StackTraceDatabaseSizeInMB**, just type **TraceDb**.

 

 

 





