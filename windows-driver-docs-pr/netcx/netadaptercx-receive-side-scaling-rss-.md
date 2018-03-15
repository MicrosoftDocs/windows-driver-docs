---
title: NetAdapterCx receive side scaling (RSS)
description: NetAdapterCx receive side scaling (RSS)
ms.assetid: 85A819E2-6352-4DE9-9689-3DCEB9B0AAD8
keywords:
- WDF Network Adapter Class Extension Receive Side Scaling, NetAdapterCx receive side scaling, NetAdapterCx RSS, NetAdapter RSS
ms.author: windowsdriverdev
ms.date: 03/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetAdapterCx receive side scaling (RSS)

Receive side scaling (RSS) is a network driver technology that enables the efficient distribution of network receive processing across multiple CPUs in multiprocessor systems. RSS improves system performance and increases network scalability by harnessing all available processors in a system and dynamically rebalancing CPU workloads. 

This topic highlights RSS for NetAdapterCx client drivers and assumes knowledge of RSS underpinnings and terminology. For more information about RSS in general, including diagrams illustrating RSS in different hardware scenarios, see [Receive Side Scaling](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-receive-side-scaling2).

## Overview of RSS in NetAdapterCx

RSS in NetAdapterCx focuses on ease of configuration, simplicity of enablement and disablement, and abstraction of processor-to-interrupt complexity. A client driver for an RSS-capable NIC only needs to meet three criteria to support RSS in NetAdapterCx:

1. The driver must set RSS capabilities in the *[EvtNetAdapterSetCapabilities](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_set_capabilities)* event callback. This includes implementing four RSS callbacks and registering them in the RSS capabilities structure.
2. The driver's datapath queues must be created and ready to accept requests.
3. The driver must be in the *D0* power state.

Because of these conditions, the design of RSS in NetAdapterCx guarantees that the system will not call a client's RSS callbacks and enable RSS until the very end of the power-up sequence shown on [Power-up sequence for a NetAdapterCx client driver](power-up-sequence-for-a-netadaptercx-client-driver.md). Clients do not have to manage indirection table move requests or handle other RSS events until everything they need is ready. 

## Setting RSS capabilities

Follow these steps to get started with RSS in NetAdapterCx:

1. In your *[EvtNetAdapterSetCapabilities](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_set_capabilities)* callback, tell the system about your hardware's RSS capabilities and constraints using the [NET_ADAPTER_RECEIVE_SCALING_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netreceivescaling/ns-netreceivescaling-_net_adapter_receive_scaling_capabilities) structure.
2. Initialize the capabilities structure by calling [NET_ADAPTER_RECEVIE_SCALING_CAPABILITIES_INIT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netreceivescaling/nf-netreceivescaling-net_adapter_receive_scaling_capabilities_init). 
3. When you initialize the RSS capabilities structure, set the structure's RSS callback members to register your implementations for these callbacks:
    1. *[EvtNetAdapterReceiveScalingEnable](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netreceivescaling/nc-netreceivescaling-evt_net_adapter_receive_scaling_enable)*
    2. *[EvtNetAdapterReceiveScalingDisable](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netreceivescaling/nc-netreceivescaling-evt_net_adapter_receive_scaling_disable)*
    3. *[EvtNetAdapterReceiveScalingSetHashSecretKey](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netreceivescaling/nc-netreceivescaling-evt_net_adapter_receive_scaling_set_hash_secret_key)*
    4. *[EvtNetAdapterReceiveScalingSetIndirectionEntries](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netreceivescaling/nc-netreceivescaling-evt_net_adapter_receive_scaling_set_indirection_entries)*
