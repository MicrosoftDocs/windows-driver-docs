---
title: NetAdapterCx hardware offloads
description: NetAdapterCx offloads
ms.assetid: 85A819E2-6352-4DE9-9689-3DCEB9B0AAD8
keywords:
- WDF Network Adapter Class Extension Offloads, NetAdapterCx hardware offloads, NetAdapterCx Offloads, NetAdapter Offloads
ms.date: 01/18/2019
ms.custom: 19H1
---

# NetAdapterCx hardware offloads

To increase its performance, the Windows TCP/IP stack can offload some tasks to a network interface card (NIC) that has the appropriate task offload capabilities.

## Overview of offloads in NetAdapterCx

NetAdapterCx focuses on ease of offload configuration and management of offload capabilities. Client drivers only need to specify a simple configuration for their hardware offload capabilities and register callbacks to be notified of changes in capabilities. 

This guidance provides an overview of key concepts for hardware offloads in NetAdapterCx.

- Hardware offload capabilities are advertised by the network adapter hardware during initialization and must be advertised before calling [**NetAdapterStart**](https://docs.microsoft.com/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterstart).
- The driver doesn't need to worry about checking standard registry keywords. NetAdapterCx checks the registry keywords and honors them when enabling the active offload capabilities.
- The *active* offload capabilities of the network adapter are those that the network adapter is currently programmed to perform. These are a subset of the hardware capabilities advertised by the client driver previously.
- The TCP/IP stack or an overlying protocol driver can request a change in active capabilities of the network adapter. Client drivers register callbacks with NetAdapterCx to be notified of changes in the active offload capabilities.
- If a packet extension is needed for an offload, it is automatically registered when the network adapter advertises support for the hardware offload.

Client drivers advertise a granular set of capabilities to NetAdapterCx. For example, this can be whether IPv4 Options, IPv6 Extensions or TCP Options are supported, etc. The client driver can also specify if it has a hardware packet header offset limit. For example, if a client driver has only 8 bits in the descriptor for the layer 4 header offset, it would set the Layer4HeaderOffset to 255. Any packets that have a header offset greater than the specified limit will be offloaded in software by NetAdapterCx. 

If the hardware is not capable of handling a specific combination, it should not declare support for that capability.

The following offloads are supported by NetAdapterCx and the Windows TCP/IP stack:

| Offload name | Description |
| --- | --- |
| [Checksum](checksum-offload.md) | Offloading the calculation and validation of IP and TCP checksums to the NIC. |
| [Generic send offload (GSO)](gso-offload.md) | Offloading segmentation of large TCP/UDP packets for IPv4 and IPv6. |

## Configuring hardware offloads

Client drivers first advertise their hardware's offload capabilities during net adapter initialization. This might occur within the context of [*EvtDevicePrepareHardware*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) when starting a net adapter. To get started, the client driver allocates a capabilities structure for each supported offload, initializes them, and calls the appropriate **NetAdapterOffloadSetXxxCapabilities** methods to register them with NetAdapterCx. During the call to **NET_ADAPTER_OFFLOAD_XxX_CAPABILITIES_INIT**, the driver provides a pointer to a callback function that the system invokes later if active hardware offload capabilities change.

For examples, visit the corresponding offload reference page.

## Updating hardware offloads

If the TCP/IP stack or an overlying protocol driver requests a change in active capabilities of the network adapter, NetAdapterCx invokes the client driver's *EVT_NET_ADAPTER_OFFLOAD_SET_XxX* callback function that was previously registered during adapter initialization. In this function, the system supplies updated capabilities in the NETOFFLOAD object, which the client driver can query and use to update its offload capabilities.

For examples, visit the corresponding offload reference page.
