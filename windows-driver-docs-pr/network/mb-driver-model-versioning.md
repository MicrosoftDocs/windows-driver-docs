---
title: MB Driver Model Versioning
description: MB Driver Model Versioning
ms.date: 04/20/2017
---

# MB Driver Model Versioning


MB driver model versioning is accomplished by having the driver model version and individual OID data structure revisions. This is consistent with the versioning paradigm used in NDIS 6.x.

The driver model version defines the interface evolution between the MB Service and the MB miniport driver. The individual OID revisions keep track of the changes made to OIDs in different MB driver model versions. That is, the driver model version defines a set of OIDs whose data structures are identified by specific revision numbers.

Consistent with the *NDIS Specification*, the MB driver model evolution is *additive*. That is, new OIDs and new members can only be added to existing OID data structures. This ensures that the MB Service can support backward compatibility for miniport drivers.

**Important**  Only under extremely rare circumstances will existing OIDs be deprecated or members of existing OID data structures not be used in the next version. If that happens, these changes and their impacts on backward compatibility shall be clearly documented in subsequent documentation about newer versions of the MB driver model specification.

 

This documentation covers the Windows 8 release of the MB driver model. The driver model version has been incremented to version 2.0. Some OID revisions continue to be revision number 1, while some have been updated to revision 2. For more information about which revisions to use with respective OIDs, see [MB Data Model](mb-data-model.md).

This documentation covers the initial release of the MB driver model, so both the driver model version and individual OID revisions start with revision number 1.

When the driver model moves to the next version, its version number is increased by 1. Any new OIDs added to the driver model will start at revision 1; any existing OIDs whose data structures have changed will increase their corresponding revision by 1, and any existing OIDs that do not change will keep their respective revision numbers.

The driver model version is conveyed by [OID\_WWAN\_DRIVER\_CAPS](./oid-wwan-driver-caps.md). The MB Service sends an OID\_WWAN\_DRIVER\_CAPS query request to the miniport driver during [MB Miniport Driver Initialization](mb-device-readiness.md#mb-miniport-driver-initialization). Individual OID revisions are described by the **Revision** member of the [**NDIS\_OBJECT\_HEADER**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_object_header) structure that is included as part of the data structure for each individual OID.

## See also
[MBIM extension 2.0 versioning for 5G](./mb-5g-operations-overview.md)
