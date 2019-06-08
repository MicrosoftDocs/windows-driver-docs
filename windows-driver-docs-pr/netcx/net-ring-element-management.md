---
title: Net ring element management
description: USB Dual Role controllers are now supported in Windows, starting with Windows 10.
ms.date: 06/07/2019
ms.localizationpriority: medium
---

# Net ring element management

When testing your NetAdapterCx client driver with [Driver Verifier](../devtest/driver-verifier.md), follow the guidance in this topic to manage your [**NET_RING**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ring/ns-ring-_net_ring) structures and their elements. The rules in this topic describe which members of the net ring elements client drivers can modify and when, depending on the data path scenario, as well as general information client drivers should keep in mind for these structures. If a client driver does not adhere to these directions, Driver Verifier reports a violation and bug checks the target PC on which the client driver is being tested.

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

The fields in a [**NET_PACKET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/packet/ns-packet-_net_packet) are sensitive to the different contexts in which the data path operates.

## NET_FRAGMENT