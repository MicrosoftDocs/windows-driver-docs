








The client driver can choose to let NetAdapterCx manage the receive buffer.  To opt in:

  1.  Set the **AllocationSize** and **AlignmentRequirement** members of [**NET_RXQUEUE_CONFIG**](net-rxqueue-config.md).
  2.  Call [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983), typically from the [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md) event callback function.
  3.  Call **NetRxQueueQueryAllocatorCacheEnabled** with the initialized WDFDMAENABLER.

NetAdapterCx uses the queue's DMA enabler to allocate pre-mapped buffers for each packet in the queue's [**NET_RING_BUFFER**](net-ring-buffer.md) structure, and updates the **VirtualAddress** and **DmaLogicalAddress** members of each [**NET_PACKET_FRAGMENT**](net-packet-fragment.md) to point to each premapped buffer.

The client driver retrieves a pointer to the ring buffer by calling [**NetTxQueueGetRingBuffer**](nettxqueuegetringbuffer.md) or [**NetRxQueueGetRingBuffer**](netrxqueuegetringbuffer.md).