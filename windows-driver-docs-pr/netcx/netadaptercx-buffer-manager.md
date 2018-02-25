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

# Network data buffer management

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NetAdapterCx enables the client drivers and the system to work together when allocating data buffer from the system memory for the network packets being received and transmitted. This can result in faster performance for the NIC's data path, easier memory lifetime managment for the client drivers, and gives more control to the system.

## The benefits of buffer management in NetAdapterCx

The choice of where the buffers are allocated from system memory for packet payloads is critical to the performance of the data path. In NetAdapterCx, the buffer management model is heavily optimized for DMA capable NIC hardware and the best way to take advantage of it is to let the system allocate the data buffers on the behalf of the client driver for both the transmit (Tx) path and the the receive (Rx) path. Meanwhile, the NIC client driver still can influence the system about where and how to allocate the data buffers so they can be easily consumed by their hardware. 

For a typical DMA capable NIC, there are serval benefits of this approach:
1. The data buffers are allocated and freed by the system, therefore the client driver is free of burden of memory lifetime management.
2. The system makes sure that the allocated data buffers are DMA-ready for the NIC hardware according to the capabilities declared by the client driver. Therefore, the client driver can simply programs the data buffer into their hardware as is, without perform any additional DMA mapping operation.
3. The system can take the needs of upper layer applications into consideration when allocating the data buffers, so that the system can use heuristics to optimize the end-to-end performance.

For non-DMA capabile NIC, such like USB based network dangle, or other advanced/software NICs, the system still have an option to leave the data buffer management completely to the client driver. 

## How to leverage the buffer management

The buffer management feature is supported starting in NetAdapterCx 1.2, which ships with Windows 10, version 1803. To opt in, follow these steps:

1. In your *[EvtNetAdapterSetCapabilities](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_set_capabilities)* callback, tells the system about your hardware's data buffer capabilities and constraints using the [NET_ADAPTER_RX_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_rx_capabilities) and [NET_ADAPTER_TX_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_tx_capabilities) data structure for Rx and Tx path respectively. 
2. Initialize the two capabilities structures by calling one of the initialization functions. For instance, a  DMA-capable NIC would use **NET_ADAPTER_TX_CAPABILITIES_INIT_FOR_DMA** and **NET_ADAPTER_RX_CAPABILITIES_INIT_SYSTEM_MANAGED** to declare its DMA capablities and to instruct the system to fully manage the data buffer on behalf of the client driver.
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
                                                        MAX_PACKET_SIZE + FRAME_CRC_SIZE + RSVD_BUF_SIZE,
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