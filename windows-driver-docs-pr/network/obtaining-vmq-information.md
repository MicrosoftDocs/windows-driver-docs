---
title: Obtaining VMQ Information
description: Obtaining VMQ Information
ms.assetid: e851b656-ef59-42e7-b734-17ce9830096a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining VMQ Information





The VMQ interface includes OID requests and WMI GUIDs that allow overlying drivers and applications to obtain information about the underlying VMQ configuration.

[OID\_RECEIVE\_FILTER\_ENUM\_QUEUES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-enum-queues) enumerates the queues allocated on a network adapter. For more information about enumerating queues, see [Enumerating the Allocated Queues](enumerating-the-allocated-queues.md).

As a method OID request, overlying drivers can use the [OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-queue-parameters) OID to obtain the parameter settings of a particular queue. For more information about obtaining queue parameter settings, see [Obtaining and Updating VM Queue Parameters](obtaining-and-updating-vm-queue-parameters.md).

[OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-enum-filters) enumerates the filters that are allocated on a particular queue. For more information about enumerating the filters that are set on a queue, see [Enumerating Filters on a VMQ](enumerating-filters-on-a-vmq.md).

As a method OID request, overlying drivers can use the [OID\_RECEIVE\_FILTER\_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-parameters) OID to obtain the parameter settings of a filter. For more information about obtaining filter parameter settings, see [Obtaining and Updating VM Queue Parameters](obtaining-and-updating-vm-queue-parameters.md).

Overlying drivers and applications can issue the following OID query requests to obtain the VMQ capabilities.

[OID\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-hardware-capabilities)

[OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-current-capabilities)

[OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-receive-filter-global-parameters)

For more information about obtaining VMQ capabilities, see [Determining the VMQ Capabilities of a Network Adapter](determining-the-vmq-capabilities-of-a-network-adapter.md).

 

 





