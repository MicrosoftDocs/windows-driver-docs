---
title: Generic Segmentation Offload
description: Generic Segmentation Offload usage, rules, and examples in NetAdapterCx
keywords:
- WDF Network Adapter Class Extension Offloads, NetAdapterCx hardware offloads, NetAdapterCx Offloads, NetAdapter Offloads, Generic segmentation offload, GSO, Large Segmentation Offload, LSO, UDP Segmentation Offload, USO
ms.date: 10/08/2020
ms.custom: Fe
---

# Generic Segmentation Offload

> [!WARNING]
> Some information in this topic relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.
>
> NetAdapterCx is preview only in Windows 10, version 2004.
>
> Currently, NetAdapterCx client drivers cannot be certified.

Generic Segmentation Offload (GSO) collectively represents [Large Send Offload (LSO)](../network/offloading-the-segmentation-of-large-tcp-packets.md) and [UDP Send Offload (USO)](../network/udp-segmentation-offload-uso-.md). 

Client drivers can offload the segmentation of TCP/UDP packets that are larger than the maximum transmission unit (MTU) of the network medium. Drivers must indicate this capability to NetAdapterCx using the GSO APIs.

## INF keywords for controlling GSO

NetAdapterCx checks the registry keywords and honors them when enabling the active offload capabilities. The driver doesn't need to take any further action.

The LSO keywords specified in [Using Registry Values to Enable and Disable Task Offloading](../network/using-registry-values-to-enable-and-disable-task-offloading.md) can be used to enable/disable the LSO offload with a registry key setting.

The USO keywords specified in [UDP Segmentation Offload (USO)](../network/udp-segmentation-offload-uso-.md) can be used to enable/disable the USO offload with a registry key setting.

The keyword values must be of type [REG_SZ](/windows/win32/sysinfo/registry-value-types).

## Configuring GSO

Client drivers first advertise their hardware's GSO capabilities during net adapter initialization. This might occur within their [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback before starting a net adapter.

To configure GSO, the client driver:

1. Allocates a [**NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES**](/windows-hardware/drivers/ddi/netadapteroffload/ns-netadapteroffload-_net_adapter_offload_gso_capabilities) structure.

1. Calls [**NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES_INIT**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-net_adapter_offload_gso_capabilities_init) to initialize the structure.

1. Calls [**NetAdapterOffloadSetGsoCapabilities**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netadapteroffloadsetgsocapabilities) to register the structure with NetAdapterCx.

During the call to **NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES_INIT** the client driver provides a pointer to the [*EVT_NET_ADAPTER_OFFLOAD_SET_GSO*](/windows-hardware/drivers/ddi/netadapteroffload/nc-netadapteroffload-evt_net_adapter_offload_set_gso) callback. The system invokes this callback later if active offload capabilities change.

### Rules for indicating hardware GSO capabilities

The following rules apply to the [**NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES**](/windows-hardware/drivers/ddi/netadapteroffload/ns-netadapteroffload-_net_adapter_offload_gso_capabilities) structure:

1. The driver must set the **Layer3Flags** and **Layer4Flags**.

1. If the NIC supports LSO, the driver must populate the **Layer4Flags** field with the `NetAdapterOffloadLayer4FlagTcpWithoutOptions` TCP flag.

1. If the NIC supports USO, the driver must populate the **Layer4Flags** field with the `NetAdapterOffloadLayer4FlagUdp` UDP flag.

1. **MaximumOffloadSize** and **MinimumSegmentCount** are mandatory fields.

1. The **Layer4OffsetLimit** field is optional. If the OS sends a packet with a header offset larger than the specified limit, it won't ask for GSO to be performed.

1. IP/TCP packets without options/extensions must be supported if options/extensions are supported.

This example shows how a client driver might set up its hardware offload capabilities.

```C++
VOID
MyAdapterSetOffloadCapabilities(
    NETADAPTER NetAdapter
)
{
    // Configure the hardware's GSO offload capabilities
    NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES gsoOffloadCapabilities;

    auto const layer3Flags = NetAdapterOffloadLayer3FlagIPv4NoOptions |
        NetAdapterOffloadLayer3FlagIPv4WithOptions |
        NetAdapterOffloadLayer3FlagIPv6NoExtensions |
        NetAdapterOffloadLayer3FlagIPv6WithExtensions;

    auto const layer4Flags = NetAdapterOffloadLayer4FlagTcpNoOptions |
        NetAdapterOffloadLayer4FlagTcpWithOptions;
        NetAdapterOffloadLayer4FlagUdp;

    NET_ADAPTER_OFFLOAD_GSO_CAPABILITIES_INIT(
        &gsoOffloadCapabilities,
        layer3Flags,
        layer4Flags,
        MY_GSO_OFFLOAD_MAX_SIZE,
        MY_GSO_OFFLOAD_MIN_SEGMENT_COUNT,
        EvtAdapterOffloadSetGso);

    gsoOffloadCapabilities.Layer4OffsetLimit = 127;

    // Set the current GSO offload capabilities and register the callback for future changes in active capabilities
    NetAdapterOffloadSetGsoCapabilities(NetAdapter, &gsoOffloadCapabilities);
}
```

## Updating hardware offloads

If the TCP/IP stack or an overlying protocol driver requests a change to the net adapter's active capabilities, NetAdapterCx invokes the client driver's [*EVT_NET_ADAPTER_OFFLOAD_SET_GSO*](/windows-hardware/drivers/ddi/netadapteroffload/nc-netadapteroffload-evt_net_adapter_offload_set_gso) callback that was registered during adapter initialization. In this function, the system supplies updated capabilities in the NETOFFLOAD object which the client driver queries to update its offload capabilities.

Client drivers can call the following functions to determine which offloads are enabled:

* [**NetOffloadIsLsoIPv4Enabled**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netoffloadislsoipv4enabled)
* [**NetOffloadIsLsoIPv6Enabled**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netoffloadislsoipv6enabled)
* [**NetOffloadIsUsoIPv4Enabled**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netoffloadisusoipv4enabled)
* [**NetOffloadIsUsoIPv6Enabled**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netoffloadisusoipv6enabled)

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