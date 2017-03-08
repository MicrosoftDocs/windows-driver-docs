---
title: Configuring Power Management Hardware Capabilities
---

# Configuring Power Management Hardware Capabilities

first you can preview protocol offload and wake patterns as they come in.

## Power Management

then, client driver queries the necessary wake-on-LAN (WoL) configuration from the NETPOWERSETTINGS object.

 To access this object, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md) from [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) and related callback functions.  For example:

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
