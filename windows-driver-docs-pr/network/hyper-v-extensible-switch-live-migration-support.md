---
title: Hyper-V Extensible Switch Live Migration Support
description: Hyper-V Extensible Switch Live Migration Support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch Live Migration Support


During a Hyper-V live migration, a child partition, or *virtual machine (VM)*, is stopped on one host computer (*source host*) and migrated to another host computer (*destination host*). During live migration, the following operations occur:

-   When the live migration starts on the source host, the extensible switch interface requests underlying extensions to save run-time data for each port and its associated network adapter connection.

    For more information about this operation, see [Hyper-V Extensible Switch Save Operations](hyper-v-extensible-switch-save-operations.md).

-   Before the live migration completes on the destination host, the extensible switch interface requests underlying extensions to restore run-time data for each port and its associated network adapter connection.

    For more information about this operation, see [Hyper-V Extensible Switch Restore Operations](hyper-v-extensible-switch-restore-operations.md).

During the live migration setup stage, the source host creates a TCP connection with the destination physical host. Hyper-V transfers the source VM's configuration data over this connection to the destination physical host. A skeleton VM is set up on the destination host and memory is allocated to the destination VM. At this point, Hyper-V transfers the source VM's state, including its memory pages, to the destination VM.

The extensible switch interface also uses the TCP connection to synchronize steps and results during the live migration. For example, the interface that runs on the destination host requests the transfer of run-time data from the source host for the port and network adapter connection associated with the migrated VM.

Before the destination VM is brought online on the destination host, the extensible switch interface performs these steps:

1.  A validation port is created on the destination host through an object identifier (OID) set request of [OID\_SWITCH\_PORT\_CREATE](./oid-switch-port-create.md). If the port is created successfully, the extensible switch interface issues other OID requests to verify the properties of port policies by underlying extensions.

    If the extension fails the port creation or invalidates any of the policy properties, the live migration does not continue for that destination node and switch.

    For more information about the validation port and its usages, see [Validation Ports](validation-ports.md).

2.  After the verification of policy properties is completed successfully, the validation port is deleted on the destination host through an OID set request of [OID\_SWITCH\_PORT\_DELETE](./oid-switch-port-delete.md). After this port is deleted, an operational port is created on the destination host and an operational port is created in its place. The [**NDIS\_SWITCH\_PORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_parameters) structure that is associated with the [OID\_SWITCH\_PORT\_CREATE](./oid-switch-port-create.md) request for the operational port contains the same data that was used to create the port on the source host.

    If the operational port is created successfully, port policies are added to the operational port.

3.  If the settings are successfully applied to the operational port on the destination host, a save operation is issued for the operational port on the source host.

4.  If the save operation is completed successfully, the operational port and its network adapter connection are deleted on the source host in the following way:

    1.  The network connection is first disconnected through an OID set request of [OID\_SWITCH\_NIC\_DISCONNECT](./oid-switch-nic-disconnect.md). After this OID request is completed, the network adapter connection on the source host is deleted through an OID set request of [OID\_SWITCH\_NIC\_DELETE](./oid-switch-nic-delete.md).

    2.  After the network adapter connection is deleted, the operational port is torn down through an OID set request of [OID\_SWITCH\_PORT\_TEARDOWN](./oid-switch-port-teardown.md). After this OID request is completed, the operational port is deleted through an OID set request of OID\_SWITCH\_PORT\_DELETE.

5.  A network adapter connection is created for the operational port on the destination host through an OID set request of [OID\_SWITCH\_NIC\_CREATE](./oid-switch-nic-create.md). If this OID request completes successfully, the network adapter connection is established on the associated operation port through an OID set request of [OID\_SWITCH\_NIC\_CONNECT](./oid-switch-nic-connect.md).

    If the network adapter connection is established successfully, the run-time data for the operational port and network adapter connection is restored on the target host.

    At this point, the underlying extensions can perform resource reservation and validation on the network adapter connection.

 

