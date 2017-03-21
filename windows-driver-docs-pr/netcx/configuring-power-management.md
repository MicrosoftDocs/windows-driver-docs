---
title: Configuring Power Management
---

# Configuring Power Management

This topic describes how to configure power management capabilities in a NetAdapterCx client driver.

Because the client driver is a WDF driver, much of the implementation is the same as any other WDF driver, and then there are a few options specific to NetAdapterCx that you can add in.

For details on the common WDF behaviors, see the following pages:

*  The client registers optional WDF event callbacks to receive notification of power transitions, as described in [Supporting PnP and Power Management in Function Drivers](../wdf/supporting-pnp-and-power-management-in-function-drivers.md).
*  For info on registering PnP and power callback functions in a WDF client, see [Creating Device Objects in a Function Driver](../wdf/creating-device-objects-in-a-function-driver.md).
*  For details on how your device can wake the system from a system-wide low-power state, see [Supporting System Wake-Up](../wdf/supporting-system-wake-up.md).

## NetAdapterCx specific options

After configuring the standard WDF power management functionality, the next step is to call [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md) to set the power capabilities of the network adapter.

The following example shows how to initialize and configure a NETPOWERSETTINGS object, which the client typically does in its [*EVT_NET_ADAPTER_SET_CAPABILITIES*](evt-net-adapter-set-capabilities.md) callback:

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

The client can register [*EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD*](evt-net-adapter-preview-protocol-offload.md) and [*EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN*](evt-net-adapter-preview-wake-pattern.md) callback functions to accept or reject incoming protocol offloads and wake patterns.

## Programming Protocol Offload and Wake Patterns

In its [*EvtDeviceArmWakeFromS0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) and [*EvtDeviceArmWakeFromSx*](https://msdn.microsoft.com/library/windows/hardware/ff540844) callback functions, the driver iterates through the enabled wake patterns and protocol offloads and programs them into the hardware.

First retrieve a handle to the NETPOWERSETTINGS object that is associated with the adapter by calling [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md) from [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) or a related callback function.  The following example shows how to iterate through the wake patterns:

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
The client uses the same mechanism to iterate through protocol offloads.
