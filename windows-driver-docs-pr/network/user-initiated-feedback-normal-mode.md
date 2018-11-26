---
title: User-initiated feedback - normal mode
description: This topic describes normal mode for user-initiated feedback with IHV trace logging in WDI drivers.
ms.assetid: 723732A3-4B24-4FE5-B338-B8443F287FDE
ms.date: 06/15/2018
ms.localizationpriority: medium
---

# User-initiated feedback - normal mode

In the normal user-initiated feedback (UIF) scenario, a user experiences a problem with Wi-Fi and submits a feedback report. This report collects a snapshot of the Wi-Fi subsystem, including Wi-Fi WMI auto-loggers, network statistics, etc. To collect IHV-specific logs, Microsoft provides a WMI auto-logger session with no initial ETW providers. Each IHV adds their set of ETW providers under the Microsoft-provided WMI auto-logger session registry entry. When the UIF report is submitted, the IHV auto-logger ETL is collected and sent to Microsoft for analysis. This log file is implemented using a circular buffer with a somewhat limited size (\<= 1MB). The events saved in this log file should be appropriately throttled via flags/level/keywords to ensure that at least the past 30 minutes of the log events are always saved.

## Microsoft-provided WMI auto-logger session

Microsoft provides a WMI auto-logger session with no initial ETW providers. When the IHV's drivers are installed, they must add the required WMI provider registry keys under the Microsoft-provided WMI auto-logger session key. The IHV should not change any of the auto-logger session registry values. However, all ETW provider options are available to the IHV including enable level, match any, match all, etc. This logging session always runs and has a limited circular buffer, so IHVs should set the provider EnableLevels appropriately.

The WMI auto-logger session is added to the HKLM registry hive with the following path:

`HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession`

The resulting ETL log file is located here:

`%SystemDrive%\System32\LogFiles\WMI\WifiDriverIHVSession.etl`

## IHV driver INF changes

IHVs need to update their driver INF files to add the following registry key values so they can get verbose IHV logs during UIF normal mode. The following snippets provide a template for adding a single ETW provider to the auto-logger session. An IHV may add as many providers as they see fit. In addition, the enable level values are IHV-specific per ETW provider, so they don't have to necessarily be the same as the Microsoft-defined values (TRACE_LEVEL_CRITICAL, TRACE_LEVEL_ERROR, etc.).

### Enable the IHV auto-logger session

Because the IHV auto-logger session is initialized with no ETW providers, it is disabled by default. IHVs are required to enable this session by updating the "Start" value to **1** in their driver's INF file, as shown in this example:

```INF
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession,Start,%REG_DWORD%,1
```

### Add IHV ETW providers

The following snippet shows how to add IHV ETW providers in the INF file:

```INF
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession\<IHVProviderGUID_1>,Enabled,%REG_DWORD%,1
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession\<IHVProviderGUID_1>,,EnableLevel,%REG_DWORD%,<IHV_LogEnableLevelValue>
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession\<IHVProviderGUID_1>,MatchAnyKeyword,%REG_QWORD%,<IHV_MatchAnyKewordValue>

[The following is optional]
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession\<IHVProviderGUID_1>,MatchAllKeyword,%REG_QWORD%,<IHV_MatchAllKewordValue>

[Strings]
REG_DWORD = 0x00010001
REG_QWORD = 0x000B0001
```

### Example values

This example illustrates a Native Wi-Fi custom level setting (enable all) with all Native Wi-Fi keywords:

```INF
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession\{0BD3506A-9030-4f76-9B88-3E8FE1F7CFB6},Enabled,%REG_DWORD%,1
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession\{0BD3506A-9030-4f76-9B88-3E8FE1F7CFB6},,EnableLevel,%REG_DWORD%,0x04
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession\{0BD3506A-9030-4f76-9B88-3E8FE1F7CFB6},MatchAnyKeyword,%REG_QWORD%,0x000FFFFF

Standard EnableLevel values:
0x5 - Verbose
0x4 - Informational
0x3 - Warning
0x2 - Error
0x1 - Critical
0x0 – LogAlways
```

## Related links

[User-initiated feedback with IHV trace logging](user-initiated-feedback-with-ihv-trace-logging.md)

[User-initiated feedback - repro mode](user-initiated-feedback-repro-mode.md)
