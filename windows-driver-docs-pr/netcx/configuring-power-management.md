---
title: Configuring power management
description: Configuring power management
ms.assetid: 0EAE26D0-C191-422F-8A73-28A71C272D4D
keywords:
- NetAdapterCx configuring power management, NetCx configuring power management
ms.date: 06/05/2017
ms.localizationpriority: medium
---

# Configuring power management

This topic describes how to configure power management capabilities in a NetAdapterCx client driver.

Because the client driver is a WDF driver, much of the implementation is the same as any other WDF driver, and then there are a few options specific to NetAdapterCx that you can add in.

For details on the common WDF behaviors, see the following pages:

*  The client registers optional WDF event callbacks to receive notification of power transitions, as described in [Supporting PnP and Power Management in Function Drivers](../wdf/supporting-pnp-and-power-management-in-function-drivers.md).
*  For info on registering PnP and power callback functions in a WDF client, see [Creating Device Objects in a Function Driver](../wdf/creating-device-objects-in-a-function-driver.md).
*  For details on how your device can wake the system from a system-wide low-power state, see [Supporting System Wake-Up](../wdf/supporting-system-wake-up.md).

## Setting power capabilities of the network adapter

After configuring the standard WDF power management functionality, the next step is to call [**NetAdapterSetPowerCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadaptersetpowercapabilities) to set the power capabilities of the network adapter.

The following example shows how to initialize and configure a NETPOWERSETTINGS object, which the client typically does when starting a net adapter, but before calling [**NetAdapterStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterstart):

```C++
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

The client can register [*EVT_NET_ADAPTER_PREVIEW_PROTOCOL_OFFLOAD*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nc-netadapter-evt_net_adapter_preview_protocol_offload) and [*EVT_NET_ADAPTER_PREVIEW_WAKE_PATTERN*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nc-netadapter-evt_net_adapter_preview_wake_pattern) callback functions to accept or reject incoming protocol offloads and wake patterns. If you would like to register either of these optional callbacks, you must do so while starting a net adapter, before calling [**NetAdapterStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterstart).

## Programming Protocol Offload and Wake Patterns

In its [*EvtDeviceArmWakeFromS0*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0) and [*EvtDeviceArmWakeFromSx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx) callback functions, the driver iterates through the enabled wake patterns and protocol offloads and programs them into the hardware.

First retrieve a handle to the NETPOWERSETTINGS object that is associated with the adapter by calling [**NetAdapterGetPowerSettings**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadaptergetpowersettings) from [*EvtDeviceArmWakeFromS0*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0) or a related callback function.  The following example shows how to iterate through the wake patterns:

```C++
NTSTATUS
EvtDeviceArmWakeFromS0(
    WDFDEVICE     Device
)
{

    NETADAPTER adapter = GetDeviceContext(Device)->Adapter;
    NETPOWERSETTINGS powerSettings = NetAdapterGetPowerSettings(adapter);

    ULONG wakeUpFlags = NetPowerSettingsGetEnabledWakeUpFlags(powerSettings);
     
    if (wakeUpFlags & NET_ADAPTER_WAKE_ON_MEDIA_DISCONNNECT)
    {
        // ...
    }

    // Iterate through stored wake patterns and query which ones
    // are enabled and should be programmed to hardware

    for (ULONG i = 0; i < NetPowerSettingsGetWakePatternCount(powerSettings); i++)
    {
        PNDIS_PM_WOL_PATTERN wakePattern = NetPowerSettingsGetWakePattern(powerSettings, i);

        if (NetPowerSettingsIsWakePatternEnabled(powerSettings, wakePattern))
        {
            // ...
        }

    }

    return STATUS_SUCCESS;
}
```

The client uses the same mechanism to iterate through protocol offloads, using [**NetPowerSettingsGetProtocolOffloadCount**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netpowersettings/nf-netpowersettings-netpowersettingsgetprotocoloffloadcount), [**NetPowerSettingsGetProtocolOffload**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netpowersettings/nf-netpowersettings-netpowersettingsgetprotocoloffload) and [**NetPowerSettingsIsProtocolOffloadEnabled**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netpowersettings/nf-netpowersettings-netpowersettingsisprotocoloffloadenabled).
