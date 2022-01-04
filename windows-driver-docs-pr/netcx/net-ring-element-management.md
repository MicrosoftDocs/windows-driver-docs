---
title: Net ring element management
description: Learn about net ring element management. Manage your structures and their elements during network data transfer.
ms.date: 06/12/2019
---

# Net ring element management

Follow the guidance in this topic to manage your [**NET_RING**](/windows-hardware/drivers/ddi/ring/ns-ring-_net_ring) structures and their elements during network data transfer. The rules in this topic describe which members of the net ring elements client drivers can modify and when, depending on the data path scenario, as well as general information client drivers should keep in mind for these structures. 

> [!IMPORTANT]
> Client drivers should adhere to these directions during all phases of development. If a client driver does not adhere to these directions while testing with [Driver Verifier](../devtest/driver-verifier.md), Driver Verifier reports a violation and triggers a bug check on the device under test.

## NET_RING

When the [**NET_RING**](/windows-hardware/drivers/ddi/ring/ns-ring-_net_ring)'s parent packet queue is started, all indices in the ring are initialized to **0**.

The following table describes which members of the net ring that client drivers can modify.

| Field | Client driver is allowed to modify |
| --- | --- |
| OSReserved1 | No |
| ElementStride | No |
| NumberOfElements | No |
| ElementIndexMask | No |
| EndIndex | No |
| OSReserved0 | No |
| OSReserved2 | No |
| BeginIndex | Yes (Required) |
| NextIndex | Yes (Optional) **Note**: The framework never reads **NextIndex**. |
| Scratch | Yes (Optional) **Note**: The framework never reads **Scratch**. |
| Buffer | No |

Client drivers must not modify any read only members of this structure, nor should they ever increment **BeginIndex** past **EndIndex** during a call to [*EvtPacketQueueAdvance*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance).

For more information about index ownership in net rings, see [Introduction to net rings](introduction-to-net-rings.md).

## NET_PACKET

The fields in a [**NET_PACKET**](/windows-hardware/drivers/ddi/packet/ns-packet-_net_packet) are sensitive to the different contexts in which the data path operates. Whether the packet's **Ignore** field is set and whether the driver is receiving (Rx) or transmitting (Tx) the packet change the ruleset that is applied to the packet.

The following table provides directions for drivers in each scenario.

| Rx or Tx | Ignore field is set by... | Notes |
| --- | --- | --- |
| Rx | Client driver | <ul><li>During Rx, client drivers set **Ignore** if necessary, and the framework reads it. Client drivers do not need to read **Ignore** at any point during Rx.</li><li>If a client driver sets the **Ignore** field during Rx, then:<ul><li>Client drivers must write to the **Ignore** field when canceling Rx operations for any packet that has not been successfully programmed to hardware. For more info, see [Canceling network data with net rings](canceling-network-data-with-net-rings.md).</li><li>Client drivers must not associate resources with the packet because they will not be freed.</li></ul></li><li>If a client driver does not set the **Ignore** field during Rx, then:<ul><li>Client drivers must populate **FragmentIndex**, **FragmentCount**, and all fields in **Layout**.</li><li>**FragmentIndex** must be between **BeginIndex** inclusive and **EndIndex** exclusive in the fragment ring.</li><li>**FragmentCount** cannot exceed the count of fragments between **BeginIndex** inclusive and **EndIndex** exclusive in the fragment ring.</li><li>Client drivers must move the packet ring **BeginIndex** if they move the corresponding fragment ring **BeginIndex**.</li><li>After the call to [*EvtPacketQueueAdvance*](/windows-hardware/drivers/ddi/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance), if a client driver increments the packet ring **BeginIndex** then the driver must also increment the fragment ring **BeginIndex** past the fragments for that packet. In other words, the fragment ring **BeginIndex** should move to the **EndIndex** of the previous packet's fragments.</li></ul></ul> |
| Tx | NetAdapterCx | <ul><li>Client drivers must not modify any fields in any packet except for **Scratch**.</li><li>Client drivers can read the value of **Ignore** but must never write to it.</li><li>If a Tx packet is ignored, the driver must not read any fields except possibly for **Scratch**, if necessary.</li></ul> |

### NET_PACKET_LAYOUT

During Rx operations, the **Layout** field of the [**NET_PACKET**](/windows-hardware/drivers/ddi/packet/ns-packet-_net_packet) is subject to the following rules:

- All fields except for **Reserved0** must be initialized by the client driver.
- If **Layer2Type** is set to **NetPacketLayer2TypeEthernet**, then **Layer2HeaderLength** must be **14** or greater.
- If **Layer2Type** is set to **NetPacketLayer2TypeNull**, then **Layer2HeaderLength** must be set to **0**.
- If **Layer3Type** is an IPv4 type, then **Layer3HeaderLength** must be **20** or greater.
- If **Layer3Type** is an IPv6 type, then **Layer3HeaderLength** must be **40** or greater.
- If **Layer4Type** is set to **Tcp**, then **Layer4HeaderLength** must be **40** or greater.
- If **Layer4Type** is set to **Udp**, then **Layer4HeaderLength** must be **8** or greater.
- The layer type fields must be within the appropriate enum range.

**Layout** is not used during Tx.

## NET_FRAGMENT

[**NET_FRAGMENT**](/windows-hardware/drivers/ddi/fragment/ns-fragment-_net_fragment) field rules depend on whether the driver is receiving or transmitting, and on whether the fragment buffers are attached to the packets by the driver or by the framework.

| Rx or Tx | Notes |
| --- | --- |
| Rx | <ul><li>Client drivers cannot write to the **OsReserved_Bounced** field.</li><li>If the driver is not attaching, then **Capacity** must not be modified but **ValidLength** and **Offset** must be modified.</li><li>If the driver is attaching, then **Capacity**, **ValidLength**, and **Offset** must all be modified.</li><li>**Offset** + **ValidLength** must be less than **Capacity**.</li></ul> |
| Tx | <ul><li>Client drivers cannot modify any fields except for **Scratch**.</li></ul> |
