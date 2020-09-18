---
title: Receive Segment Coalescing Offload
description: Receive Segment Coalescing Offload usage, rules, and example
ms.assetid:
keywords:
- WDF Network Adapter Class Extension Offloads, NetAdapterCx hardware offloads, NetAdapterCx Offloads, NetAdapter Offloads, Receive Segment Coalescing offload, RSC
ms.date: 01/18/2019
ms.custom: 19H1
---

# Receive Segment Coalescing

Almost all the layers in the TCP/IP stack must look at a segment's header information separately.
This creates a large amount of overhead when large amounts of data are being received.
Receive segment coalescing (RSC) reduces this overhead by coalescing a sequence of received segments and indicate them up the TCP/IP stack in one single coalesced segment,
so that upper layers in the TCP/IP stack need only look at one header for the entire sequence.
Network interface card (NIC) that supports RSC in hardware can not only greatly improve the receiving path performance, but also reduce the host CPU utilization as it frees protocol layer from doing RSC in software.

Refer [Overview of Receive Segment Coalescing](https://docs.microsoft.com/en-us/windows-hardware/drivers/network/overview-of-receive-segment-coalescing) for more details on RSC.

## INF keywords for controlling RSC offload

The client driver doesn't need to worry about checking standard registry keywords.
NetAdapterCx checks the registry keywords and honors them when enabling the active offload capabilities.

The RSC keywords specified in [Standardized INF Keywords for RSC](https://docs.microsoft.com/en-us/windows-hardware/drivers/network/standardized-inf-keywords-for-rsc) can be used to enable/disable the RSC offload with a registry key setting.


## Configuring hardware offloads

Similar to the case of GSO and checksum offloads, client drivers first advertise their hardware's RSC capabilities during initialization.
This might occur within the context of [*EvtDevicePrepareHardware*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) when starting a net adapter.
To get started, the client driver allocates a capabilities structure for the RSC offload, initialize it, and calls the [**NetAdapterOffloadSetRscCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netadapteroffloadsetrsccapabilities) method to register it with NetAdapterCx.
During the call to [**NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES_INIT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-net_adapter_offload_rsc_capabilities_init), the driver provides a pointer to a callback function that the system invokes later if active RSC capabilities change.

### Rules for indicating hardware RSC capabilities
1. NetAdapterOffloadLayer3FlagIPv4NoOptions and NetAdapterOffloadLayer3FlagIPv6NoExtensions are the only valid values for NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES's Layer3Flags field. They are used to indicate IPv4 and IPv6 support respectively.
2. NetAdapterOffloadLayer4FlagTcpNoOptions is the only valid value for NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES's Layer4Flags field.
3. Layer 3 flags must be set if NetAdapterOffloadLayer4FlagTcpNoOptions flag is set.
4. *TcpTimestampOption* is optional. Client driver sets this field after calling **NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES_INIT** and before calling **NetAdapterOffloadSetRscCapabilities**, based on whether NIC supports TCP timestamp option or not.
5. Client driver must **NOT** perform **software** RSC on a type of traffics if its NIC doesn't have hardware support for that type of traffic.

This example shows how a client driver might set up its RSC hardware offload capabilities.

```C++
VOID
MyAdapterSetRscOffloadCapabilities(
    NETADAPTER NetAdapter
)
{
    // Configure the hardware's RSC offload capabilities
    NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES rscOffloadCapabilities;
    NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES_INIT(
        &rscOffloadCapabilities,
        NetAdapterOffloadLayer3FlagIPv4NoOptions | NetAdapterOffloadLayer3FlagIPv6NoExtensions,
        NetAdapterOffloadLayer4FlagTcpNoOptions,
        MyEvtAdapterOffloadSetRsc);
    rscOffloadCapabilities.TcpTimestampOption = FALSE;

    // Set the current RSC offload capabilities and register the callback for future changes in active capabilities
    NetAdapterOffloadSetRscCapabilities(NetAdapter, &rscOffloadCapabilities);
}
```

## Updating hardware offloads

Similar to checksum and GSO offloads, if the TCP/IP stack requests a change in active RSC capabilities of the network adapter, NetAdapterCx invokes the client driver's *EVT_NET_ADAPTER_OFFLOAD_SET_RSC* callback function that was previously registered in **NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES**.
In this callback, the system supplies updated capabilities in the NETOFFLOAD object, through which the client driver can query to update its offload capabilities.

The following examples shows how a client driver might update its RSC offload capabilities:
```C++
VOID
MyEvtAdapterOffloadSetRsc(
    NETADAPTER NetAdapter,
    NETOFFLOAD Offload
)
{
    PMY_NET_ADAPTER_CONTEXT adapterContext = NetvAdapterGetContext(NetAdapter);

    // Store the updated information in the context
    adapterContext->IsRscIPv4Enabled = NetOffloadIsTcpRscIPv4Enabled(Offload);
    adapterContext->IsRscIPv6Enabled = NetOffloadIsTcpRscIPv6Enabled(Offload);
    adapterContext->IsRscTcpTimestampOptionEnabled = NetOffloadIsRscTcpTimestampOptionEnabled(Offload);
}
```

## Related links

[**NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/ns-netadapteroffload-_net_adapter_offload_rsc_capabilities)

[**NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES_INIT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-net_adapter_offload_rsc_capabilities_init)

[**NetAdapterOffloadSetRscCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netadapteroffloadsetrsccapabilities)

[**NetOffloadIsTcpRscIPv4Enabled**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netoffloadistcprscipv4enabled)

[**NetOffloadIsTcpRscIPv6Enabled**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netoffloadistcprscipv6enabled)

[**NetOffloadIsRscTcpTimestampOptionEnabled**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netoffloadisrsctcptimestampoptionenabled)
