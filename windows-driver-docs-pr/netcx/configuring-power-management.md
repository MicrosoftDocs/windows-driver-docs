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

This topic describes how to configure power management capabilities in a NetAdapterCx client driver. Because any NetAdapterCx client driver is a WDF driver, much of the power management implementation is the same as any other WDF driver, and then there are some additional power configurations specific to networking that your driver can support. 

A typical networking device supports 3 common power managment features:

1. The networking device can enter a lower-power(Dx) state when instructed by the OS.

    * The client driver registers optional WDF event callbacks to receive notification of power transitions, as described in [Supporting PnP and Power Management in Function Drivers](../wdf/supporting-pnp-and-power-management-in-function-drivers.md).

    * If the network device can enter Dx state while the system remains in its working (S0) state, and then the client driver should be [Supporting Idle Power-Down](../wdf/supporting-idle-power-down.md).

2. When the networking device is in the lower-power(Dx) state, it can trigger a wake-up signal if certain pre-configured wake condition has happened.

    * For details on how a WDF device can wake the system from a system-wide low-power state, see [Supporting System Wake-Up](../wdf/supporting-system-wake-up.md).

    * NetAdapterCx provides APIs for the client driver to declare which network events that its hardware has wake support for, see [Setting power capabilities of the network adapter](##setting-power-capabilities-of-the-network-adapter) section below.

3. When the networking device is in the lower-power(Dx), it can still response to some commonly used network requests to maintain the host system's presence on the network, without waking up the host system. See [Setting power capabilities of the network adapter](##setting-power-capabilities-of-the-network-adapter) section below.

## Setting power capabilities of the network adapter

After configuring the standard WDF power management functionality, the next step is to set the power capabilities of the network adapter. Power capabilities are divided into two categories: low power protocol offload capabilities and wake-up capabilities.

### Low Power Protocol Offload Capabilities

For background information on how Windows network stack make use of this capabilty, see [Protocol Offloads for NDIS Power Management](../network/protocol-offloads-for-ndis-power-management.md).
Client drivers set their low power protocol offload capabilities by calling the following methods appropriate for their hardware:

- [**NetAdapterPowerOffloadSetArpCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterpoweroffloadsetarpcapabilities)
- [**NetAdapterPowerOffloadSetNSCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterpoweroffloadsetnscapabilities)

### Wake-Up Capabilities

Next, client drivers call any of the following methods to set the wake capabilities that their hardware supports when the device is in Dx:

- [**NetAdapterWakeSetBitmapCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetbitmapcapabilities)
- [**NetAdapterWakeSetMagicPacketCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetmagicpacketcapabilities)
- [**NetAdapterWakeSetMediaChangeCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetmediachangecapabilities)
- [**NetAdapterWakeSetPacketFilterCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetpacketfiltercapabilities)

It is known that the device might still need to draw power when it's armed for wake, so it can generate the wake-up signal. It's also expected that there would be some resume latency before the device can transfer or receive packets again after waking-up. The table below shows the allowed power consumption and resume latency for each wake capability.

| Wake Capability | Wake Events | Power Consumption | Resume Latency
|-|-|-|-|
| PacketFilter | Any packet matches configured ReceivePacketFilter | lower than when in D0, may be higher than Bitmap because shorter latency expected | <= 10 ms
| Bitmap | Any packet matches configured bitmap pattern | lower than when in D0, may be higher than MagicPacket | <= 300 ms
| MagicPacket | Magic packet | lower than when in D0, may be higher than MediaChange | <= 300 ms
| MediaChange | Media connected or disconnected | lower than when in D0, lowest possible | <= 300 ms

The following example shows how a client driver might initialize its power capabilities, which it does while starting the net adapter but before calling [**NetAdapterStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterstart). In this example, the client driver sets its bitmap, media change, and packet filter wake capabilities.

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

The client can register [*EVT_NET_DEVICE_PREVIEW_POWER_OFFLOAD*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_preview_power_offload) and [*EVT_NET_DEVICE_PREVIEW_WAKE_SOURCE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_preview_wake_source) callback functions to accept or reject incoming protocol offloads and wake patterns. If you would like to register either of these optional callbacks, you must do so while starting a net adapter, before calling [**NetAdapterStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterstart).

## Programming Protocol Offload and Wake Patterns

In its [*EvtDeviceArmWakeFromS0*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0) and [*EvtDeviceArmWakeFromSx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx) callback functions, the driver iterates through the enabled wake patterns and protocol offloads and programs them into the hardware.

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
## Power management scenarios for Modern Standby system

> [!IMPORTANT]
> For Modern Standby platform, the networking device driver must: 
> *  Call [**WdfDeviceSetPowerCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetpowercapabilities) to report a device's power management capabilities to the OS.
> * Call [**WdfDeviceAssignS0IdleSettings**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings) to support device idling when the system is in its working (S0) state.
> * Call [**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks) to enable wake-up callbacks
> * Support [Low Power Protocol Offload Capabilities]() that is appropriate for their physical medium:
> * Support PacketFilter and Bitmap wake-up capabilities, optionally MagicPacket and MediaChange if appropriate

For networking device, the OS is responsible for the power policy decision for the device, i.e. the OS controls when the device must go to Dx and what kind of network events the device should wake-up on. The device driver's responsiblity is to reliably execute the power transition flow when requested by the OS, and correctly program their hardware according to the condition set by the OS.

The OS makes the power policy decision based an array of factors, including system-wide power policies and user decisions. The following are some possible power policies that a networking device could encounter on a Modern Standby system:

> [!IMPORTANT] The power policies might change between releases as the OS evolves, and they are listed here just for illustration purpose.  

* When the PC screen is on and the networking device has been idling, the OS asks the device go to Dx and arms it for PacketFilter and MediaChange wake.

* When the PC enters Modern Standby and the networking device has been idling, the OS asks the NIC go to Dx and arms it for Bitmap, MediaChange and Magic Packet wake.

* When the PC goes to Hiberation, the OS asks the NIC to go to Dx and arms it for Magic Packet wake.

