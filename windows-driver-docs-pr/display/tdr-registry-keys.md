---
title: Testing and debugging TDR during driver development
description: TDR testing and debugging information for developers
keywords:
- TDR debugging, driver development
- Timeout detection and recovery debugging, driver development
- TDR testing, driver development
- Timeout detection and recovery testing, driver development
- Registry keys, TDR, driver development
- Registry keys, timeout detection and recovery, driver development
- WDK display development
- TDR tests, WHLK
- TDR tests, Windows Hardware Lab Kit
ms.date: 03/30/2021
ms.localizationpriority: medium
ms.custom: contperf-fy21q3
---

# Testing and debugging TDR during driver development

This topic provides TDR testing and debugging strategies for display driver developers.

## TDR tests in WHLK

The [Windows Hardware Lab Kit](/windows-hardware/test/hlk/) (WHLK) contains TDR-specific tests that driver developers can use for testing and debugging purposes. For example, developers can manually trigger a GPU TDR using the [**SimulatePreemption TDR**](/windows-hardware/test/hlk/testref/86be5032-cfcd-4ee5-a515-0e3ebc0cb6f4). See [**Device.Graphics**](/windows-hardware/test/hlk/testref/device-graphics) for more information about the various TDR-related tests.

## TDR registry keys for testing and debugging

Developers can use the following TDR (timeout detection and recovery)-related registry keys for testing or debugging purposes only during the driver development process.

> [!IMPORTANT]
> These registry keys should not be manipulated by end users, or by applications outside of targeted testing or debugging during driver development.

### TdrLevel

Specifies the initial level of recovery.

```registry
KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
KeyValue  : TdrLevel
ValueType : REG_DWORD
ValueData : TdrLevelXxx (see the following table)
```

Where TdrLevel*Xxx* can be one of the following values:

| Value | Meaning |
| ----- | ------- |
| TdrLevelOff (0) | Detection disabled |
| TdrLevelBugcheck (1) | Bug check on detected timeout; for example, no recovery. |
| TdrLevelRecoverVGA (2) | Recover to VGA (not implemented). |
| TdrLevelRecover (3) | Recover on timeout. This is the default value. |

### TdrDelay

Specifies the number of seconds that the GPU can delay the preempt request from the GPU scheduler. This is effectively the timeout threshold.

```registry
KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
KeyValue  : TdrDelay
ValueType : REG_DWORD
ValueData : Number of seconds to delay. The default value is 2 seconds.
```

### TdrDdiDelay

Specifies the number of seconds that the OS allows threads to leave the driver. After a specified time, the OS bug-checks the computer with the code VIDEO_TDR_FAILURE (0x116).

```registry
KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
KeyValue  : TdrDdiDelay
ValueType : REG_DWORD
ValueData : Number of seconds to leave the driver. The default value is 5 seconds.
```

### TdrDebugMode

Specifies the debugging-related behavior of the TDR process. The default value is TDR_DEBUG_MODE_RECOVER_NO_PROMPT, which indicates not to break into the debugger.

```registry
KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
KeyValue  : TdrDebugMode
ValueType : REG_DWORD
ValueData : TDR_DEBUG_MODE_XXX (see the following table)
```

| Value | Meaning |
| ----- | ------- |
| TDR_DEBUG_MODE_OFF (0) | Break to kernel debugger before the recovery to allow investigation of the timeout. |
| TDR_DEBUG_MODE_IGNORE_TIMEOUT (1) | Ignore any timeout. |
| TDR_DEBUG_MODE_RECOVER_NO_PROMPT (2) | Recover without breaking into the debugger. This is the default value. |
| TDR_DEBUG_MODE_RECOVER_UNCONDITIONAL (3) | Recover even if some recovery conditions are not met (for example, recover on consecutive timeouts). |

### TdrLimitTime

Specifies the default time within which a specific number of TDRs (specified by the **TdrLimitCount** key) are allowed without crashing the computer.

```registry
KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
KeyValue  : TdrLimitTime
ValueType : REG_DWORD
ValueData : Number of seconds before crashing. The default value is 60 seconds.
```

### TdrLimitCount

Specifies the default number of TDRs (0x117) that are allowed during the time specified by the **TdrLimitTime** key without crashing the computer.

```registry
KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
KeyValue  : TdrLimitCount
ValueType : REG_DWORD
ValueData : Number of TDRs before crashing. The default value is 5.
```

### TdrTestMode

Reserved. Do not use.

```registry
KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
KeyValue  : TdrTestMode
ValueType : REG_DWORD
ValueData : Do not use.
```
