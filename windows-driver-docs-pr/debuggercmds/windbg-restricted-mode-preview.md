---
title: WinDbg - Restricted Mode
description: Restricted Mode limits the types of debugging sessions WinDbg can start to remote debugging sessions and dump files only. 
ms.date: 08/09/2021
---

# WinDbg - Restricted Mode

## Restricted Mode

![Small logo on WinDbg.](images/windbgx-preview-logo.png)

This section describes how to enable the restricted mode feature that restricts the type of debugging sessions that can be started.  

WinDbg provides you the ability to start a variety of debugging session types. However, in some circumstances you may not want WinDbg to be able to start certain debugging sessions. Restricted Mode limits the types of debugging sessions WinDbg can start to only remote debugging sessions and loading dump files. 

Restricted mode can be enabled by Windows Defender Application Control (WDAC) policy or by registry key.

## Configuration using Windows Defender Application Control (WDAC)
 
Restricted mode can be enabled by Windows Defender Application Control (WDAC) policy. WDAC policy can prevent local administrators from altering policy settings after a policy has been deployed. To enable restricted mode by WDAC policy, configure your policy with the following setting:

```xml
<Settings>
    <!-- Other settings -->
    <Setting Provider="Microsoft.WindbgX" Key="Settings" ValueName="EnableRestrictedMode">
        <Value>
            <Boolean>true</Boolean>
        </Value>
    </Setting>
</Settings>
```

##  Configuration using Registry Key

To enable restricted mode by registry key, set this registry key `HKLM\SOFTWARE\Microsoft\WinDbg\EnableRestrictedMode` to the DWORD value of 1.

This example command shows how to use the [reg add command](/windows-server/administration/windows-commands/reg-add) to add the key and set it to a value of 1.

```powershell
PS C:\WINDOWS\system32> reg add HKLM\SOFTWARE\Microsoft\WinDbg /v EnableRestrictedMode /t REG_DWORD /d 1
The operation completed successfully.
```

## See Also

[WinDbg Features](../debugger/debugging-using-windbg-preview.md)

[WinDbg – Command line startup options](windbg-command-line-preview.md)
