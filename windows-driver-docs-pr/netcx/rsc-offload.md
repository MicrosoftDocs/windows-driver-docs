---
title: Receive Segment Coalescing offload
description: Receive Segment Coalescing (RSC) offload usage, rules, and examples in NetAdapterCx.
keywords:
- WDF Network Adapter Class Extension Offloads, NetAdapterCx hardware offloads, NetAdapterCx Offloads, NetAdapter Offloads, Receive Segment Coalescing offload, RSC
ms.date: 10/13/2020
ms.custom: Fe
---

# Receive Segment Coalescing (RSC) offload

> [!WARNING]
> Some information in this topic relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.
>
> NetAdapterCx is preview only in Windows 10, version 2004.
>
> Currently, NetAdapterCx client drivers cannot be certified.

When receiving data, most layers in the TCP/IP stack must look at each segment's header information separately. This creates a large amount of overhead when large amounts of data are being received.

[Receive segment coalescing (RSC)](../network/overview-of-receive-segment-coalescing.md) reduces this overhead by coalescing a sequence of received segments and indicating them up the TCP/IP stack in one single coalesced segment. The upper layers in the TCP/IP stack only need to look at one header for the entire sequence.
A network interface card (NIC) that supports RSC in hardware can greatly improve the receive path performance. It can also reduce the host CPU utilization as it frees the protocol layer from doing RSC in software.

For more details on RSC, see [Overview of Receive Segment Coalescing](../network/overview-of-receive-segment-coalescing.md).

## INF keywords for controlling RSC offload

NetAdapterCx checks the registry keywords and honors them when enabling the active offload capabilities. The driver doesn't need to take any further action.

The RSC keywords specified in [Standardized INF Keywords for RSC](../network/standardized-inf-keywords-for-rsc.md) can be used to enable/disable the RSC offload with a registry key setting.

The keyword values must be of type [REG_SZ](/windows/win32/sysinfo/registry-value-types).

## Configuring RSC offload

Client drivers first advertise their hardware's RSC capabilities during net adapter initialization. This might occur within their [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback before starting a net adapter.

To configure RSC capabilities, the client driver:

1. Allocates a [**NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES**](/windows-hardware/drivers/ddi/netadapteroffload/ns-netadapteroffload-_net_adapter_offload_rsc_capabilities) structure.

1. Calls [**NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES_INIT**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-net_adapter_offload_rsc_capabilities_init) to initialize the structure.

1. Calls [**NetAdapterOffloadSetRscCapabilities**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netadapteroffloadsetrsccapabilities) to register the structure with NetAdapterCx.
 
During the call to **NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES_INIT** the client driver provides a pointer to the [*EVT_NET_ADAPTER_OFFLOAD_SET_RSC*](/windows-hardware/drivers/ddi/netadapteroffload/nc-netadapteroffload-evt_net_adapter_offload_set_rsc) callback. The system invokes this callback later if active offload capabilities change.

### Rules for indicating hardware RSC capabilities

1. Client drivers must **NOT** perform **software** RSC on any type of traffic that doesn't have hardware support in the NIC.

The following rules apply to the [**NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES**](/windows-hardware/drivers/ddi/netadapteroffload/ns-netadapteroffload-_net_adapter_offload_rsc_capabilities) structure:

2. `NetAdapterOffloadLayer3FlagIPv4NoOptions` and `NetAdapterOffloadLayer3FlagIPv6NoExtensions` are the only valid values for the **Layer3Flags** field. These flags indicate IPv4 and IPv6 support respectively.

3. `NetAdapterOffloadLayer4FlagTcpNoOptions` is the only valid value for the **Layer4Flags** field.

4. Layer 3 flags must be set if the `NetAdapterOffloadLayer4FlagTcpNoOptions` flag is set.

5. The **TcpTimestampOption** field is optional. Client drivers set this field after calling **NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES_INIT** and before calling **NetAdapterOffloadSetRscCapabilities** to indicate whether the NIC supports the TCP timestamp option.

The following example shows how a client driver might set up its RSC hardware offload capabilities.

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

## Updating RSC hardware offloads

If the TCP/IP stack or an overlying protocol driver requests a change to the net adapter's active RSC capabilities, NetAdapterCx invokes the client driver's [*EVT_NET_ADAPTER_OFFLOAD_SET_RSC*](/windows-hardware/drivers/ddi/netadapteroffload/nc-netadapteroffload-evt_net_adapter_offload_set_rsc) callback that was registered in **NET_ADAPTER_OFFLOAD_RSC_CAPABILITIES**. In this callback, the system supplies updated capabilities in the NETOFFLOAD object which the client driver can query to update its offload capabilities.

Client drivers can call the following functions to determine which RSC offloads are enabled:

* [**NetOffloadIsTcpRscIPv4Enabled**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netoffloadistcprscipv4enabled)
* [**NetOffloadIsTcpRscIPv6Enabled**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netoffloadistcprscipv6enabled)
* [**NetOffloadIsRscTcpTimestampOptionEnabled**](/windows-hardware/drivers/ddi/netadapteroffload/nf-netadapteroffload-netoffloadisrsctcptimestampoptionenabled)


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
