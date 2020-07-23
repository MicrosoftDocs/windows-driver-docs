---
title: Generic Segmentation Offload
description: Generic Segmentation Offload usage, rules, and example
ms.assetid:
keywords:
- WDF Network Adapter Class Extension Offloads, NetAdapterCx hardware offloads, NetAdapterCx Offloads, NetAdapter Offloads, Generic segmentation offload, GSO, Large Segmentation Offload, LSO, UDP Segmentation Offload, USO
ms.date: 01/18/2019
ms.custom: 19H1
---

# Generic Segmentation Offload

Generic Segmentation Offload (GSO) is a term that collectively represents Large Send Offload (LSO) and UDP Send Offload (USO).  Client drivers that can offload the segmentation of large TCP/UDP packets that are larger than the maximum transmission unit (MTU) of the network medium must indicate their capability to NetAdapterCx using the GSO APIs.

Refer [Offloading the Segmentation of Large TCP Packets](https://docs.microsoft.com/windows-hardware/drivers/network/offloading-the-segmentation-of-large-tcp-packets) for more details on LSO.

Refer [UDP Segmentation Offload (USO)](https://docs.microsoft.com/windows-hardware/drivers/network/udp-segmentation-offload-uso-) for more details on USO.

## INF keywords for controlling checksum offload

The driver doesn't need to worry about checking standard registry keywords. NetAdapterCx checks the registry keywords and honors them when enabling the active offload capabilities.

The LSO keywords specified in [Using Registry Values to Enable and Disable Task Offloading](https://docs.microsoft.com/windows-hardware/drivers/network/using-registry-values-to-enable-and-disable-task-offloading) can be used to enable/disable the LSO offload with a registry key setting.

The USO keywords specified in [UDP Segmentation Offload (USO)](https://docs.microsoft.com/windows-hardware/drivers/network/udp-segmentation-offload-uso-) can be used to enable/disable the USO offload with a registry key setting.

## Configuring hardware offloads

Client drivers first advertise their hardware's GSO capabilities during net adapter initialization. This might occur within the context of [*EvtDevicePrepareHardware*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) when starting a net adapter. To get started, the client driver allocates a capabilities structure for the GSO offload, initialize it, and calls the [**NetAdapterOffloadSetGsoCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netadapteroffloadsetgsocapabilities) method to register it with NetAdapterCx. During the call to [**NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES_INIT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-net_adapter_offload_gso_capabilities_init), the driver provides a pointer to a callback function that the system invokes later if active GSO capabilities change.

### Rules for indicating hardware GSO capabilities
1. If Large Send Offload (LSO) is supported by the NIC, the driver must populate the TcpFlags field of the NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES with the types of packets it can perform LSO on.
2. If UDP Send Offload (USO) is supported by the NIC, the driver must populate the UdpFlags field of the NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES with the types of packets it can perform USO on.
3. MaximumOffloadSize and MinimumSegmentCount are mandatory fields.
2. The layer 4 header offset limit is optional. If the OS sends a packet with a header offset larger than the specified limit, it will not ask for GSO to be performed. 
2. IP/TCP packets without options/extensions must be supported if options/extensions are supported.
3. Layer 3 flags must be set if layer 4 flags are set.

This example shows how a client driver might set up its hardware offload capabilities.

```C++
VOID
MyAdapterSetOffloadCapabilities(
    NETADAPTER NetAdapter
)
{
    // Configure the hardware's GSO offload capabilities
    NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES gsoOffloadCapabilities;

    auto const tcpFlags = NetAdapterOffloadFlagIPv4WithoutOptions |
        NetAdapterOffloadFlagIPv4WithOptions |
        NetAdapterOffloadFlagIPv6WithoutExtensions |
        NetAdapterOffloadFlagIPv6WithExtensions |
        NetAdapterOffloadFlagTcpWithoutOptions |
        NetAdapterOffloadFlagTcpWithOptions;

    auto const udpFlags = NetAdapterOffloadFlagIPv4WithoutOptions |
        NetAdapterOffloadFlagIPv4WithOptions |
        NetAdapterOffloadFlagIPv6WithoutExtensions |
        NetAdapterOffloadFlagIPv6WithExtensions |
        NetAdapterOffloadFlagUdp;

    NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES_INIT(
        &gsoOffloadCapabilities,
        tcpFlags,
        MY_GSO_OFFLOAD_MAX_SIZE,
        MY_GSO_OFFLOAD_MIN_SEGMENT_COUNT,
        EvtAdapterOffloadSetGso);

    gsoOffloadCapabilities.UdpFlags = udpFlags;
    gsoOffloadCapabilities.Layer4OffsetLimit = 127;

    // Set the current GSO offload capabilities and register the callback for future changes in active capabilities
    NetAdapterOffloadSetGsoCapabilities(NetAdapter, &gsoOffloadCapabilities);
}
```

## Updating hardware offloads

If the TCP/IP stack or an overlying protocol driver requests a change in active capabilities of the network adapter, NetAdapterCx invokes the client driver's *EVT_NET_ADAPTER_OFFLOAD_SET_XxX* callback function that was previously registered during adapter initialization. In this function, the system supplies updated capabilities in the NETOFFLOAD object, which the client driver can query and use to update its offload capabilities.

The following example example shows how a client driver might update its GSO offload capabilities:

```C++
VOID
MyEvtAdapterOffloadSetGso(
	NETADAPTER NetAdapter,
	NETOFFLOAD Offload
)
{
	PMY_NET_ADAPTER_CONTEXT adapterContext = MyGetNetAdapterContext(NetAdapter);

	// Store the updated information in the context
	adapterContext->LSOv4 = NetOffloadIsLsoIPv4Enabled(Offload) ? 
		GsoOffloadEnabled : GsoOffloadDisabled;
	adapterContext->LSOv6 = NetOffloadIsLsoIPv6Enabled(Offload) ?
		GsoOffloadEnabled : GsoOffloadDisabled;
	adapterContext->USOv4 = NetOffloadIsUsoIPv4Enabled(Offload) ? 
		GsoOffloadEnabled : GsoOffloadDisabled;
	adapterContext->USOv6 = NetOffloadIsUsoIPv6Enabled(Offload) ?
		GsoOffloadEnabled : GsoOffloadDisabled;

	// Enable hardware checksum if LSO/USO is enabled
	MyUpdateHardwareChecksum(adapterContext);
}
```

## Related links

[**NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/ns-netadapteroffload-_net_adapter_offload_gso_capabilities)

[**NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES_INIT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-net_adapter_offload_gso_capabilities_init)

[**NetAdapterOffloadSetGsoCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netadapteroffloadsetgsocapabilities)

[*EvtNetAdapterOffloadSetGso*](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nc-netadapteroffload-evt_net_adapter_offload_set_gso)
