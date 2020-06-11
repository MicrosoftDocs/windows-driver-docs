---
title: Configuring power management
description: Configuring power management
ms.assetid: 0EAE26D0-C191-422F-8A73-28A71C272D4D
keywords:
- NetAdapterCx configuring power management, NetCx configuring power management
ms.date: 11/06/2019
ms.localizationpriority: medium
---

# Configuring power management

This topic describes how to configure power management capabilities in a NetAdapterCx client driver. 

Any NetAdapterCx client driver is also a WDF driver, so much of its power management implementation is the same as any other WDF driver. However, there are some additional networking specific power configurations that your driver needs to support. 

A typical networking device supports 3 common power management features:

1. The networking device can enter a lower-power (Dx) state when instructed by the OS.

    * The client driver registers optional WDF event callbacks to receive notification of power transitions, as described in [Supporting PnP and Power Management in Function Drivers](../wdf/supporting-pnp-and-power-management-in-function-drivers.md).

    * If the network device can enter its Dx state while the system remains in its working (S0) state, then the client driver should support idle power-down. See [Supporting Idle Power-Down](../wdf/supporting-idle-power-down.md).

2. When the networking device is in the Dx state, it can trigger a wake-up signal if a pre-configured wake condition has occurred.

    * For details on how a WDF device can wake the system from a system-wide low-power state, see [Supporting System Wake-Up](../wdf/supporting-system-wake-up.md).

    * NetAdapterCx provides APIs for the client driver to declare which network events its hardware has wake support for. See the [Setting power capabilities of the network adapter](##setting-power-capabilities-of-the-network-adapter) section below.

3. When the networking device is in the Dx state, it can still respond to some commonly used network requests to maintain the host system's presence on the network, without waking up the host system. See the [Setting power capabilities of the network adapter](##setting-power-capabilities-of-the-network-adapter) section below.

## Setting power capabilities of the network adapter

After configuring the standard WDF power management functionality, the next step is to set the power capabilities of the network adapter. Power capabilities are divided into two categories: low power protocol offload capabilities and wake-up capabilities.

### Low power protocol offload capabilities

For background information on how the Windows network stack makes use of this capability, see [Protocol Offloads for NDIS Power Management](../network/protocol-offloads-for-ndis-power-management.md).

Client drivers set their low power protocol offload capabilities by calling the following methods appropriate for their hardware:

- [**NetAdapterPowerOffloadSetArpCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterpoweroffloadsetarpcapabilities)
- [**NetAdapterPowerOffloadSetNSCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterpoweroffloadsetnscapabilities)

### Wake-up capabilities

Client drivers call any of the following methods to set the wake capabilities that their hardware supports when the device is in low power state (Dx):

- [**NetAdapterWakeSetBitmapCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetbitmapcapabilities)
- [**NetAdapterWakeSetMagicPacketCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetmagicpacketcapabilities)
- [**NetAdapterWakeSetMediaChangeCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetmediachangecapabilities)
- [**NetAdapterWakeSetPacketFilterCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetpacketfiltercapabilities)

### Power consumption and resume latency

When the networking device is in Dx, it still needs to consume some power to perform offload and arm for wake. After the device starts to wake-up from Dx, there is a delay before the device can transfer packets again. The deeper the internal power state the device goes into, the less power it consumes while in Dx, but the longer the resume latency is. 

The table below describes the general guidelines regarding the trade-off between power consumption and resume latency for each wake capability. 

> [!WARNING]
> These guidelines are still under review and might change in the future. Please refer to media specific documentation and WHCP for more information about your device type.
  
| Wake Capability | Wake Events | Power Consumption | Resume Latency
|-|-|-|-|
| PacketFilter | Any packet matches configured ReceivePacketFilter | Should be lower than when in D0, and the device needs to be kept in an appropriate state so that the resume latency is very small  | <= 10 ms
| Bitmap |Any packet matches configured bitmap pattern | Should be lower than when armed for PacketFilter because it has more latitude in resume latency | <= 300 ms
| MagicPacket | Magic packet | Similar to Bitmap | <= 300 ms
| MediaChange | Media connected or disconnected | Similar to Bitmap | <= 300 ms

The following example shows how a client driver might initialize its power capabilities. It does this while starting the net adapter but before calling [**NetAdapterStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterstart). In this example, the client driver sets its bitmap, media change, and packet filter wake capabilities.

```C++
//
// Set bitmap wake capabilities
//
NET_ADAPTER_WAKE_BITMAP_CAPABILITIES bitmapCapabilities;
NET_ADAPTER_WAKE_BITMAP_CAPABILITIES_INIT(&bitmapCapabilities);

bitmapCapabilities.BitmapPattern = TRUE;
bitmapCapabilities.MaximumPatternCount = deviceContext->PowerFiltersSupported;
bitmapCapabilities.MaximumPatternSize = 256;

NetAdapterWakeSetBitmapCapabilities(Adapter, &bitmapCapabilities);

//
// Set media change wake capabilties
//
NET_ADAPTER_WAKE_MEDIA_CHANGE_CAPABILITIES mediaChangeCapabilities;
NET_ADAPTER_WAKE_MEDIA_CHANGE_CAPABILITIES_INIT(&mediaChangeCapabilities);

mediaChangeCapabilities.MediaConnect = TRUE;
mediaChangeCapabilities.MediaDisconnect = TRUE;

NetAdapterWakeSetMediaChangeCapabilities(Adapter, &mediaChangeCapabilities);

//
// Set packet filter wake capabilties 
//
if(deviceContext->SelectiveSuspendSupported)
{
    NET_ADAPTER_WAKE_PACKET_FILTER_CAPABILITIES packetFilterCapabilities;
    NET_ADAPTER_WAKE_PACKET_FILTER_CAPABILITIES_INIT(&packetFilterCapabilities);
    
    packetFilterCapabilities.PacketFilterMatch = TRUE;

    NetAdapterWakeSetPacketFilterCapabilities(Adapter, &packetFilterCapabilities);
}
```

The client can optionally register [*EVT_NET_DEVICE_PREVIEW_POWER_OFFLOAD*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_preview_power_offload) and [*EVT_NET_DEVICE_PREVIEW_WAKE_SOURCE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_preview_wake_source) callback functions to accept or reject incoming protocol offloads and wake patterns.

## Programming protocol power offload and wake patterns

During the device's [powering down sequence](../wdf/power-down-and-removal-sequence-for-a-function-or-filter-driver.md), the driver iterates through the enabled wake patterns and protocol power offloads and programs them into the hardware. The driver does this in its [*EvtDeviceArmWakeFromS0*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0) and [*EvtDeviceArmWakeFromSx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx) callback functions.

The following example shows how a client driver might iterate over the wake pattern list to check for a wake on magic packet entry, then iterate over the power offload list to process IPv4 ARP protocol offload:

```C++
NTSTATUS
EvtDeviceArmWakeFromSx(
    WDFDEVICE     Device
)
{
    NETADAPTER adapter = GetDeviceContext(Device)->Adapter;
    
    //
    // Process wake source list
    //
    NET_WAKE_SOURCE_LIST wakeSourceList;
    NET_WAKE_SOURCE_LIST_INIT(&wakeSourceList);

    NetDeviceGetWakeSourceList(Device, &wakeSourceList);

    for(UINT32 i = 0; i < NetWakeSourceListGetCount(&wakeSourceList; i++); i++)
    {
        NETWAKESOURCE wakeSource = NetWakeSourceListGetElement(&wakeSourceList, i);
        NET_WAKE_SOURCE_TYPE const wakeSourceType = NetWakeSourceGetType(wakeSource);

        if(wakeSourceType == NetWakeSourceTypeMagicPacket)
        {
            // Enable magic packet wake for the adapter
            ..
            //
        }
    }

    //
    // Process power offload list
    //
    NET_POWER_OFFLOAD_LIST powerOffloadList;
    NET_POWER_OFFLOAD_LIST_INIT(&powerOffloadList);

    NetDeviceGetPowerOffloadList(Device, &powerOffloadList);

    for(UINT32 i = 0; i < NetPowerOffloadListGetCount(&powerOffloadList); i++)
    {
        NETPOWEROFFLOAD powerOffload = NetPowerOffloadGetElement(&powerOffloadList, i);
        NET_POWER_OFFLOAD_TYPE const powerOffloadType = NetPowerOffloadGetType(powerOffload);

        if(powerOffloadType == NetPowerOffloadTypeArp)
        {
            // Enable ARP protocol offload for the adapter
            ..
            //
        }
    }

    return STATUS_SUCCESS;
}
```
On the way [back to high power](../wdf/power-up-sequence-for-a-function-or-filter-driver), the driver normally disables the previously programmed protocol power offloads and wake patterns in the corresponding [*EvtDeviceDisarmWakeFromSx*](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_sx) and [*EvtDeviceDisarmWakeFromS0*](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_s0) callbacks.

## Power management scenarios for Modern Standby system

> [!IMPORTANT]
> For Modern Standby platform, the networking device driver must: 
> *  Call [**WdfDeviceInitSetPnpPowerEventCallbacks**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks) to register power callbacks.
> * Call [**WdfDeviceAssignS0IdleSettings**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings) to support device idling when the system is in its working (S0) state.
> * Call [**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks) to register wake-up callbacks.
> * Support [Low power protocol offload capabilities](#Low-power-protocol-offload-capabilities) that are appropriate for the device type.
> * Support [Wake-up capabilities](#Wake-up-capabilities) that are appropriate for the device type.
>
> Please refer to media specific documentation and WHCP for the complete Modern Standby requirements for your device type.

The OS is responsible for networking devices' power policy decisions. For example, the OS controls when a device must go to Dx and what kinds of network events the device should wake on. The device driver's responsibility is to reliably execute the power transition sequence when requested by the OS, and then correctly program their hardware for the wake condition set by the OS.

The OS makes power policy decisions based on a broad set of factors, including system-wide power policies and user choices. The following are some common power policies used for networking devices on a Modern Standby system:

> [!WARNING] 
> These power policies might change between releases as the OS evolves. They are listed here just for illustration.

* When the PC screen is on and the networking device has been idling, the OS asks the device to go to Dx and arms it for PacketFilter and MediaChange wake.

* When the PC enters Modern Standby and the networking device has been idling, the OS asks the NIC go to Dx and arms it for Bitmap, MediaChange and Magic Packet wake.

* When the PC goes to Hibernation, the OS asks the NIC to go to Dx and arms it for Magic Packet wake.

