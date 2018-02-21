---
title: NetAdapterCx Buffer Manager
description: NetAdapterCx Buffer Manager
ms.assetid: BFE1D376-88FB-41CB-AB6D-A0D6BB83128C
keywords:
- WDF Network Adapter Class Extension Buffer Manager, NetAdapterCx Buffer Manager
ms.author: windowsdriverdev
ms.date: 02/20/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetAdapterCx buffer manager

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

## Overview

Buffer manager is a new feature in NetAdapterCx 1.2 that enables Network Interface Card (NIC) drivers, protocol drivers, and NetAdapterCx to work together on memory buffer allocation for the receive and transmit data paths. This can result in faster performance for the NIC and gives more control over aspects like data buffer lifetime management, variable-size buffers, and more. Buffer manager for NetAdapterCx also provides more flexibility than the previous buffer manager model in the [Packet Direct Provider Interface (PDPI)](https://docs.microsoft.com/windows-hardware/drivers/network/introduction-to-ndis-pdpi) that NDIS 6.*X* miniport drivers could optionally use.

## Summary of performance benefits

The choice of where memory is allocated for packet payloads is critical to the performance of the data path. In the NDIS 6.*X* Net Buffer List (NBL) data path, the NIC cannot influence where the OS allocates memory for the transmit (Tx) path, while the OS likewise cannot influence where the NIC allocates memory for the receive (Rx) path. If a NIC supports the PD path, this issue is partially mitigated by the PD's own buffer manager feature that enables either the OS or the NIC to allocate the buffers. However, the PD buffer manager still doesn't permit the OS and the NIC to cooperate on that choice. In addition, PD has other limitations such as a fixed buffer size and inability to fully exploit a NIC's advanced memory management features on the Rx path.

The NetAdapterCx buffer manager improves on the PD buffer manager and existing infrastructure in the following ways:

1. It abstracts the preferences or requirements for memory allocation away from the NIC.
2. It is exposed to protocol drivers, which therefore enables all parties in the network stack (NetAdapterCx, the protocol driver, and the NIC driver) to agree on where to allocate payload memory for the best performance on a given NIC.
3. It can allocate memory needed for both Rx and Tx on behalf of the NIC, and it manages the lifetime of these allocations.
4. It supports a registration mode in which protocol drivers can specify the memory range for data buffers.
5. It gives advanced NICs the freedom to use the memory that the OS allocates for them in any way they'd like.

## How to use buffer manager

Buffer manager is supported starting in NetAdapterCx 1.2, which ships with Windows 10, version 1803. To opt in, follow these steps:

1. In your *[EvtDriverDeviceAdd](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add)* callback, register your *[EvtNetAdapterSetCapabilities](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_set_capabilities)* callback by setting the appropriate member of the [NET_ADAPTER_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_config.md) structure, then call [NetAdapterCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptercreate).
2. In your **EvtNetAdapterSetCapabilities** callback, allocate a [NET_ADAPTER_RX_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_rx_capabilities) structure and a [NET_ADAPTER_TX_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_tx_capabilities) structure. 
3. Initialize the two capabilities structures by calling one of the initialization methods for each. For more info about the different ways to initialize them, see the reference page for each structure.
4. Pass the initialized Tx and Rx capabilities structures to the [NetAdapterSetDatapathCapabilities](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptersetdatapathcapabilities) method in your *[EvtNetAdapterSetCapabilities](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_set_capabilities)* callback function.

## Example

The following example illustrates the basic steps outlined in the previous section for how to get started using the buffer manager in your NIC client driver. The example uses DMA for both Tx and Rx, so it previously created a WDFDMAENABLER object that it stored in its device context space. 

Note that the example also sets some hints about its fragment buffers after it initializes the Tx and Rx capabilities structures. These hints can be used by NetAdapterCx and protocol drivers to improve performance.

Error handling has been left out for clarity.

```c++
NTSTATUS
MyDeviceAdd(
    WDFDRIVER Driver,
    PWDFDEVICE_INIT DeviceInit
)
{
    NTSTATUS status;

    // Other device setup tasks
    ...

    // Set up the NETADAPTER object
    NET_ADAPTER_CONFIG  adapterConfig;
    NET_ADAPTER_CONFIG_INIT(&adapterConfig,
                            MyAdapterSetCapabilities,
                            MyAdapterCreateTxQueue,
                            MyAdapterCreateRxQueue
                            );

    WDF_OBJECT_ATTRIBUTES adapterAttributes;
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&adapterAttributes, MY_CONTEXT);

    NETADAPTER netAdapter;
    status = NetAdapterCreate(wdfDevice,
                              &adapterAttributes,
                              &adapterConfig,
                              &netAdapter
                              );

    // Other device setup tasks
    ...
}

NTSTATUS
MyAdapterSetCapabilities(
    NETADAPTER Adapter
)
{
    NTSTATUS status;

    // Get the device context
    PMY_DEVICE_CONTEXT deviceContext = GetMyContextFromDevice(Adapter);

    // Set various capabilities such as link layer MTU size, link layer capabilities, and power capabilities
    ...   

    // Initialize the Tx DMA capabilities structure
    NET_ADAPTER_DMA_CAPABILITIES txDmaCapabilities;
    NET_ADAPTER_DMA_CAPABILITIES_INIT(&txDmaCapabilities,
                                      deviceContext->dmaEnabler
                                      );

    // Set Tx capabilities
    NET_ADAPTER_TX_CAPABILITIES txCapabilities;
    NET_ADAPTER_TX_CAPABILITIES_INIT_FOR_DMA(&txCapabilities,
                                             &txDmaCapabilities,
                                             MAX_PACKET_SIZE,
                                             1
                                             );
    txCapabilities.FragmentRingNumberOfElementsHint = deviceContext->NumTransmitControlBlocks * MAX_PHYS_BUF_COUNT;

    // Initialize the Rx DMA capabilities structure
    NET_ADAPTER_DMA_CAPABILITIES rxDmaCapabilities;
    NET_ADAPTER_DMA_CAPABILITIES_INIT(&rxDmaCapabilities,
                                      deviceContext->dmaEnabler
                                      );

    // Set Rx capabilities
    NET_ADAPTER_RX_CAPABILITIES rxCapabilities;
    NET_ADAPTER_RX_CAPABILITIES_INIT_SYSTEM_MANAGED_DMA(&rxCapabilities,
                                                        &rxDmaCapabilities,
                                                        MAX_PACKET_SIZE + FRAME_CRC_SIZE + RSVD_BUF_SIZE
                                                        1
                                                        );
    rxCapabilities.FragmentBufferAlignment = 64;
    rxCapabilities.FragmentRingNumberOfElementsHint = deviceContext->NumReceiveBuffers;

    // Set the adapter's datapath capabilities
    NetAdapterSetDatapathCapabilities(Adapter, &txCapabilities, &rxCapabilities);

    // Set other needed capabilities
    ...
}
```