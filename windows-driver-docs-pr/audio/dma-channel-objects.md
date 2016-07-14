---
Description: DMA Channel Objects
MS-HAID: 'audio.dma\_channel\_objects'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: DMA Channel Objects
---

# DMA Channel Objects


## <span id="dma_channel_objects"></span><span id="DMA_CHANNEL_OBJECTS"></span>


The PortCls system driver implements the [IDmaChannel](audio.idmachannel) and [IDmaChannelSlave](audio.idmachannelslave) interfaces for the benefit of WaveCyclic and WavePci miniport drivers. **IDmaChannel** represents a DMA channel plus its associated DMA buffer and buffer-usage parameters. In addition, WaveCyclic miniport drivers use **IDmaChannelSlave** to manage a DMA channel for a subordinate device. **IDmaChannelSlave** inherits from **IDmaChannel**. For information about controlling DMA operations, see [Adapter Objects and DMA](kernel.adapter_objects_and_dma).

An **IDmaChannel** object encapsulates the following:

-   A DMA channel for a master or subordinate device

-   The data buffer that is associated with the channel

-   Information that describes how the channel is to be used

Port and miniport drivers use DMA channel objects to communicate information regarding DMA channel usage. Typically, a miniport driver allocates a set of DMA channels during initialization or during the creation of a stream. During the creation of a new stream, the miniport driver tells the port driver which DMA channel object will be used for the stream.

A DMA channel object can be created for a master or subordinate device:

-   A subordinate device has no built-in DMA-hardware capabilities and must rely on the system DMA controller to perform any data transfers that the device requires.

-   A master device uses its own bus-mastering DMA hardware to perform data transfers on the system bus.

For an example of a WaveCyclic device that uses a subordinate DMA channel object, see the Sb16 sample audio driver in the Microsoft Windows Driver Kit (WDK). A master DMA channel object is little more than a backboard for sharing information about the DMA channel between the port and miniport drivers. For more information about master and subordinate devices, see [Introduction to Adapter Objects](kernel.introduction_to_adapter_objects).

The DMA channel object for a master or subordinate device exposes the following:

-   An adapter object

-   A single common buffer that the driver and DMA hardware can share

-   A buffer-size value that can be queried and changed

The [*adapter object*](wdkgloss.a#wdkgloss-adapter-object) is a DMA-adapter structure for a [*physical device object (PDO)*](wdkgloss.p#wdkgloss-physical-device-object--pdo-). The adapter object is automatically created when the miniport driver creates the DMA channel object by calling one of the following methods:

[**IPortWavePci::NewMasterDmaChannel**](audio.iportwavepci_newmasterdmachannel)

[**IPortWaveCyclic::NewMasterDmaChannel**](audio.iportwavecyclic_newmasterdmachannel)

[**IPortWaveCyclic::NewSlaveDmaChannel**](audio.iportwavecyclic_newslavedmachannel)

The method [**IDmaChannel::GetAdapterObject**](audio.idmachannel_getadapterobject) can be used to obtain a pointer to the adapter object.

An adapter driver can also call the [**PcNewDmaChannel**](audio.pcnewdmachannel) function to create a DMA channel object, but this function is more difficult to use than the **IPortWave*Xxx*::New*Xxx*DmaChannel** calls because the caller must explicitly specify a device object and other contextual information.

In the case of a DMA channel for a subordinate device, the [**IDmaChannel::TransferCount**](audio.idmachannel_transfercount) method returns the maximum transfer size (the *MapSize* parameter) that was specified in the call to [**IDmaChannelSlave::Start**](audio.idmachannelslave_start). Also, the adapter object provides some methods for manipulating and querying the DMA device. None of these methods are meaningful for master DMA channels.

[**IDmaChannel::AllocateBuffer**](audio.idmachannel_allocatebuffer) and [**IDmaChannel::FreeBuffer**](audio.idmachannel_freebuffer) are used to manage the single common buffer that is associated with the DMA channel object. The buffer that is allocated by the object is guaranteed to be accessible to both the driver (with kernel virtual-memory addresses) and DMA device (with physical-memory addresses). In addition, the buffer will be physically contiguous. Typically, the best strategy is to allocate the DMA buffer during miniport-driver initialization when physically contiguous memory is most plentiful. [**IDmaChannel::AllocatedBufferSize**](audio.idmachannel_allocatedbuffersize) returns the size of the buffer as it was specified in the call to **IDmaChannel::AllocateBuffer**.

[**IDmaChannel::MaximumBufferSize**](audio.idmachannel_maximumbuffersize) indicates the actual maximum buffer size that can be used. This might exceed the allocated size if the allocated size is not an even multiple of the page size. It might be less than the allocated size if the DMA device cannot support transfers of the allocated size. [**IDmaChannel::BufferSize**](audio.idmachannel_buffersize) and [**IDmaChannel::SetBufferSize**](audio.idmachannel_setbuffersize) are used to query and set the size of the buffer to be used for DMA transfers. When the buffer is allocated, the buffer size is set to the maximum buffer size. After initialization, both the port driver and miniport driver have the opportunity to change the buffer size or discover its current value. The miniport driver uses the result of **IDmaChannel::BufferSize** to determine the transfer size for DMA operations when the DMA channel is started. [**IDmaChannel::SystemAddress**](audio.idmachannel_systemaddress) and [**IDmaChannel::PhysicalAddress**](audio.idmachannel_physicaladdress) are used to obtain the virtual and physical addresses of the buffer, respectively.

[**IDmaChannel::CopyTo**](audio.idmachannel_copyto) and [**IDmaChannel::CopyFrom**](audio.idmachannel_copyfrom) copy sample data to and from the DMA buffer. The WaveCyclic port driver calls these methods to copy audio data between the application buffer and the miniport driver's cyclic buffer.

The DMA buffer is not necessarily used to transfer the streamed data. In the case of the WavePci port driver, the streamed data is delivered to (or retrieved from) the miniport driver as a list of scatter/gather mappings. However, the miniport driver might still make use of the DMA buffer as a shared memory space for communicating with the adapter driver.

Port drivers provide miniport drivers with functions that they can use to create DMA channels. Unless otherwise noted in the description of the port driver, it is not absolutely necessary to use DMA objects allocated from the port driver. The port driver simply requires a pointer to an **IDmaChannel** interface that supports the methods it needs. Check the documentation for each port driver for a list of the DMA channel methods that the port driver requires.

Typically, the easiest approach is to use the DMA channel allocation functions that the port driver implements. In rare instances, miniport driver developers might need to implement their own DMA channel objects to meet the special requirements of their particular adapters. This sometimes requires the implementation of a new object. At other times, it is sufficient to have the miniport driver's stream object expose an **IDmaChannel** interface and implement the DMA channel methods itself.

The **IDmaChannel** interface supports the following methods:

[**IDmaChannel::AllocateBuffer**](audio.idmachannel_allocatebuffer)

[**IDmaChannel::AllocatedBufferSize**](audio.idmachannel_allocatedbuffersize)

[**IDmaChannel::BufferSize**](audio.idmachannel_buffersize)

[**IDmaChannel::CopyFrom**](audio.idmachannel_copyfrom)

[**IDmaChannel::CopyTo**](audio.idmachannel_copyto)

[**IDmaChannel::FreeBuffer**](audio.idmachannel_freebuffer)

[**IDmaChannel::GetAdapterObject**](audio.idmachannel_getadapterobject)

[**IDmaChannel::MaximumBufferSize**](audio.idmachannel_maximumbuffersize)

[**IDmaChannel::PhysicalAddress**](audio.idmachannel_physicaladdress)

[**IDmaChannel::SetBufferSize**](audio.idmachannel_setbuffersize)

[**IDmaChannel::SystemAddress**](audio.idmachannel_systemaddress)

[**IDmaChannel::TransferCount**](audio.idmachannel_transfercount)

The **IDmaChannelSlave** interface extends **IDmaChannel** by adding the following methods:

[**IDmaChannelSlave::ReadCounter**](audio.idmachannelslave_readcounter)

[**IDmaChannelSlave::Start**](audio.idmachannelslave_start)

[**IDmaChannelSlave::Stop**](audio.idmachannelslave_stop)

[**IDmaChannelSlave::WaitForTC**](audio.idmachannelslave_waitfortc)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DMA%20Channel%20Objects%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



