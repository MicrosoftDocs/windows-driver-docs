---
title: NetAdapterCx hardware offloads
description: NetAdapterCx offloads
ms.assetid: 85A819E2-6352-4DE9-9689-3DCEB9B0AAD8
keywords:
- WDF Network Adapter Class Extension Offloads, NetAdapterCx hardware offloads, NetAdapterCx Offloads, NetAdapter Offloads
ms.author: windowsdriverdev
ms.date: 07/31/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetAdapterCx hardware offloads

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

To increase its performance, the Windows TCP/IP stack can offload some tasks to a network interface card (NIC) that has the appropriate task offload capabilities.

## Overview of offloads in NetAdapterCx

NetAdapterCx focuses on ease of offload configuration and management of offload capabilities. Client drivers only need to specify a simple configuration for their hardware offload capabilities and register callbacks to be notified of changes in capabilities. 

This guidance provides an overview of key concepts for hardware offloads in NetAdapterCx.

- Hardware offload capabilities are advertised by the network adapter hardware during initialization and must be advertised before calling [**NetAdapterStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterstart).
- The driver doesn't need to worry about checking standard registry keywords. NetAdapterCx checks the registry keywords and honors them when enabling the active offload capabilities.
- The *active* offload capabilities of the network adapter are those that the network adapter is currently programmed to perform. These are a subset of the hardware capabilities advertised by the client driver previously.
- The TCP/IP stack or an overlying protocol driver can request a change in active capabilities of the network adapter. Client drivers register callbacks with NetAdapterCx to be notified of changes in the active offload capabilities.
- If a packet extension is needed for an offload, it is automatically registered when the network adapter advertises support for the hardware offload.

Client drivers advertise a minimum set of capabilities to NetAdapterCx. These do not include granular capability details for all offload combinations supported by the client driver. For example, this can be whether IPOptions, IPExtensions or TCPOptions are supported, etc. This means that the client driver is responsible for performing the offload on all combinations of an advertised capability. For example, support for IPv4 implies support for IPOptions, support for IPv6 implies support for IPExtensions, and support for TCP implies support for TCPOptions. 

If the hardware is not capable of handling a specific combination, it should either not declare support for that capability or perform a software fallback when it encounters such a packet.

The following offloads are supported by NetAdapterCx and the Windows TCP/IP stack:

| Offload name | Description |
| --- | --- |
| Checksum | Offloading the calculation and validation of IP and TCP checksums to the NIC. |
| Large send offload (LSO) | Offloading segmentation of large TCP packets for IPv4 and IPv6. |

## Example

Client drivers first advertise their hardware's checksum offload capabilities during net adapter initialization. This might occur within the context of [*EvtDevicePrepareHardware*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) when starting a net adapter. To get started, the client driver allocates a capabilities structure for each supported offload, initializes them, and calls the appropriate **NetAdapterOffloadSetXxxCapabilities** methods to register them with NetAdapterCx. During the call to **NetAdapterOffloadSetXxxCapabilities**, the driver provides a pointer to a callback function that the system invokes later if active hardware offload capabilities change.

This example shows how a client driver might set up its hardware offload capabilities.

```C++
VOID
MyAdapterSetOffloadCapabilities(
    NETADAPTER NetAdapter
)
{
    // Configure the hardware's checksum offload capabilities
    NET_ADAPTER_OFFLOAD_CHECKSUM_CAPABILITIES checksumOffloadCapabilities;
    NET_ADAPTER_OFFLOAD_CHECKSUM_CAPABILITIES_INIT(&checksumOffloadCapabilities,
                                                   TRUE,    // IPv4
                                                   TRUE,    // TCP
                                                   TRUE);   // UDP

    // Set the current checksum offload capabilities and register the callback for future changes in active capabilities
    NetAdapterOffloadSetChecksumCapabilities(NetAdapter,
                                             &checksumOffloadCapabilities,
                                             MyEvtAdapterOffloadSetChecksum);

    // Configure the hardware's LSO offload capabilities
    NET_ADAPTER_OFFLOAD_LSO_CAPABILITIES lsoOffloadCapabilities;
    NET_ADAPTER_OFFLOAD_LSO_CAPABILITIES_INIT(&lsoOffloadCapabilities,
                                              TRUE,         // IPv4
                                              TRUE,         // IPv6
                                              MY_LSO_OFFLOAD_SIZE_MAX,
                                              MY_LSO_OFFLOAD_MIN_SEGMENT_COUNT);

    // Set the current LSO offload capabilities and register the callback for future changes in active capabilities
    NetAdapterOffloadSetLsoCapabilities(NetAdapter,
                                        &lsoOffloadCapabilities,
                                        MyEvtAdapterOffloadSetLso);   
}
```

## Related links

[Packet descriptors and extensions](packet-descriptors-and-extensions.md)