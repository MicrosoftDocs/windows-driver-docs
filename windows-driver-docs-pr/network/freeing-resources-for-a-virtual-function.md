---
title: Freeing Resources for a Virtual Function
description: Freeing Resources for a Virtual Function
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Freeing Resources for a Virtual Function


The overlying driver requests resource allocation for a PCI Express (PCIe) Virtual Function (VF) through object identifier (OID) method requests of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](./oid-nic-switch-allocate-vf.md). After the VF resources are successfully allocated, the overlying driver frees the resources through an OID set request of [OID\_NIC\_SWITCH\_FREE\_VF](./oid-nic-switch-free-vf.md).

This section includes the following topics:

[Issuing OID\_NIC\_SWITCH\_FREE\_VF Requests](issuing-oid-nic-switch-allocate-vf-requests.md)

[Handling OID\_NIC\_SWITCH\_FREE\_VF Requests](handling-oid-nic-switch-allocate-vf-requests.md)

 

