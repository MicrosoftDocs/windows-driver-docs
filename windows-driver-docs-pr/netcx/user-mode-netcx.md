---
title: User-Mode NetAdapterCx
description: Overview of the User-Mode Driver Framework (UMDF) Network Adapter WDF Class Extension (NetAdapterCx).
ms.date: 01/22/2024
---

# User-mode NetAdapterCx
 
Starting in WIN11_NEXT, NetAdapterCx enables you to write a [User-Mode Driver Framework (UMDF)](/wdf/getting-started-with-umdf-version-2) network adapter driver. The UMDF APIs in NetAdapterCx align with the KMDF versions, allowing you to convert your KMDF-based client driver to UMDF with little to no code changes.

## Benefits of user-mode NetAdapterCx drivers

Creating a UMDF NetAdapterCx driver offers these benefits:

1. **Enhanced system stability**: A user-mode driver can only access its process's address space. If it crashes, it doesn't impact the system. The driver can restart automatically, quickly restoring the connection.

1. **Improved security**: User-mode applications can't directly access critical system resources or execute privileged instructions. Therefore, any breach in driver security doesn't compromise the kernel's integrity.
 
1. **Simplified development**: User-mode drivers can enhance the developer's workflow. There's no need to wait for test machines to reboot after crashes, and deployment can be quicker by using the same machine for development and testing.
 
1. **Increased innovation and flexibility**: Kernel-mode driver development constraints often limit innovation. User-mode drivers provide a more flexible environment, allowing developers to use advanced features and tools that might be incompatible or challenging to implement in kernel-mode. 

## Limitations of user-mode NetAdapterCx

The following features are currently only available to KMDF-based NetAdapterCx drivers.

### Direct Memory Access (DMA)

DMA is not yet available in user-mode. 

UMDF drivers must set the **DmaCapabilities** member in 
[**NET_ADAPTER_RX_CAPABILITIES**](/windows-hardware/drivers/ddi/netadapter/ns-netadapter-_net_adapter_rx_capabilities) and [**NET_ADAPTER_TX_CAPABILITIES**](/windows-hardware/drivers/ddi/netadapter/ns-netadapter-_net_adapter_tx_capabilities) to **NULL**.

### Client-side buffer allocation

Client-side [network data buffer management]((network-data-buffer-management.md)) is not available in user-mode. UMDF NetAdapterCx drivers must rely on the system to allocate data buffers for the transmit and receive data paths. 

When your UMDF driver advertises its hardware data buffer capabilities using the [**NET_ADAPTER_RX_CAPABILITIES**](/windows-hardware/drivers/ddi/netadapter/ns-netadapter-_net_adapter_rx_capabilities) structure, it must:

- Set [**NET_RX_FRAGMENT_BUFFER_ALLOCATION_MODE**](/windows-hardware/drivers/ddi/netadapter/ne-netadapter-_net_rx_fragment_buffer_allocation_mode) to **NetRxFragmentBufferAllocationModeSystem**. 
- Set [**NET_RX_FRAGMENT_BUFFER_ATTACHMENT_MODE**](/windows-hardware/drivers/ddi/netadapter/ne-netadapter-_net_rx_fragment_buffer_attachment_mode) to **NetRxFragmentBufferAttachmentModeSystem**. 

## Convert a KMDF NetAdapterCx driver to UMDF

To operate in user-mode, the client driver must only use core WDF APIs that are part of UMDF. For example, the client driver must not use any [APIs exclusive to KMDF drivers](./wdf/comparing-umdf-2-0-functionality-to-kmdf.md).

To convert your KMDF NetAdapterCx driver to UMDF, follow the steps in [How to convert a KMDF driver to a UMDF 2 driver](../wdf/how-to-generate-a-umdf-driver-from-a-kmdf-driver.md).

The UMDF and KMDF versions of NetAdapterCx share the same [major version number](netadaptercx-version-overview.md).
