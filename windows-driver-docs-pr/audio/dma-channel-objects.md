---
title: DMA Channel Objects
description: DMA Channel Objects
keywords:
- helper objects WDK audio , DMA channel objects
- DMA channel objects WDK audio
- master devices WDK audio
- IDmaChannel interface
- channel objects WDK audio
ms.date: 09/23/2020
---

# DMA Channel Objects

> [!NOTE]
> Microsoft supports a diverse and inclusive environment. This article contains references to terminology that the [Microsoft style guide for bias-free communication](/style-guide/bias-free-communication) recognizes as exclusionary. The word or phrase is used in this article for consistency because it currently appears in the software. When the software is updated to remove the language, this article will be updated to be in alignment.

The PortCls system driver implements the [IDmaChannel](/windows-hardware/drivers/ddi/portcls/nn-portcls-idmachannel) and [IDmaChannelSlave](/windows-hardware/drivers/ddi/portcls/nn-portcls-idmachannelslave) interfaces for the benefit of WaveCyclic and WavePci miniport drivers. **IDmaChannel** represents a DMA channel plus its associated DMA buffer and buffer-usage parameters. In addition, WaveCyclic miniport drivers use **IDmaChannelSlave** to manage a DMA channel for a subordinate device. **IDmaChannelSlave** inherits from **IDmaChannel**. For information about controlling DMA operations, see [Adapter Objects and DMA](../kernel/introduction-to-adapter-objects.md).

An **IDmaChannel** object encapsulates the following:

- A DMA channel for a master or subordinate device

- The data buffer that is associated with the channel

- Information that describes how the channel is to be used

Port and miniport drivers use DMA channel objects to communicate information regarding DMA channel usage. Typically, a miniport driver allocates a set of DMA channels during initialization or during the creation of a stream. During the creation of a new stream, the miniport driver tells the port driver which DMA channel object will be used for the stream.

A DMA channel object can be created for a master or subordinate device:

- A subordinate device has no built-in DMA-hardware capabilities and must rely on the system DMA controller to perform any data transfers that the device requires.

- A master device uses its own bus-mastering DMA hardware to perform data transfers on the system bus.

For an example of a WaveCyclic device that uses a subordinate DMA channel object, see the Sb16 sample audio driver in earlier versions of the the Microsoft Windows Driver Kit (WDK). A master DMA channel object is little more than a backboard for sharing information about the DMA channel between the port and miniport drivers. For more information about master and subordinate devices, see [Introduction to Adapter Objects](../kernel/introduction-to-adapter-objects.md).

The DMA channel object for a master or subordinate device exposes the following:

- An adapter object

- A single common buffer that the driver and DMA hardware can share

- A buffer-size value that can be queried and changed

The *adapter object* is a DMA-adapter structure for a *physical device object (PDO)*. The adapter object is automatically created when the miniport driver creates the DMA channel object by calling one of the following methods:

[**IPortWavePci::NewMasterDmaChannel**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportwavepci-newmasterdmachannel)

[**IPortWaveCyclic::NewMasterDmaChannel**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportwavecyclic-newmasterdmachannel)

[**IPortWaveCyclic::NewSlaveDmaChannel**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportwavecyclic-newslavedmachannel)

The method [**IDmaChannel::GetAdapterObject**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-getadapterobject) can be used to obtain a pointer to the adapter object.

An adapter driver can also call the [**PcNewDmaChannel**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewdmachannel) function to create a DMA channel object, but this function is more difficult to use than the **IPortWave*Xxx*::New*Xxx*DmaChannel** calls because the caller must explicitly specify a device object and other contextual information.

In the case of a DMA channel for a subordinate device, the [**IDmaChannel::TransferCount**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-transfercount) method returns the maximum transfer size (the *MapSize* parameter) that was specified in the call to [**IDmaChannelSlave::Start**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannelslave-start). Also, the adapter object provides some methods for manipulating and querying the DMA device. None of these methods are meaningful for master DMA channels.

[**IDmaChannel::AllocateBuffer**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-allocatebuffer) and [**IDmaChannel::FreeBuffer**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-freebuffer) are used to manage the single common buffer that is associated with the DMA channel object. The buffer that is allocated by the object is guaranteed to be accessible to both the driver (with kernel virtual-memory addresses) and DMA device (with physical-memory addresses). In addition, the buffer will be physically contiguous. Typically, the best strategy is to allocate the DMA buffer during miniport-driver initialization when physically contiguous memory is most plentiful. [**IDmaChannel::AllocatedBufferSize**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-allocatedbuffersize) returns the size of the buffer as it was specified in the call to **IDmaChannel::AllocateBuffer**.

[**IDmaChannel::MaximumBufferSize**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-maximumbuffersize) indicates the actual maximum buffer size that can be used. This might exceed the allocated size if the allocated size is not an even multiple of the page size. It might be less than the allocated size if the DMA device cannot support transfers of the allocated size. [**IDmaChannel::BufferSize**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-buffersize) and [**IDmaChannel::SetBufferSize**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-setbuffersize) are used to query and set the size of the buffer to be used for DMA transfers. When the buffer is allocated, the buffer size is set to the maximum buffer size. After initialization, both the port driver and miniport driver have the opportunity to change the buffer size or discover its current value. The miniport driver uses the result of **IDmaChannel::BufferSize** to determine the transfer size for DMA operations when the DMA channel is started. [**IDmaChannel::SystemAddress**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-systemaddress) and [**IDmaChannel::PhysicalAddress**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-physicaladdress) are used to obtain the virtual and physical addresses of the buffer, respectively.

[**IDmaChannel::CopyTo**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-copyto) and [**IDmaChannel::CopyFrom**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-copyfrom) copy sample data to and from the DMA buffer. The WaveCyclic port driver calls these methods to copy audio data between the application buffer and the miniport driver's cyclic buffer.

The DMA buffer is not necessarily used to transfer the streamed data. In the case of the WavePci port driver, the streamed data is delivered to (or retrieved from) the miniport driver as a list of scatter/gather mappings. However, the miniport driver might still make use of the DMA buffer as a shared memory space for communicating with the adapter driver.

Port drivers provide miniport drivers with functions that they can use to create DMA channels. Unless otherwise noted in the description of the port driver, it is not absolutely necessary to use DMA objects allocated from the port driver. The port driver simply requires a pointer to an **IDmaChannel** interface that supports the methods it needs. Check the documentation for each port driver for a list of the DMA channel methods that the port driver requires.

Typically, the easiest approach is to use the DMA channel allocation functions that the port driver implements. In rare instances, miniport driver developers might need to implement their own DMA channel objects to meet the special requirements of their particular adapters. This sometimes requires the implementation of a new object. At other times, it is sufficient to have the miniport driver's stream object expose an **IDmaChannel** interface and implement the DMA channel methods itself.

The **IDmaChannel** interface supports the following methods:

[**IDmaChannel::AllocateBuffer**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-allocatebuffer)

[**IDmaChannel::AllocatedBufferSize**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-allocatedbuffersize)

[**IDmaChannel::BufferSize**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-buffersize)

[**IDmaChannel::CopyFrom**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-copyfrom)

[**IDmaChannel::CopyTo**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-copyto)

[**IDmaChannel::FreeBuffer**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-freebuffer)

[**IDmaChannel::GetAdapterObject**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-getadapterobject)

[**IDmaChannel::MaximumBufferSize**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-maximumbuffersize)

[**IDmaChannel::PhysicalAddress**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-physicaladdress)

[**IDmaChannel::SetBufferSize**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-setbuffersize)

[**IDmaChannel::SystemAddress**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-systemaddress)

[**IDmaChannel::TransferCount**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannel-transfercount)

The **IDmaChannelSlave** interface extends **IDmaChannel** by adding the following methods:

[**IDmaChannelSlave::ReadCounter**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannelslave-readcounter)

[**IDmaChannelSlave::Start**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannelslave-start)

[**IDmaChannelSlave::Stop**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannelslave-stop)

[**IDmaChannelSlave::WaitForTC**](/windows-hardware/drivers/ddi/portcls/nf-portcls-idmachannelslave-waitfortc)

 

