---
title: Obtaining VMQ Information
description: Obtaining VMQ Information
ms.date: 04/20/2017
---

# Obtaining VMQ Information





The VMQ interface includes OID requests and WMI GUIDs that allow overlying drivers and applications to obtain information about the underlying VMQ configuration.

[OID\_RECEIVE\_FILTER\_ENUM\_QUEUES](./oid-receive-filter-enum-queues.md) enumerates the queues allocated on a network adapter. For more information about enumerating queues, see [Enumerating the Allocated Queues](enumerating-the-allocated-queues.md).

As a method OID request, overlying drivers can use the [OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](./oid-receive-filter-queue-parameters.md) OID to obtain the parameter settings of a particular queue. For more information about obtaining queue parameter settings, see [Obtaining and Updating VM Queue Parameters](obtaining-and-updating-vm-queue-parameters.md).

[OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](./oid-receive-filter-enum-filters.md) enumerates the filters that are allocated on a particular queue. For more information about enumerating the filters that are set on a queue, see [Enumerating Filters on a VMQ](enumerating-filters-on-a-vmq.md).

As a method OID request, overlying drivers can use the [OID\_RECEIVE\_FILTER\_PARAMETERS](./oid-receive-filter-parameters.md) OID to obtain the parameter settings of a filter. For more information about obtaining filter parameter settings, see [Obtaining and Updating VM Queue Parameters](obtaining-and-updating-vm-queue-parameters.md).

Overlying drivers and applications can issue the following OID query requests to obtain the VMQ capabilities.

[OID\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES](./oid-receive-filter-hardware-capabilities.md)

[OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES](./oid-receive-filter-current-capabilities.md)

[OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS](./oid-receive-filter-global-parameters.md)

For more information about obtaining VMQ capabilities, see [Determining the VMQ Capabilities of a Network Adapter](determining-the-vmq-capabilities-of-a-network-adapter.md).

 

