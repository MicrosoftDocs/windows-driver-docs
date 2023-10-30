---
title: Configuring NetAdapterCx power management
description: Configuring power management
keywords:
- NetAdapterCx configuring power management, NetCx configuring power management
ms.date: 06/12/2020
---

# Configuring NetAdapterCx power management

All NetAdapterCx client drivers are Windows Driver Framework (WDF) drivers with power management functionality similar to all WDF drivers. NetAdapterCx drivers require additional networking-specific power configurations as detailed in this article.

A typical networking device supports three common power management features:

- The networking device can enter a lower-power (Dx) state when instructed by the OS.
  - The client driver registers optional WDF event callbacks to receive notification of power transitions, as described in [Supporting PnP and Power Management in Function Drivers](../wdf/supporting-pnp-and-power-management-in-function-drivers.md).

  - If the network device can enter its Dx state while the system remains in its working (S0) state then the client driver should support idle power-down. See [Supporting Idle Power-Down](../wdf/supporting-idle-power-down.md). Besides the standard [User Control of Device Idle and Wake Behavior](../wdf/user-control-of-device-idle-and-wake-behavior.md) available to all WDF devices, NetAdapterCx allows additional network specific idle control through **\*IdleRestriction** as defined in [Standardized INF Keywords for Power Management](../network/standardized-inf-keywords-for-power-management.md).

- When the networking device is in the Dx state, it can trigger a wake-up signal if a pre-configured wake condition has occurred.
  - For details on how a WDF device can wake the system from a system-wide low-power state see [Supporting System Wake-Up](../wdf/supporting-system-wake-up.md).

  - NetAdapterCx provides APIs for the client driver to declare which network events its hardware has wake support for. See [Setting power capabilities of the network adapter](#setting-power-capabilities-of-the-network-adapter).

- When the networking device is in the Dx state, it can still respond to some commonly used network requests to maintain the host system's presence on the network without waking up the host system. See [Setting power capabilities of the network adapter](#setting-power-capabilities-of-the-network-adapter).

## Setting power capabilities of the network adapter

After configuring WDF power management functionality, the next step is to set the power capabilities of the network adapter. Power capabilities are divided into two categories: [Low power protocol offload capabilities](#low-power-protocol-offload-capabilities) and [Wake up capabilities](#wake-up-capabilities).

### Low power protocol offload capabilities

For background information on how the Windows network stack makes use of this capability, see [Protocol Offloads for NDIS Power Management](../network/protocol-offloads-for-ndis-power-management.md).

Client drivers set their low power protocol offload capabilities by calling the following methods appropriate for their hardware:

- [**NetAdapterPowerOffloadSetArpCapabilities**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterpoweroffloadsetarpcapabilities)
- [**NetAdapterPowerOffloadSetNSCapabilities**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterpoweroffloadsetnscapabilities)

### Wake up capabilities

Client drivers call any of the following methods to set the wake capabilities that their hardware supports when the device is in low power state (Dx):

- [**NetAdapterWakeSetBitmapCapabilities**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetbitmapcapabilities)
- [**NetAdapterWakeSetMagicPacketCapabilities**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetmagicpacketcapabilities)
- [**NetAdapterWakeSetMediaChangeCapabilities**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetmediachangecapabilities)
- [**NetAdapterWakeSetPacketFilterCapabilities**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterwakesetpacketfiltercapabilities)

### Power consumption and resume latency

When the networking device is in Dx, it still consumes power to perform offload and arm for wake. After the device initiates wake-up from Dx, there's a delay before the device can transfer packets again. The deeper the internal power state the device goes into the less power it consumes while in Dx, but the longer the resume latency.

The following table describes the general guidelines regarding the trade-off between power consumption and resume latency for each wake capability.

> [!IMPORTANT]
> Some information relates to prereleased product which may be substantially modified before commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided. For more information about a specific device type, refer to media-specific documentation and the [Windows Hardware Compatibility Program (WHCP)](/windows-hardware/design/compatibility/).
  
| Wake Capability | Wake Events | Power Consumption | Resume Latency
|-|-|-|-|
| PacketFilter | Any packet matches configured ReceivePacketFilter | Should be lower than when in D0, and the device needs to be kept in an appropriate state so that the resume latency is very small  | <= 10 ms |
| Bitmap |Any packet matches configured bitmap pattern | Should be lower than when armed for PacketFilter because it has more latitude in resume latency | <= 300 ms |
| MagicPacket | Magic packet | Similar to Bitmap | <= 300 ms |
| MediaChange | Media connected or disconnected | Similar to Bitmap | <= 300 ms |

The following example illustrates how a client driver might initialize its power capabilities. It does this while starting the net adapter but before calling [**NetAdapterStart**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterstart). In this example, the client driver sets its bitmap, media change, and packet filter wake capabilities.

```cpp
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
// Set media change wake capabilities
//
NET_ADAPTER_WAKE_MEDIA_CHANGE_CAPABILITIES mediaChangeCapabilities;
NET_ADAPTER_WAKE_MEDIA_CHANGE_CAPABILITIES_INIT(&mediaChangeCapabilities);

mediaChangeCapabilities.MediaConnect = TRUE;
mediaChangeCapabilities.MediaDisconnect = TRUE;

NetAdapterWakeSetMediaChangeCapabilities(Adapter, &mediaChangeCapabilities);

//
// Set packet filter wake capabilities
//
if(deviceContext->SelectiveSuspendSupported)
{
    NET_ADAPTER_WAKE_PACKET_FILTER_CAPABILITIES packetFilterCapabilities;
    NET_ADAPTER_WAKE_PACKET_FILTER_CAPABILITIES_INIT(&packetFilterCapabilities);

    packetFilterCapabilities.PacketFilterMatch = TRUE;

    NetAdapterWakeSetPacketFilterCapabilities(Adapter, &packetFilterCapabilities);
}
```

The client can optionally register [*EVT_NET_DEVICE_PREVIEW_POWER_OFFLOAD*](/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_preview_power_offload) and [*EVT_NET_DEVICE_PREVIEW_WAKE_SOURCE*](/windows-hardware/drivers/ddi/netdevice/nc-netdevice-evt_net_device_preview_wake_source) callback functions to accept or reject incoming protocol offloads and wake patterns.

## Programming protocol power offload and wake patterns

During the device's [powering down sequence](../wdf/power-down-and-removal-sequence-for-a-function-or-filter-driver.md), the driver iterates through the enabled wake patterns and protocol power offloads and programs them into the hardware. The driver does this in its [*EvtDeviceArmWakeFromS0*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0) and [*EvtDeviceArmWakeFromSx*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx) callback functions.

The following example shows how a client driver might iterate over the wake pattern list to check for a wake on magic packet entry, then iterate over the power offload list to process IPv4 ARP protocol offload:

```cpp
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

On the way [back to high power](../wdf/power-up-sequence-for-a-function-or-filter-driver.md) the driver normally disables the previously programmed protocol power offloads and wake patterns in the corresponding [*EvtDeviceDisarmWakeFromSx*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_sx) and [*EvtDeviceDisarmWakeFromS0*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_s0) callbacks.

## Reporting wake reason

> [!IMPORTANT]
> It is mandatory that client drivers report wake reason to NetAdapterCx.

When the NIC hardware wakes up the system, the client driver must report to NetAdapterCx which wake source triggered the wake. For most wake sources, drivers use the [**NET_ADAPTER_WAKE_REASON_PACKET**](/windows-hardware/drivers/ddi/netadapter/ns-netadapter-_net_adapter_wake_reason_packet) structure to describe the network packet that triggered the wake.

If the [**NET_WAKE_SOURCE_TYPE**](/windows-hardware/drivers/ddi/netwakesource/ne-netwakesource-_net_wake_source_type) is:

- **NetWakeSourceTypeBitmapPattern**, call [**NET_ADAPTER_WAKE_REASON_PACKET_INIT**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-net_adapter_wake_reason_packet_init) to initialize the **NET_ADAPTER_WAKE_REASON_PACKET** structure. Call [**NetAdapterReportWakeReasonPacket**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterreportwakereasonpacket) to report this wake reason.

- **NetWakeSourceTypeMagicPacket**, call [**NET_ADAPTER_WAKE_REASON_MAGIC_PACKET_INIT**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-net_adapter_wake_reason_magic_packet_init)  to initialize the **NET_ADAPTER_WAKE_REASON_PACKET** structure. Call **NetAdapterReportWakeReasonPacket** to report this wake reason.

- **NetWakeSourceTypePacketFilterMatch**, call [**NET_ADAPTER_WAKE_REASON_FILTER_PACKET_INIT**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-net_adapter_wake_reason_filter_packet_init)  to initialize the **NET_ADAPTER_WAKE_REASON_PACKET** structure. Call **NetAdapterReportWakeReasonPacket** to report this wake reason.

- **NetWakeSourceTypeMediaChange**, call [**NetAdapterReportWakeReasonMediaChange**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterreportwakereasonmediachange) to report this wake reason.

## Power management scenarios for Modern Standby system

> [!IMPORTANT]
> For Modern Standby platform, the networking device driver must:
>
> - Call [**WdfDeviceInitSetPnpPowerEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks) to register power callbacks.
> - Call [**WdfDeviceAssignS0IdleSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings) to support device idling when the system is in its working (S0) state.
> - Call [**WdfDeviceInitSetPowerPolicyEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks) to register wake-up callbacks.
> - Support [Low power protocol offload capabilities](#low-power-protocol-offload-capabilities) that are appropriate for the device type.
> - Support [Wake-up capabilities](#wake-up-capabilities) that are appropriate for the device type.
>
> Please refer to media-specific documentation and WHCP for the complete Modern Standby requirements for your device type.

The OS is responsible for networking device's power policy decisions. For example, the OS controls when a device must go to Dx and what types of network events the device should wake on. The device driver's responsibility is to reliably execute the power transition sequence when requested by the OS, and then correctly program their hardware for the wake condition set by the OS.

The OS makes power policy decisions based on a broad set of factors, including system-wide power policies and user choices. The following are some common power policies used for networking devices on a Modern Standby system:

> [!IMPORTANT]
> These power policies may change with OS updates and the following information is provided as an example. Dependencies on specific end-to-end behavior of the OS should be avoided.

- When the PC screen is on and the networking device has been idling, the OS asks the device to go to Dx and arms it for PacketFilter and MediaChange wake.

- When the PC enters Modern Standby and the networking device has been idling, the OS asks the NIC go to Dx and arms it for Bitmap, MediaChange and Magic Packet wake.

- When the PC goes to Hibernation, the OS asks the NIC to go to Dx and arms it for Magic Packet wake.

**Note**: NetAdapterCx client drivers control the visibility of the power management tab. For more information, see [User Control of Device Idle and Wake Behavior](../wdf/user-control-of-device-idle-and-wake-behavior.md).
