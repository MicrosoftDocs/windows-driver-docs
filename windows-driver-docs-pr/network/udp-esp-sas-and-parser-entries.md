---
title: UDP-ESP SAs and Parser Entries
description: UDP-ESP SAs and Parser Entries
ms.assetid: 1682b077-07ba-4b2e-9c01-fd7662f3f189
keywords:
- UDP-encapsulated ESP packets WDK IPsec offload , parser entries
- parser entries WDK IPsec offload
- UDP-encapsulated ESP packets WDK IPsec offload , security associations
- security associations WDK IPsec offload
- SAs WDK IPsec offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UDP-ESP SAs and Parser Entries

\[The IPsec Task Offload feature is deprecated and should not be used.\]




A miniport driver that supports UDP-ESP encapsulation must maintain a list of parser entries. A parser entry contains information that a NIC requires to parse incoming UDP-ESP packets on offloaded security associations (SAs).

A parser entry contains the following information:

-   The UDP-ESP encapsulation type.

    Currently, only one encapsulation type is supported. For a description of the basic UDP-ESP encapsulation types, see [UDP-ESP Encapsulation Types](udp-esp-encapsulation-types.md).

-   The destination encapsulation port.

    The NIC should look for the destination port in the UDP header of inbound UDP-encapsulated packets that it processes on the offloaded SAs. Currently, UDP encapsulation of ESP packets is supported only on port 4500.

The TCP/IP transport maintains its own list of parser entries that it has offloaded to the miniport driver. When adding or deleting a UDP-ESP SA, the transport and miniport driver use a handle to identify a particular parser entry.

Note that parser entries allow UDP-ESP functionality to be extended, if necessary, to accommodate different encapsulation types and more than one port for each encapsulation type.

### Adding a UDP-ESP SA and Parser Entry

The TCP/IP transport requests a miniport driver to add one or more UDP-ESP SAs, and the parser entry for these SAs, by issuing an [OID\_TCP\_TASK\_IPSEC\_ADD\_UDPESP\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569809) request. The **EncapTypeEntry** member of the OFFLOAD\_IPSEC\_ADD\_UDPESP\_SA structure contains the parser entry information.

Before issuing an OID\_TCP\_TASK\_IPSEC\_ADD\_UDPESP\_SA request, the TCP/IP transport determines whether the parser entry for the SAs that is being offloaded is in its parser entry list for the specified IP interface.

-   If the parser entry is not in the transport's list, the transport creates its own copy of the entry and sets the **EncapTypeEntryOffloadHandle** member of the OFFLOAD\_IPSEC\_ADD\_UDPESP\_SA structure to **NULL**. The transport then issues the [OID\_TCP\_TASK\_IPSEC\_ADD\_UDPESP\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569809) request. After receiving the request, the miniport driver determines whether the parser entry that the **EncapTypeEntry** specified is in the NIC's parser entry list.

    -   If the specified parser entry is not in the NIC's parser entry list, the miniport driver creates the parser entry by using the encapsulation type and destination port specified in **EncapTypeEntry** and adds the parser entry to the NIC's parser entry list. The miniport driver then offloads the SAs specified in the OID\_TCP\_TASK\_IPSEC\_ADD\_UDPESP\_SA request. After successfully completing the OID request, the miniport driver returns a handle in **EncapTypeEntryOffloadHandle** that identifies the newly created parser entry. The miniport driver also returns a handle that identifies the offloaded SAs in the **OffloadHandle** member of the OFFLOAD\_IPSEC\_ADD\_UDPESP\_SA structure.
    -   If the specified parser entry is already in the NIC's parser entry list, the miniport driver simply returns the handle in **EncapTypeEntryOffloadHandle** for the existing parser entry. The miniport driver also returns a handle that identifies the offloaded SAs in the **OffloadHandle** member of the OFFLOAD\_IPSEC\_ADD\_UDPESP\_SA structure.

    If the miniport driver completes the OID\_TCP\_TASK\_IPSEC\_ADD\_UDPESP\_SA request successfully, the transport adds its copy of the new parser entry to its own parser entry list for the given IP interface. In addition, the transport increments the reference count for the parser entry by one. The transport uses this reference count to enumerate how many offloaded UDP-ESP SAs are associated with the parser entry.

    If the miniport driver fails the OID\_TCP\_TASK\_IPSEC\_ADD\_UDPESP\_SA request, the transport discards its copy of the parser entry. If the miniport driver fails such a request, it must ensure that it has not, in fact, added the parser entry and offloaded the SAs.

-   If the parser entry is already in the transport's parser entry list, the miniport driver has already added the parser entry in response to a previous OID\_TCP\_TASK\_IPSEC\_ADD\_UDPESP\_SA request. In this case, the transport increments the reference count for the parser entry by one and sets the **EncapTypeEntryOffloadHandle** to the value that the miniport driver previously returned. The transport then issues an OID\_TCP\_TASK\_IPSEC\_ADD\_UDPESP\_SA request This requests the miniport driver to use an existing parser entry for the additional SAs that are being offloaded. In this case, the miniport driver should simply return an **OffloadHandle** that identifies the offloaded SAs. If the OID\_TCP\_TASK\_IPSEC\_ADD\_UDPESP\_SA request fails, the transport decrements the reference count for the parser entry.

### Deleting a UDP-ESP SA and Parser Entry

The TCP/IP transport requests a miniport driver to delete one or more SAs and possibly the parser entry for these SAs by issuing an [OID\_TCP\_TASK\_IPSEC\_DELETE\_UDPESP\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569811) request.

Before issuing this request, the TCP/IP transport decrements the reference count for the parser entry that is associated with the SAs to be deleted. The transport then tests whether the reference count is zero.

-   If the reference count is not zero, the parser entry is associated with one or more other SAs that are currently offloaded to the NIC. In this case, the transport sets the **EncapTypeEntryOffldHandle** member of the OFFLOAD\_IPSEC\_DELETE\_UDPESP\_SA structure to **NULL**. After it receives the OID\_TCP\_TASK\_IPSEC\_DELETE\_UDPESP\_SA request, the miniport driver simply deletes the SAs that are specified in the OID\_TCP\_TASK\_IPSEC\_DELETE\_UDPESP\_SA request.

-   If the reference count is zero, the parser entry is not associated with any other SAs that have been offloaded to the NIC. In this case, the transport sets the **EncapTypeEntryOffldHandle** member to the value of the parser entry handle that the miniport driver previously returned. The miniport driver deletes both the specified parser entry and the specified SAs.

If the miniport driver fails the OID\_TCP\_TASK\_IPSEC\_DELETE\_UDPESP\_SA request, it should mark the specified SAs and, if appropriate, the specified parser entry for deletion and perform the deletion later. To process incoming packets, the miniport driver must not use a parser entry or SA that is marked for deletion.

Note that a transport could request a miniport driver to delete an SA or a parser entry (or both) before the miniport driver completes adding that SA or parser entry (or both). The miniport driver must therefore serialize the deletion operation with the addition operation.

 

 





