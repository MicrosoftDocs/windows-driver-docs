---
title: ReportDiscoveredTargets2
description: ReportDiscoveredTargets2
ms.date: 10/17/2018
---

# ReportDiscoveredTargets2


The **ReportDiscoveredTargets2** WMI method reports all discovered targets.

This WMI method belongs to the unpublished [MSiSCSI\_DiscoveryOperations WMI class](msiscsi-discoveryoperations-wmi-class.md) that is defined in *Discover.mof*. For a description of the parameters of the **ReportDiscoveredTargets2** method, see the member descriptions for the [**ReportDiscoveredTargets2\_OUT**](/windows-hardware/drivers/ddi/iscsifnd/ns-iscsifnd-_reportdiscoveredtargets2_out) structure.

**ReportDiscoveredTargets2** is similar to the [ReportDiscoveredTargets](reportdiscoveredtargets.md) method, but **ReportDiscoveredTargets2** reports target portal information that the **ReportDiscoveredTargets** method does not report, such as the tag number for the portal group.

Miniport drivers that implement the MSiSCSI\_DiscoveryOperations WMI class must support **ReportDiscoveredTargets2**.

 

