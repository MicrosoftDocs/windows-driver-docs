---
title: Configuring Power Management
---

# Configuring Power Management

This topic describes how to preview and query power management capabilities in a NetAdapterCx client driver.

Typically, a client driver calls [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md) to set the power capabilities of the network adapter.

The client then uses standard WDF event callbacks to receive notification of power transitions.  For more info, see [Supporting PnP and Power Management in Function Drivers](../wdf/supporting-pnp-and-power-management-in-function-drivers.md).

The following example shows how to initialize and configure a NETPOWERSETTINGS object.  The client typically does this in its [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md) callback:

```cpp
NET_ADAPTER_POWER_CAPABILITIES     powerCaps;
NET_ADAPTER_POWER_CAPABILITIES_INIT(&powerCaps);

powerCaps.Flags = NET_ADAPTER_POWER_WAKE_PACKET_INDICATION;

powerCaps.SupportedMediaSpecificWakeUpEvents = NET_ADAPTER_WLAN_WAKE_ON_AP_ASSOCIATION_LOST;
powerCaps.SupportedProtocolOffloads = NET_ADAPTER_PROTOCOL_OFFLOAD_ARP | NET_ADAPTER_PROTOCOL_OFFLOAD_NS;
powerCaps.SupportedWakePatterns = NET_ADAPTER_WAKE_BITMAP_PATTERN;
powerCaps.SupportedWakeUpEvents = NET_ADAPTER_WAKE_ON_MEDIA_CONNECT | NET_ADAPTER_WAKE_ON_MEDIA_DISCONNECT;

powerCaps.EvtAdapterPreviewWakePattern = EvtAdapterPreviewWakePattern;
powerCaps.EvtAdapterPreviewProtocolOffload = EvtAdapterPreviewProtocolOffload;

NetAdapterSetPowerCapabilities(NetAdapter, &powerCaps);
```

## Previewing Protocol Offload and Wake Patterns

The client can register [*EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD*](evt-net-adapter-preview-protocol-offload.md) and [*EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN*](evt-net-adapter-preview-wake-pattern.md) callback functions to accept or reject incoming protocol offloads and wake patterns.

In its [*EvtDeviceArmWakeFromS0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) and [*EvtDeviceArmWakeFromSx*](https://msdn.microsoft.com/library/windows/hardware/ff540844) callback functions, the driver can iterate through the enabled wake patterns and protocol offloads to program them into the hardware.

### Wake patterns

To access the configuration from the NETPOWERSETTINGS object, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md) from [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) or a related callback function.  For example:

```cpp
NTSTATUS
EvtDeviceArmWakeFromS0(
    WDFDEVICE     Device
)
{

    NETPOWERSETTINGS NetWakeSettings;
    ULONG EnabledWolPacketPatterns;

    NetWakeSettings = NetAdapterGetPowerSettings(deviceContext->AdapterContext->Adapter);
    EnabledWolPacketPatterns = NetPowerSettingsGetEnabledWakePatterns(NetWakeSettings);
    PNDIS_PM_WOL_PATTERN CurrentPattern = nullptr;
    ULONG NumberOfPatterns = NetPowerSettingsGetWakePatternCount(NetWakeSettings);

    for (UINT PatternIndex = 0; PatternIndex < NumberOfPatterns ; PatternIndex++)
    {
        CurrentPattern = NetPowerSettingsGetWakePattern(NetWakeSettings, PatternIndex);

    }

    return STATUS_SUCCESS;
}
```

For more info, see:

|Method|Summary|
|---|---|
| [**NetPowerSettingsGetEnabledWakePatterns**](netpowersettingsgetenabledwakepatterns.md) | Retrieves flags representing the types of wake patterns that a network adapter supports. |
| [**NetPowerSettingsGetEnabledWakeUpFlags**](netpowersettingsgetenabledwakeupflags.md) | Retrieves the media-independent wake-up events that a network adapter supports. |
<!--TODO: add other NetPowerSettings* to table, usage examples-->

Use these methods to access protocol offloads:

* [**NetPowerSettingsGetEnabledProtocolOffloads**](netpowersettingsgetenabledprotocoloffloads.md)
* [**NetPowerSettingsGetProtocolOffload**](netpowersettingsgetprotocoloffload.md)
* [**NetPowerSettingsGetProtocolOffloadCount**](netpowersettingsgetprotocoloffloadcount.md)
* [**NetPowerSettingsGetProtocolOffloadCountForType**](netpowersettingsgetprotocoloffloadcountfortype.md)
* [**NetPowerSettingsIsProtocolOffloadEnabled**](netpowersettingsisprotocoloffloadenabled.md)

Because the client is the [power policy owner](../wdf/power-policy-ownership.md) for the NIC's device stack, it can use WDF's built-in power management functionality.  For example, you might want to add your own idle logic. For info, see [Supporting System Wake-Up](../wdf/supporting-system-wake-up.md).

