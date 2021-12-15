---
title: Overview of Network Direct Kernel Provider Interface (NDKPI)
description: This section provides an overview of Network Direct Kernel Provider Interface (NDKPI)
ms.date: 04/20/2017
---

# Overview of Network Direct Kernel Provider Interface (NDKPI)


The Network Direct Kernel Provider Interface (NDKPI) is an extension to NDIS that allows IHVs to provide kernel-mode Remote Direct Memory Access (RDMA) support in a network adapter (also called an RNIC). To expose the adapter's RDMA functionality, the IHV must implement the NDKPI interface as defined in the [NDKPI Reference](/windows-hardware/drivers/ddi/_netvista/).

-   [NDKPI and RDMA](#ndkpi-and-rdma)
-   [The NDK provider](#the-ndk-provider)
-   [The NDK consumer](#the-ndk-consumer)

### NDKPI and RDMA

A NIC vendor implements RDMA as a combination of software, firmware, and hardware. The hardware and firmware portion is a network adapter that provides NDK/RDMA functionality. This type of adapter is also called an RDMA-enabled NIC (RNIC). The software portion is an NDK-capable miniport driver, which implements the NDKPI interface.

The Windows implementation of RDMA is called Network Direct (ND). The kernel portion is called Network Direct Kernel (NDK).

NDK providers must support Network Direct connectivity via both IPv4 and IPv6 addresses assigned to NDK-capable miniport adapters.

For more information about RDMA, see [Background Reading on RDMA](background-reading-on-rdma.md).

### The NDK provider

An NDK provider is a miniport driver that implements the NDKPI interface.

The NDK provider is loaded and initialized by the PnP Manager. For more information, see [Initializing an NDK-Capable Miniport Driver](initializing-an-ndk-capable-miniport-driver.md) and [Initializing an NDK Miniport Adapter](initializing-an-ndk-miniport-adapter.md).

Once the NDK provider is loaded and initialized, it is ready to handle requests from the NDK consumer. These requests arrive as calls to provider functions.

When handling requests from an NDK consumer, the provider can call the consumer's NDK callback functions. These are documented in [NDKPI Consumer Callback Functions](/windows-hardware/drivers/ddi/_netvista/).

NDK providers must implement all elements of the NDKPI interface that are documented in the [NDKPI Reference](/windows-hardware/drivers/ddi/_netvista/), except for the [NDKPI Consumer Callback Functions](/windows-hardware/drivers/ddi/_netvista/).

### The NDK consumer

NDK consumers are kernel-mode Windows components, such as SMB server and client.

**Note**  This documentation does not discuss how to implement an NDK consumer. The NDKPI consumer device driver interface (DDI) is a proprietary Windows-internal interface.

 

An NDK consumer calls the provider's *NdkOpenAdapter* ([*OPEN\_NDK\_ADAPTER\_HANDLER*](/windows-hardware/drivers/ddi/ndisndk/nc-ndisndk-open_ndk_adapter_handler)) callback function to create an adapter object and *NdkCloseAdapter* ([*NDK\_FN\_CLOSE\_OBJECT*](/windows-hardware/drivers/ddi/ndkpi/nc-ndkpi-ndk_fn_close_object)) to close it. Once the provider has created the adapter object, the consumer calls other provider callback functions to create additional NDK objects.

NDK consumers implement the [NDKPI Consumer Callback Functions](/windows-hardware/drivers/ddi/_netvista/), which are called by NDK providers.


 

