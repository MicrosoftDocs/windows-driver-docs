---
title: 'WinDbg: Restricted Mode'
description: "Restricted mode limits the types of debugging sessions that WinDbg can start to remote debugging sessions and dump files only. "
keywords: ["Restricted Mode", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 08/09/2021
ms.topic: how-to
---

# WinDbg: Restricted mode

## Restricted mode

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This article describes how to enable the restricted mode feature that restricts the type of debugging sessions that you can start.

With WinDbg, you can start various debugging session types. In some circumstances, you might not want WinDbg to start certain debugging sessions. Restricted mode limits the types of debugging sessions that WinDbg can start to only remote debugging sessions and loading dump files.

To enable restricted mode, you can use a Windows Defender Application Control policy or the registry key.

## Configuration by using Windows Defender Application Control

You can enable restricted mode by using a Windows Defender Application Control policy. A Windows Defender Application Control policy can prevent local administrators from altering policy settings after a policy is deployed. To enable restricted mode by using a Windows Defender Application Control policy, configure your policy with the following setting:

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

## Configuration by using the registry key

To enable restricted mode by using the registry key, set the registry key `HKLM\SOFTWARE\Microsoft\WinDbg\EnableRestrictedMode` to the `DWORD` value of `1`.

This example command shows how to use the [reg add command](/windows-server/administration/windows-commands/reg-add) to add the key and set it to a value of `1`.

```powershell
PS C:\WINDOWS\system32> reg add HKLM\SOFTWARE\Microsoft\WinDbg /v EnableRestrictedMode /t REG_DWORD /d 1
The operation completed successfully.
```

## Related content

- [WinDbg features](../debugger/debugging-using-windbg-preview.md)
- [WinDbg: Command-line startup options](windbg-command-line-preview.md)