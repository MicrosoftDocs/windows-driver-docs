---
title: WinDbg Preview - LockedDownMode
description: This section describes how to use LockedDownMode in the WinDbg preview debugger.
ms.date: 06/28/2021
ms.localizationpriority: medium
---

# WinDbg Preview - Locked Down Mode

This section describes how to use Locked Down Mode in the WinDbg preview debugger. 

## Locked Down Mode

WinDbg preview can be configured in Locked Down Mode. Locked Down Mode restricts the use of various debug targets and is intended to be used in environments where certain debug targets, such as "Attach to local process", may be a risk and should be disabled. Configuring WinDbg preview in this mode disables starting any debug session except "Connect to remote debugger" and "Open dump file".

## Configuring Locked Down Mode

Locked Down Mode can be enabled via a registry key or via a [Windows Defender Application Control policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control). 

### Configuration with Registry Key 

Locked Down Mode can be enabled by setting the registry key ```HKLM\SOFTWARE\Microsoft\WinDbg\EnableLockedDownMode``` to the DWORD value ```1```

### Configuration with Windows Defender Application Control Policy

Locked Down Mode can be enabled by adding the following setting to your WDAC policy:

```
<Settings>
    <!-- Other settings -->
    <Setting Provider="Microsoft.WindbgX" Key="Settings" ValueName=“EnableLockedDownMode">
        <Value>
            <Boolean>true</Boolean>
        </Value>
    </Setting>
</Settings>
```
