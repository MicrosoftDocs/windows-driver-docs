---
title: Virtual Machine Network Adapters
description: Learn about the virtualization types that virtual machine network adapters support, and what steps occur when a user starts or stops a Hyper-V VM.
ms.date: 12/16/2024
---

# Virtual machine network adapters

The virtual machine (VM) network adapter is exposed in the guest operating system that runs in the Hyper-V child partition.

> [!NOTE]
> In Hyper-V, a child partition is also known as a VM.

The VM network adapter supports the following virtualization types:

- **Synthetic network adapter**: The VM network adapter could be a synthetic virtualization of a network adapter. In this case, the network virtual service client (NetVSC) that runs in the VM exposes this virtual network adapter. NetVSC forwards packets to and from the extensible switch port over the VM bus (VMBus).

- **Emulated network adapter**: The VM network adapter could be an emulated virtualization of a physical network adapter. In this case, the VM network adapter mimics an Intel network adapter and uses hardware emulation to forward packets to and from the extensible switch port.

The following diagram shows the interface between VM network adapters and the extensible switch NDIS 6.40 (Windows Server 2012 R2) and later.

:::image type="content" source="images/vswitch-vm-nic-ndis640.png" alt-text="Diagram of flowchart that shows the interface between emulated VM network adapters and the extensible switch for NDIS 6.40.":::

The following diagram shows the interface between VM network adapters and the extensible switch for NDIS 6.30 (Windows Server 2012).

:::image type="content" source="images/vswitch-vm-nic.png" alt-text="Diagram of flowchart that shows the interface between emulated VM network adapters and the extensible switch for NDIS 6.30.":::

## Starting a Hyper-V VM

The following steps occur when the user starts a Hyper-V VM:

1. The protocol edge of the extensible switch issues an object identifier (OID) set request of [OID\_SWITCH\_PORT\_CREATE](./oid-switch-port-create.md) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that a port is being created for the VM.

1. The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CREATE](oid-switch-nic-create.md) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that a network connection for the VM network adapter is being created for the VM port that was previously created.

1. When the networking stacks are operational and have bound to the VM network adapter, the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CONNECT](oid-switch-nic-connect.md) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that a network connection for the VM network adapter is connected and operational. At this point, the extension can inspect, inject, and forward packets to the port that's connected to the VM network adapter.

## Stopping a Hyper-V VM

The following steps occur when the user stops a Hyper-V VM:

1. The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_DISCONNECT](./oid-switch-nic-disconnect.md) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the connection to the VM network adapter is being torn down.

1. After all packet traffic and OID requests that target the network connection are completed, the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the connection to the VM network adapter was gracefully torn down and deleted.

1. The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_TEARDOWN](./oid-switch-port-teardown.md) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the port that was used for the VM network adapter connection is being torn down.

1. The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_DELETE](./oid-switch-port-delete.md) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the VM port was torn down and deleted.
