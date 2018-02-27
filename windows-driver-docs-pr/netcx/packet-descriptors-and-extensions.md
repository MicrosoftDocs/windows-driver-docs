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

This topic introduces concepts underlying packet descriptors and extensions in NetAdapterCx 1.2 and later.

## Overview

*Packet descriptors* are small, runtime-extensible structures that describe a network packet. They can be used by different components in the system and are not limited in scope to specific APIs or header files. Each packet has one core descriptor that is used to hold OS-specific information.

*Packet extensions* are attached to each packet's core descriptor and are used by client drivers to hold per-packet metadata to share with the upper layers. Extensions can hold advanced offload information like checksum, large send offload (LSO), and receive side scaling (RSS) hash results, or they can also hold application-specific details.

## Packet descriptor and extension design and benefits

NetAdapterCx 1.2 introduces packet descriptors and a system for NIC client drivers to use packet extensions. Packet descriptors used by NetAdapterCx 1.2 and later are designed for high scalability and provide the follwing benefits.

### Extensibility

Extensibility is a core feature of the NetAdapterCx packet descriptor, as it also affects versionability and performance. At runtime, a client driver can allocate a context block on all packet descriptors in a collection (in other words, on a datapath queue). This enables the operating system to allocate all descriptors with pre-allocated extensions inline with the descriptor. Each extension block is appended to a core descriptor, as shown in the following figure:

![NetAdapterCx packet descriptor layout](images/packet-descriptors-1-layout.png)

Drivers are not permitted to hardcode the offset to any extension block – instead, they must query at runtime for the offset to any particular extension. For example, a driver might query the offset to Extension B, and get back 70 bytes like in the following figure:

![Querying the offset to an extension of the core packet descriptor](images/packet-descriptors-2-offset-query.png)

Once a descriptor is created, all its offsets are guaranteed by the OS to be constant, so drivers don't have to re-query offsets often. 

Extensions are named with a string and a version number, and can be created by a client driver. For example, an IHV might insert an extension for custom Quality of Service (QoS) features and query the offset to that extension in a value-add protocol driver.

Because extensions are pre-allocated by the OS in an array at the time the datapath queue is initialized, there is no need for runtime allocation of blocks, searching a list for a specific descriptor, or having to store pointers to every packet extension.

### Versionability

NetAdapterCx's packet descriptor can be easily versioned by adding new fields to the end, such as in the following figure:

![NetAdapterCx core packet descriptor versioning](images/packet-descriptors-3-core-descriptor-versioning.png)

Drivers that know about the V2 fields can access them, while V1 drivers will use extension offsets to skip over the V2 fields so they can access the fields they do understand. In addition, each extension can be versioned in the same way, as the following figure shows:

![NetAdapterCx packet extension versioning](images/packet-descriptors-4-extension-versioning.png)

A driver that understands the new extension can use it. Other drivers can skip over the new fields. This permits different parts of the packet descriptor to be versioned independently.

### Performance

NetAdapterCx client drivers can target network interface cards (NICs) that are capabable of hundreds of gigabits per second (Gbps), with thousands of RSS queues. The extensibility model outlined previously provides benefits to help meet these performance goals:

1. Extensions are allocated at queue creation time, so drivers don't have to allocate and deallocate memory in the active data path or deal with lookaside lists of context blocks.
2. Extensions are in-line, which improves CPU cache hits.
3. There is no need for pointers, which saves space.
4. Features that aren't used occupy 0 bytes of space.

## Using packet extensions in a NetAdapterCx client driver

