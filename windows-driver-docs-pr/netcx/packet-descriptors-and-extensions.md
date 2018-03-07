---
title: Packet descriptors and extensions
description: Packet descriptors and extensions
ms.assetid: 7B2357AE-F446-4AE8-A873-E13DF04D8D71
keywords:
- WDF Network Adapter Class Extension packet descriptors and extensions, NetAdapterCx packet descriptors, NetAdapterCx packet extensions
ms.author: windowsdriverdev
ms.date: 02/22/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Packet descriptors and extensions

In NetAdapterCx, *Packet descriptors* are small, compat and runtime-extensible structures that describe a network packet. Each packet requires 
- one core descriptor 
- one or more fragment descriptors
- zero or more packet extensions 

*Core descriptor* ([*NET_PACKET*]()) contains the most basic metadata applicable for any packets, such like the framing layout of a given packet and the index to the first fragment descriptor.   

*Fragment descriptor* ([*NET_PACKET_FRAGMENT*]()) describes the location within the system memory where the packet data resides. There is at least one fragment descriptor per packet.

*Packet extensions* are optional and hold per-packet metadata for scenario-specific features. For instance, extensions can hold offload information for checksum, large send offload (LSO), and receive segment coalescence (RSC), or they can also hold application-specific details.

They together hold all the metadata about the packet and below are two examples of how they describe a packet: the first figure shows a scenario that the entire packet stored inside a single memory fragment and checksum offload has been turned on for this packet; the second figure shows a packet stored across two memory fragments and it has both RSC and checksum offload enabled

![1 fragment packet layout](images/packet-one-frag.png)


![2 fragments packet layout](images/packet-two-frag.png)

## Extensibility

Extensibility is a core feature of the NetAdapterCx packet descriptor, and it's the fundation for the descriptor's versionability and performance. At runtime, the operating system allocates all packets descriptors of a given packet queue in a contiguous block, together with any avaiable extensions. Each extension block is immediately behind the core descriptor, as shown in the following figure:

![NetAdapterCx packet descriptor layout](images/packet-descriptors-1-layout.png)

The client drivers are not permitted to hardcode the offset to any extension block. Instead, they must query at runtime for the offset to any particular extension. For example, a driver might query the offset to Extension B, and get back 70 bytes like in the following figure:

![Querying the offset to an extension of the core packet descriptor](images/packet-descriptors-2-offset-query.png)

Once a packet queue and its descriptors are created, all their extension offsets are guaranteed by the OS to be constant, so drivers don't have to re-query offsets often. Furthermore, because all extensions are pre-allocated by the OS in a block at the time the packet queue is initialized, there is no need for runtime allocation of blocks, searching a list for a specific descriptor, or having to store pointers to every packet extension.

## Versionability

NetAdapterCx's core packet descriptor can be easily extended in future release by adding new fields to the end, such as in the following figure:

![NetAdapterCx core packet descriptor versioning](images/packet-descriptors-3-core-descriptor-versioning.png)

The newer client drivers that know about the V2 fields can access them, while older V1-only drivers will use extension offsets to skip over the V2 fields so they can access the fields they do understand. In addition, each extension can be versioned in the same way, as the following figure shows:

![NetAdapterCx packet extension versioning](images/packet-descriptors-4-extension-versioning.png)

A client driver that understands the new extension can use it. Other client drivers can skip over the new fields. This permits different parts of the packet descriptor to be versioned independently.

## Performance
The extensibility feature outlined previously provides benefits to help the client drivers meet the performance requirements of NICs that are capabable of hundres of gigabits per second and with thousands of queues:

1. The packet descriptors are kept as compact as possible to improve CPU cache hits, as features/extensions that aren't used occupy 0 bytes of space in the descriptors. 
2. There is no pointer dereferencing but just offset arithmetic because extensions are in-line, which not only saves space but also helps with CPU cache hits. 
3. Extensions are allocated at queue creation time, so drivers don't have to allocate and deallocate memory in the active data path or deal with lookaside lists of context blocks.

## Using packet extension in the client driver

Currently, the client drivers are limited to [those pre-existing packet extensions defined by the operating system](#Predefined-packet-extension-constants-and-helper-methods).   

### Registering packet extensions

The first step in working with packet extensions in your NIC client driver is to declare and register them in your *[EvtNetAdapterSetCapabilities](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_set_capabilities)* callback function. You might do so like in the following example. Note that the example leaves out error handling for clarity.

> [!IMPORTANT]
> This example calls the **NetAdapterRegisterPacketExtension** method, which is available in the *NetPacketExtensionP.h* header from the [Realtek Github sample driver](https://github.com/Microsoft/NetAdapter-Cx-Driver-Samples/tree/master/RtEthSample). Because this header is prereleased product, it may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the contents of this header.

```
NTSTATUS
MyAdapterSetCapabilities(
    NETADAPTER Adapter
)
{
    NTSTATUS status = STATUS_SUCCESS;

    // Set various capabilities such as link layer MTU size, link layer capabilities, power capabilities,
    // and datapath capabilities
    ...   

    // Register the checksum extension
    NET_PACKET_EXTENSION extension;
    NET_PACKET_EXTENSION_INIT(
        &extension,
        NET_PACKET_EXTENSION_CHECKSUM_NAME,
        NET_PACKET_EXTENSION_CHECKSUM_VERSION_1,
        NET_PACKET_EXTENSION_CHECKSUM_VERSION_1_SIZE,
        sizeof(ULONG) - 1);

    status = NetAdapterRegisterPacketExtension(netAdapter, &extension);

    // Register the LSO extension
    NET_PACKET_EXTENSION_INIT(
        &extension,
        NET_PACKET_EXTENSION_LSO_NAME,
        NET_PACKET_EXTENSION_LSO_VERSION_1,
        NET_PACKET_EXTENSION_LSO_VERSION_1_SIZE,
        sizeof(ULONG) - 1);

    status = NetAdapterRegisterPacketExtension(netAdapter, &extension);

    // Set other needed capabilities
    ...
}
```

### Querying packet extension offsets for datapath queues

After registering packet extensions during *EvtNetAdapterSetCapabilities*, you'll need the extension offsets to access each one as you process your packets. To reduce calls out of your driver and improve performance, you can query the offsets for your extensions during the *EvtNetAdapterCreateTx(Rx)Queue* callback function and store the offset information in your queue context. Here is an example for a transmit queue. This example is similar to the example on *[EvtNetAdapterCreateTxQueue](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_txqueue)* but focuses only on packet extensions.

```C++
NTSTATUS
MyAdapterCreateTxQueue(
    _In_    NETADAPTER netAdapter,
    _Inout_ PNETTXQUEUE_INIT txQueueInit)
{
    NTSTATUS status = STATUS_SUCCESS;

    // Prepare the configuration structure
    NET_TXQUEUE_CONFIG txConfig;
    NET_TXQUEUE_CONFIG_INIT(
        &txConfig,
        EvtTxQueueAdvance,
        EvtTxQueueSetNotificationEnabled,
        EvtTxQueueCancel);

    // Configure other Tx queue properties such as packet contexts
    ...

    // Create the transmit queue
    NETTXQUEUE txQueue;
    status = NetTxQueueCreate(
        txQueueInit,
        &txAttributes,
        &txConfig,
        &txQueue);

    // Get the queue context for storing the queue ID and packet extension offset info
    PMY_TX_QUEUE_CONTEXT queueContext = GetMyTxQueueContext(txQueue);

    // Query checksum packet extension offset and store it in the context
    NET_PACKET_EXTENSION_QUERY extension;
    NET_PACKET_EXTENSION_QUERY_INIT(
        &extension,
        NET_PACKET_EXTENSION_CHECKSUM_NAME,
        NET_PACKET_EXTENSION_CHECKSUM_VERSION_1);

    queueContext->ChecksumExtensionOffset = NetTxQueueGetPacketExtensionOffset(txQueue, &extension);

    // Query Large Send Offload packet extension offset and store it in the context
    NET_PACKET_EXTENSION_QUERY_INIT(
        &extension,
        NET_PACKET_EXTENSION_LSO_NAME,
        NET_PACKET_EXTENSION_LSO_VERSION_1);
    
    queueContext->LsoExtensionOffset = NetTxQueueGetPacketExtensionOffset(txQueue, &extension);

    return status;
}
```

### Getting packet extensions at runtime

Once you have stored extension offsets in your queue context, you can use them any time you need information in an extension. For example, you could call the [NetPacketGetPacketChecksum](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/nf-netpacket-netpacketgetpacketchecksum) method while you program descriptors to hardware:

```C++
    // Get the extension offset from the device context
    PMY_TX_QUEUE_CONTEXT queueContext = GetMyTxQueueContext(txQueue);
    size_t checksumOffset = queueContext->ChecksumExtensionOffset;

    // Get the checksum info for this packet
    NET_PACKET_CHECKSUM* checksumInfo = NetPacketGetChecksum(packet, checksumOffset);

    // Do work with the checksum info
    if(checksumInfo->Layer4 == NET_PACKET_TX_CHECKSUM_REQUIRED)
    {
        ...
    }
```

## Predefined packet extension constants and helper methods

NetAdapterCx provides definitions for known packet extensions constants.

| Constant | Definition |
| --- | --- |
| NET_PACKET_EXTENSION_INVALID_OFFSET | Guards against invalid offset sizes. |
| <ul><li>NET_PACKET_EXTENSION_CHECKSUM_NAME</li><li>NET_PACKET_EXTENSION_CHECKSUM_VERSION_1</li><li>NET_PACKET_EXTENSION_CHECKSUM_VERSION_1_SIZE</li></ul> | The name, version, and size of the checksum packet extension. |
| <ul><li>NET_PACKET_EXTENSION_LSO_NAME</li><li>NET_PACKET_EXTENSION_LSO_VERSION_1</li><li>NET_PACKET_EXTENSION_LSO_VERSION_1_SIZE</li></ul> | The name, version, and size of the large send offload (LSO) packet extension. |
| <ul><li>NET_PACKET_EXTENSION_RSC_NAME</li><li>NET_PACKET_EXTENSION_RSC_VERSION_1</li><li>NET_PACKET_EXTENSION_RSC_VERSION_1_SIZE</li></ul> | The name, version, and size of the receive segment coalescence (RSC) packet extension. |

Additionally, NetAdapterCx provides three helper methods that act as wrappers around the [NetPacketGetExtension](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/nf-netpacket-netpacketgetextension) method. Each of these methods returns a pointer to the appropriate type of structure.

| Method | Structure |
| --- | --- |
| [NetPacketGetPacketChecksum](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/nf-netpacket-netpacketgetpacketchecksum) | [NET_PACKET_CHECKSUM](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet_checksum) |
| [NetPacketGetPacketLargeSendSegmentation](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/nf-netpacket-netpacketgetpacketlargesendsegmentation) | [NET_PACKET_LARGE_SEND_SEGMENTATION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet_large_send_segmentation)
| [NetPacketGetPacketReceiveSegmentCoalescence](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/nf-netpacket-netpacketgetpacketreceivesegmentcoalescence) | [NET_PACKET_RECEIVE_SEGMENT_COALESCENCE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet_receive_segment_coalescence) |
