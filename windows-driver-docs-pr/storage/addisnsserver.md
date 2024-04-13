---
title: AddiSNSServer
description: AddiSNSServer
ms.date: 10/17/2018
---

# AddiSNSServer


The **AddiSNSServer** method adds an iSNS server to the list of iSNS servers that the initiator queries for targets. HBA initiators should store the list of iSNS servers in nonvolatile memory.

This WMI method belongs to the unpublished [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md). For a description of the parameters of the **AddiSNSServer** method, see the member descriptions for the [**AddiSNSServer\_IN**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_addisnsserver_in) and [**AddiSNSServer\_OUT**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_addisnsserver_out) structures.

Miniport drivers that implement the MSiSCSI\_Operations WMI class are not required to support this method.

 

