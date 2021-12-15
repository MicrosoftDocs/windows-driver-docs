---
title: Network data buffer management
description: Network data buffer management
keywords:
- WDF Network Adapter Class Extension Buffer Manager, Network data buffer management
ms.date: 02/20/2018
ms.custom: 19H1
---

# Network data buffer management

Buffer management is a feature that enables Network Interface Card (NIC) client drivers and the operating system to work together when allocating packet data buffers from system memory for the transmit (Tx) and receive (Rx) data paths. This can result in faster performance for the NIC, easier memory lifetime management for the NIC's client driver, and more control for the system over the memory.

## The benefits of buffer management in NetAdapterCx

The choice of where data buffers are allocated from system memory for packet payloads is critical to the performance of the data path. In NetAdapterCx, the buffer management model is optimized for DMA-capable NIC hardware, and the best way for client drivers to take advantage of it is to let the system allocate data buffers on their behalf for both the Tx and Rx paths. However, client drivers can still influence where and how the system allocates the data buffers so they can be easily consumed by the client's hardware. 

Consider a typical DMA-capable NIC, for example. There are serval benefits to this approach:

1. The data buffers are allocated and freed by the system. Therefore, the client driver is freed from the burden of memory lifetime management.
2. The system makes sure that the allocated data buffers are DMA-ready for the NIC hardware based on the capabilities declared by the client driver. Then, the client driver can simply program the data buffers into their hardware as-is without performing any additional DMA mapping operations.
3. The system can take the needs of upper layer applications into consideration when allocating the data buffers, so it can decide to optimize for global end-to-end performance instead of only local end-to-end performance.

For non-DMA capabile NICs like a USB-based network dongle, or for other advanced/software NICs, the buffer management model also provides an option to leave data buffer management completely to the client driver. 

## How to leverage buffer management

> [!IMPORTANT]
> If your hardware is DMA-capable, you will need to create a WDFDMAENABLER object before setting your Rx and Tx capabilities. When you configure your WDFDMAENABLER object with the [**WDF_DMA_ENABLER_CONFIG**](/windows-hardware/drivers/ddi/wdfdmaenabler/ns-wdfdmaenabler-_wdf_dma_enabler_config) structure, make sure to set the **WdmDmaVersionOverride** member to **3** to specify DMA version 3.

To opt in to buffer management, follow these steps:

1. When starting your net adapter, but before calling [**NetAdapterStart**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterstart), tell the system about your hardware's data buffer capabilities and constraints using the [**NET_ADAPTER_RX_CAPABILITIES**](/windows-hardware/drivers/ddi/netadapter/ns-netadapter-_net_adapter_rx_capabilities) and [**NET_ADAPTER_TX_CAPABILITIES**](/windows-hardware/drivers/ddi/netadapter/ns-netadapter-_net_adapter_tx_capabilities) data structure for the Rx and Tx path respectively. 
2. Initialize the two capabilities structures by calling one of the initialization functions. For example, a DMA-capable NIC client driver would use [**NET_ADAPTER_TX_CAPABILITIES_INIT_FOR_DMA**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-net_adapter_tx_capabilities_init_for_dma) and [**NET_ADAPTER_RX_CAPABILITIES_INIT_SYSTEM_MANAGED_DMA**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-net_adapter_rx_capabilities_init_system_managed_dma) to declare its hardware DMA capablities and to instruct the system to fully manage the data buffers on its behalf.
3. Pass the initialized Tx and Rx capabilities structures to the [**NetAdapterSetDatapathCapabilities**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadaptersetdatapathcapabilities) method.


## Example

The following example illustrates the basic steps outlined in the previous section for how to get started using the buffer manager in your NIC client driver. The example uses DMA for both Tx and Rx, so it previously created a WDFDMAENABLER object that it stored in its device context space. 

Note that the example also sets some hints about its fragment buffers after it initializes the Tx and Rx capabilities structures. These hints can be used by NetAdapterCx and protocol drivers to improve performance.

Error handling has been left out for clarity.

```C++
VOID
MyAdapterSetDatapathCapabilities(
    _In_ NETADAPTER Adapter
)
{
    // Get the device context
    PMY_DEVICE_CONTEXT deviceContext = GetMyContextFromDevice(Adapter);

    // Set various capabilities such as link layer MTU size, link layer capabilities, and power capabilities
    ...   

    // Initialize the Tx DMA capabilities structure
    NET_ADAPTER_DMA_CAPABILITIES txDmaCapabilities;
    NET_ADAPTER_DMA_CAPABILITIES_INIT(&txDmaCapabilities,
                                      deviceContext->dmaEnabler);

    // Set Tx capabilities
    NET_ADAPTER_TX_CAPABILITIES txCapabilities;
    NET_ADAPTER_TX_CAPABILITIES_INIT_FOR_DMA(&txCapabilities,
                                             &txDmaCapabilities,
                                             1);
    txCapabilities.FragmentRingNumberOfElementsHint = deviceContext->NumTransmitControlBlocks * MAX_PHYS_BUF_COUNT;
    txCapabilities.MaximumNumberOfFragments = MAX_PHYS_BUF_COUNT;

    // Initialize the Rx DMA capabilities structure
    NET_ADAPTER_DMA_CAPABILITIES rxDmaCapabilities;
    NET_ADAPTER_DMA_CAPABILITIES_INIT(&rxDmaCapabilities,
                                      deviceContext->dmaEnabler);

    // Set Rx capabilities
    NET_ADAPTER_RX_CAPABILITIES rxCapabilities;
    NET_ADAPTER_RX_CAPABILITIES_INIT_SYSTEM_MANAGED_DMA(&rxCapabilities,
                                                        &rxDmaCapabilities,
                                                        MAX_PACKET_SIZE + FRAME_CRC_SIZE + RSVD_BUF_SIZE,
                                                        1);
    rxCapabilities.FragmentBufferAlignment = 64;
    rxCapabilities.FragmentRingNumberOfElementsHint = deviceContext->NumReceiveBuffers;

    // Set the adapter's datapath capabilities
    NetAdapterSetDatapathCapabilities(Adapter, 
                                      &txCapabilities, 
                                      &rxCapabilities);
}
```
