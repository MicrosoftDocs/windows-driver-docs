---
title: User-initiated feedback - repro mode
description: This topic describes repro mode for user-initiated feedback with IHV trace logging in WDI drivers.
ms.assetid: C9784C2D-75B1-4229-A219-748C52F430D5
ms.date: 06/15/2018
ms.localizationpriority: medium
---

# User-initiated feedback - repro mode

User-initiated feedback (UIF) repro mode permits the system to collect more verbose logging while the user reproduces the bug. Like UIF normal mode, this is also accomplished by creating a new WMI logging session with IHV-defined ETW providers. After the repro mode is complete, the verbose logs are gathered and sent to Microsoft for analysis. There are IHV extension points for enabling or disabling verbose firmware logs. Repro logs are intended to be more verbose to be able to track down the reason the customer is having a problem. Therefore, the log file size for the repro mode log is set at a maximum size of 10MB. The IHV should use more verbose settings for ETW provider flags/level/keywords values.

The current UIF repro mode model requires that Microsoft is notified of all provider GUIDs, levels, and flags before the IHV feedback logs are included. Adding the providers to the registry, as indicated in this topic, enables an IHV to test the logs for appropriate levels.

## Microsoft-provided WMI auto-logger session

Microsoft provides a WMI auto-logger session with no initial ETW providers. When the IHV's drivers are installed, they must add the required WMI provider registry keys under the Microsoft-provided WMI auto-logger session key. The IHV should not change any of the auto-logger session registry values. However, all ETW provider options are available to the IHV including enable level, match any, match all, etc.

> [!IMPORTANT]
> The auto-logger is never enabled as an auto-logger. These values are used to validate the repro mode IHV logging described in [Testing the repro mode logs](#testing-the-repro-mode-logs). In addition, we might ask users to submit these logs manually by using the `netsh` tool. The provider GUIDs, level, and flags must also be submitted to Microsoft, along with a sample of the logs, so they will be included in repro mode UIFs (see [Submitting IHV providers to Microsoft](#submitting-ihv-providers-to-microsoft).

The WMI auto-logger session is added to the HKLM registry hive with the following path:

`HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSessionRepro`

The resulting ETL log file is located here:

`%SystemDrive%\System32\LogFiles\WMI\WifiDriverIHVSessionRepro.etl`

## IHV driver INF changes

IHVs need to update their driver INF files to add the following registry key values so they can get verbose IHV logs during UIF normal mode. The following snippets provide a template for adding a single ETW provider to the auto-logger session. An IHV may add as many providers as they see fit. In addition, the enable level values are IHV-specific per ETW provider, so they don't have to necessarily be the same as the Microsoft-defined values (TRACE_LEVEL_CRITICAL, TRACE_LEVEL_ERROR, etc.).

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

This example shows WDI UE informational level setting with all keywords:

```INF
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession\{21ba7b61-05f8-41f1-9048-c09493dcfe38},Enabled,%REG_DWORD%,1
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession\{21ba7b61-05f8-41f1-9048-c09493dcfe38},,EnableLevel,%REG_DWORD%,0xFF
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\WifiDriverIHVSession\{21ba7b61-05f8-41f1-9048-c09493dcfe38},MatchAnyKeyword,%REG_QWORD%,0x000FFFFF

Standard EnableLevel values:
0x5 - Verbose
0x4 - Informational
0x3 - Warning
0x2 - Error
0x1 - Critical
0x0 – LogAlways
```

## ETW control callback

An IHV can register for the ETW control callback in its ETW logging code. This enables the IHV to be notified when ETW providers are enabled, disabled, or a capture control is initiated. This way, the IHV can turn on or off verbose firmware logs for repro mode.

> [!NOTE]
> If the ETW providers are shared between normal and repro mode, the IHV should key off the IHV-defined EnableLevel, defined in the INF file, to start/stop verbose firmware logs.

### ETW callback function

The following snippet shows how to register for the ETW callback. This is only important if the IHV needs to take special action during the start and end of the UIF repro mode (like starting or stopping verbose firmware logging). If multiple ETW providers are used, IHVs might consider only implementing one callback to initiate firmware logging. All firmware logging must be routed to the IHV's ETW trace provider. The diagnostic tools for UIF will only collect traces for the IHV's ETW provider.

There are two ways to enable the ETW callback, depending on how you implemented ETW logging.

1. Manifested ETWs with autogenerated code via `MC.exe`. See [Writing an Instrumentation Manifest](https://msdn.microsoft.com/library/windows/desktop/dd996930) for more details.
    1. The header in the following snippet (etwtracingevents.h) is an autogenerated ETW event header that was created via `MC.exe`. It is assumed that the ETW events have already been generated, so this topic will not focus on this part.
    1. MCGEN_PRIVATE_ENABLE_CALLBACK_V2 must be defined before including the autogenerated ETW header. Otherwise, the callback will not be called.
1. Registering for the ETW callback via the [**EventRegister**](https://msdn.microsoft.com/library/windows/desktop/aa363744) API.
    1. The ETW callback provider must be passed to the **EventRegister** function when registering the trace provider.

This snippet shows the prototype for the ETW callback function.

```C++
#include <evntprov.h>
extern
VOID
EtwEventControlCallback(
    _In_ LPCGUID SourceId,
    _In_ ULONG ControlCode,
    _In_ UCHAR Level,
    _In_ ULONGLONG MatchAnyKeyword,
    _In_ ULONGLONG MatchAllKeyword,
    _In_opt_ PEVENT_FILTER_DESCRIPTOR FilterData,
    _Inout_opt_ PVOID CallbackContext
    );
```

The following code is only required if you used autogenerated ETW events using the `MC.exe` tool.

```C++
#define MCGEN_PRIVATE_ENABLE_CALLBACK_V2 EtwEventControlCallback

#include "etwtracingEvents.h" // Generated from manifest - This must come 
                              // after MCGEN_PRIVATE_ENABLE_CALLBACK_V2 is                   
                              // defined
```

The *ControlCode* parameter of the ETW callback indicates when the provider is enabled or disabled. The values are defined in `<evntrace.h>` and have the following values:

```C++
#define EVENT_CONTROL_CODE_DISABLE_PROVIDER 0
#define EVENT_CONTROL_CODE_ENABLE_PROVIDER  1
#define EVENT_CONTROL_CODE_CAPTURE_STATE    2
```

#### EVENT_CONTROL_CODE_ENABLE_PROVIDER

This flag enables the ETW provider and indicates that the UIF repro mode session has started. This should be used to initiate verbose firmware logging and/or packet logging.

#### EVENT_CONTROL_CODE_DISABLE_PROVIDER

This flag disables the ETW provider and indicates that the UIF repro mode session has ended. The IHV's implementation should flush and reset firmware logs at this point if the *Level* parameter matches the IHV-specified UIF repro mode level in the INF file (0xFF in the following section's sample).

#### EVENT_CONTROL_CODE_CAPTURE_STATE

This flag requests that the provider logs its state information. This is generally called to flush the in-memory logs to disk. The IHV's implementation should flush and reset firmware logs at this point if the *Level* parameter matches the IHV-specified UIF repro mode level in the INF file (0xFF in the following section's sample).

### Sample code

The following is a sample ETW callback implementation that can be used as a template to enable verbose driver and firmware logging for UIF repro mode scenarios.

> [!NOTE]
> IHVs need to flush any pending firmware logs for both the **EVENT_CONTROL_CODE_CAPTURE_STATE** and **EVENT_CONTROL_CODE_DISABLE_PROVIDER** control codes.

After the **EVENT_CONTROL_CODE_CAPTURE_STATE** is invoked, the UIF diagnostics tool invokes the ETW callback two more times with the **EVENT_CONTROL_CODE_ENABLE_PROVIDER** control code. Therefore, to avoid re-enabling the firmware logging, the state machine moves from the *ReproModeStateCaptured* state to the *ReproModeStateFinal* state before moving back to the *ReproModeStateNotStarted* state. The **EVENT_CONTROL_CODE_DISABLE_PROVIDER** control code is only used to disable the provider. This is not part of the UIF process, but still needs to be honored.

IHVs should change the **IHV_ETW_REPRO_MODE_LEVEL** value in the following example to match the repro mode level set in the INF file.

```C++
#define IHV_ETW_REPRO_MODE_LEVEL 0xFF // This value must match the repro mode              
                                      // EnableLevel INF value

typedef enum _EtwReproModeState
{
    ReproModeStateNotStarted = 0,
    ReproModeStateStarted,
    ReproModeStateCaptured,
    ReproModeStateFinal
} EtwReproModeState;
 
static EtwReproModeState g_eReproModeLoggingEnabled = ReproModeStateNotStarted; 

VOID
EtwEventControlCallback(
    _In_ LPCGUID SourceId,
    _In_ ULONG ControlCode,
    _In_ UCHAR Level,
    _In_ ULONGLONG MatchAnyKeyword,
    _In_ ULONGLONG MatchAllKeyword,
    _In_opt_ PEVENT_FILTER_DESCRIPTOR FilterData,
    _Inout_opt_ PVOID CallbackContext
    )
{
    UNREFERENCED_PARAMETER(SourceId);
    UNREFERENCED_PARAMETER(MatchAnyKeyword);
    UNREFERENCED_PARAMETER(MatchAllKeyword);
    UNREFERENCED_PARAMETER(FilterData);
    UNREFERENCED_PARAMETER(CallbackContext);

    switch(ControlCode)
    {
        case EVENT_CONTROL_CODE_ENABLE_PROVIDER:
            if (Level == IHV_ETW_REPRO_MODE_LEVEL)
            {
                switch(g_eReproModeLoggingEnabled)
                {
                    case ReproModeStateNotStarted:
                        //
                        // Enable verbose Firmware logs.
                        //
                        g_eReproModeLoggingEnabled = ReproModeStateStarted;
                        break;

                    case ReproModeStateCaptured:
                        //
                        // The diagnostic tools will invoke the callback after
                        // the capture with EVENT_CONTROL_CODE_ENABLE_PROVIDER
                        // twice. 
                        //
                        g_eReproModeLoggingEnabled = ReproModeStateFinal;
                        break;

                    case ReproModeStateFinal:
                        //
                        // The state machine is now complete, reset the state.
                        //
                        g_eReproModeLoggingEnabled = ReproModeStateNotStarted;
                        break;

                    case ReproModeStateStarted:
                    default:
                        break;
                }
            }
            break;  

        case EVENT_CONTROL_CODE_DISABLE_PROVIDER:
            if (g_eReproModeLoggingEnabled == ReproModeStateStarted) 
            {
                // 
                // Merge verbose firmware logs into ETW log (if not done already).
                // Disable verbose firmware logs
                // 
                g_eReproModeLoggingEnabled = ReproModeStateNotStarted;
            }
            break;

        case EVENT_CONTROL_CODE_CAPTURE_STATE:
            if (Level == IHV_ETW_REPRO_MODE_LEVEL &&
                g_eReproModeLoggingEnabled == ReproModeStateStarted)
            {
                // 
                // Merge verbose firmware logs into ETW log (if not done already).
                // Disable verbose firmware logs
                // 
                g_eReproModeLoggingEnabled = ReproModeStateCaptured;
            }
            break;  
    }
}
```

## Testing the repro mode logs

To test the IHV repro mode logs, the following commands can be used to start and stop capture. 

> [!NOTE]
> The resulting ETL file will contain some OS logs.

- netsh wlan IHV startlogging
- netsh wlan IHV stoplogging

These commands are also used by customers to manually collect logs from a device.

## Submitting IHV providers to Microsoft

The final step for IHVs to submit repro mode user-initiated feedback is to contact Microsoft and supply the requested provider GUIDs, levels, and flags along with sample log data for review. Once the logging is approved, the providers will be added to the user-initiated feedback system. 

> [!NOTE]
> Any modifications to the provider GUIDs, levels, or flags after submission will have no effect on the UIF logs.

## Related links

[User-initiated feedback with IHV trace logging](user-initiated-feedback-with-ihv-trace-logging.md)

[User-initiated feedback - normal mode](user-initiated-feedback-normal-mode.md)
