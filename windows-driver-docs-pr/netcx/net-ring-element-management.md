---
title: Net ring element management
description: USB Dual Role controllers are now supported in Windows, starting with Windows 10.
ms.date: 06/12/2019
ms.localizationpriority: medium
---

# Net ring element management

When testing your NetAdapterCx client driver with [Driver Verifier](../devtest/driver-verifier.md), follow the guidance in this topic to manage your [**NET_RING**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ring/ns-ring-_net_ring) structures and their elements. The rules in this topic describe which members of the net ring elements client drivers can modify and when, depending on the data path scenario, as well as general information client drivers should keep in mind for these structures. If a client driver does not adhere to these directions, Driver Verifier reports a violation and triggers a bug check on the device under test.

## NET_RING

When the [**NET_RING**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ring/ns-ring-_net_ring)'s parent packet queue is started, all indices in the ring are initialized to **0**.

The following table describes which members of the net ring that client drivers can modify.

| Field | Client driver is allowed to modify | Required or Optional to modify | 
| --- | --- | --- |
| OSReserved1 | No | N/A  |
| ElementStride | No | N/A |
| NumberOfElements | No | N/A |
| ElementIndexMask | No | N/A |
| EndIndex | No | N/A |
| OSReserved0 | No | N/A |
| OSReserved2 | No | N/A |
| BeginIndex | Yes | Required |
| NextIndex | Yes | Optional |
| Scratch | Yes | Optional |
| Buffer | No | N/A |

Driver Verifier reports a violation if any of the following occurs in the net ring:

- If **BeginIndex** \> **EndIndex**
- If any read only fields are modified

The framework never reads **NextIndex** or **Scratch**.

## NET_PACKET

The fields in a [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/packet/ns-packet-_net_packet) are sensitive to the different contexts in which the data path operates. Whether the packet's **Ignore** field is set and whether the driver is receiving (Rx) or transmitting (Tx) the packet change the ruleset that is applied to the packet.

The following table provides directions for drivers in each scenario.

| Rx or Tx | Ignore field set | Notes |
| --- | --- | --- |
| Rx | Yes | <ul><li>There is no meaningful way for a client driver to read the **Ignore** field during Rx.</li><li>Client drivers must write to the **Ignore** field when canceling Rx operations.</li><li>If **Ignore** is set during Rx, the framework does not read any other fields. Therefore, client drivers must not associate resources with the packet because they will not be freed.</li></ul> |
| Rx | No | <ul><li>Client drivers must populate **FragmentIndex**, **FragmentCount**, and all fields in **Layout**.</li><li>**FragmentIndex** must be between **BeginIndex** inclusive and **EndIndex** exclusive in the fragment ring.</li><li>**FragmentCount** cannot exceed the count of fragments between **BeginIndex** inclusive and **EndIndex** exclusive in the fragment ring.</li><li>Driver Verifier reports a violation if a client driver moves the fragment **BeginIndex** but not the packet **BeginIndex**.</li>After the call to [*EvtPacketQueueAdvance*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacketqueue/nc-netpacketqueue-evt_packet_queue_advance), if a client driver increments the packet ring **BeginIndex** then the driver must also increment the fragment ring **BeginIndex** past the fragments for that packet. In other words, the fragment ring **BeginIndex** should move to the **EndIndex** of the previous packet's fragments.</li></ul> |
| Tx | Both | <ul><li>Client drivers must not modify any fields in any packet except for **Scratch**.</li></ul> |
| Tx | Yes | <ul><li>Client drivers can read the value of **Ignore** but must never write to it.</li><li>If a Tx packet is ignored, the driver must not read any fields except possibly for **Scratch**, if necessary.</li></ul> |

### NET_PACKET_LAYOUT

The **Layout** field of the [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/packet/ns-packet-_net_packet) is subject to the following rules:

- All fields except for **Reserved0** must be initialized by the client driver.
- If **Layer2Type** is set to **NetPacketLayer2TypeEthernet**, then **Layer2HeaderLength** must be **14** or greater.
- If **Layer2Type** is set to **NetPacketLayer2TypeNull**, then **Layer2HeaderLength** must be set to **0**.
- If **Layer3Type** is an IPv4 type, then **Layer3HeaderLength** must be **20** or greater.
- If **Layer3Type** is an IPv6 type, then **Layer3HeaderLength** must be **40** or greater.
- If **Layer4Type** is set to **Tcp**, then **Layer4HeaderLength** must be **40** or greater.
- If **Layer4Type** is set to **Udp**, then **Layer4HeaderLength** must be **8** or greater.
- The layer type fields must be within the appropriate enum range.

## NET_FRAGMENT

[**NET_FRAGMENT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fragment/ns-fragment-_net_fragment) field rules depend on whether the driver is receiving or transmitting, and on whether the fragment buffers are attached to the packets by the driver or by the framework.

| Rx or Tx | Notes |
| --- | --- |
| Rx | <ul><li>Client drivers cannot write to the **OsReserved_Bounced** field.</li><li>If the driver is *not* attaching, then **Capacity** must not be modified but **ValidLength** and **Offset** must be modified.</li><li>If the driver *is* attaching, then **Capacity**, **ValidLength**, and **Offset** must all be modified.</li><li>**Offset** must be less than **ValidLength**.</li><li>**ValidLength** must be less than **Capacity.**
| Tx | <ul><li>Client drivers cannot modify any fields except for **Scratch**.</li></ul> |