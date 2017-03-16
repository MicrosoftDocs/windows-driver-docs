---
title: Configuring Power Management
---

# Configuring Power Management

This topic describes how to preview and query power management capabilities in a NetAdapterCx client driver.

## Previewing Protocol Offload and Wake Patterns

The client can register [*EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD*](evt-net-adapter-preview-protocol-offload.md) and [*EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN*](evt-net-adapter-preview-wake-pattern.md) callback functions to accept or reject incoming protocol offloads and wake patterns.

## Querying Protocol Offload and Wake Patterns

In its [*EvtDeviceArmWakeFromS0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) and [*EvtDeviceArmWakeFromSx*](https://msdn.microsoft.com/library/windows/hardware/ff540844) callback functions, the driver can iterate through the enabled wake patterns and protocol offloads to program them into the hardware.
<!--TODO: add example-->

To access the configuration from the NETPOWERSETTINGS object, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md) from [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) or a related callback function.  For example:

```cpp
NTSTATUS
EvtDeviceArmWakeFromS0(WDFDEVICE Device)
{
    NETPOWERSETTINGS powerSettings = NetAdapterGetPowerSettings(Adapter->NetAdapter);

    ULONG EnabledWakePatterns = NetPowerSettingsGetEnabledWakePatterns(powerSettings);
    ULONG EnabledProtocolOffloads = NetPowerSettingsGetEnabledProtocolOffloads(powerSettings);
    ULONG WakeUpFlags = NetPowerSettingsGetEnabledWakeUpFlags(powerSettings);

    // ...
}
```

Because the client is the [power policy owner](../wdf/power-policy-ownership.md) for the NIC's device stack, it can use WDF's built-in power management functionality.  For example, you might want to add your own idle logic. For info, see [Supporting System Wake-Up](../wdf/supporting-system-wake-up.md).

See Also
-----
[**NetPowerSettingsGetEnabledWakePatterns**](netpowersettingsgetenabledwakepatterns.md)
[**NetPowerSettingsGetEnabledProtocolOffloads**](netpowersettingsgetenabledprotocoloffloads.md)
[**NetPowerSettingsGetEnabledWakeUpFlags**](netpowersettingsgetenabledwakeupflags.md)
