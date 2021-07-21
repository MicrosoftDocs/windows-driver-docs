---
title: RemoveiSNSServer
description: RemoveiSNSServer
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# RemoveiSNSServer


The **RemoveiSNSServer** method removes an iSNS server from the list of iSNS servers that the initiator queries for targets. HBA initiators should store the list of iSNS servers in nonvolatile memory.

**RemoveiSNSServer** belongs to the unpublished [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md). For a description of the parameters of the **RemoveiSNSServer** method, see the member descriptions for the [**RemoveiSNSServer\_IN**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_removeisnsserver_in) and [**RemoveiSNSServer\_OUT**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_removeisnsserver_out) structures.

Miniport drivers that implement the MSiSCSI\_Operations WMI class are not required to support this method.

 

