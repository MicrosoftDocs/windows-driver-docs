---
title: NDIS Object Version Issues for WMI
description: NDIS Object Version Issues for WMI
keywords:
- NDIS version information WDK , WMI support
ms.date: 03/02/2023
---

# NDIS Object Version Issues for WMI





This topic describes the NDIS object version issues that affect Windows Management Instrumentation (WMI) support.

There is no versioning inside a WMI managed object format (MOF) file. Therefore, if the corresponding NDIS structure has a new revision, more fields have been added to the MOF data objects.

The NDIS\_WMI\_Xxx\_HEADER structures have a new revision when more members are added for a new NDIS version. For a list of the current NDIS\_WMI\_Xxx\_HEADER structures, see [NDIS WMI Structures](/windows-hardware/drivers/ddi/ntddndis/index).

When applications access the WMI information for a query operation, they must check the version in the returned buffer before they access any data. For a set operation, applications must check the **SupportedRevision** member in the NDIS\_WMI\_OUTPUT\_INFO structure to determine which version the underlying driver has accepted.

Many WMI objects contain the **MSNdis\_ObjectHeader** property, which is equivalent to the [**NDIS\_OBJECT\_HEADER**](/windows-hardware/drivers/ddi/objectheader/ns-objectheader-ndis_object_header) structure. When populating the **MSNdis\_ObjectHeader** property, set the **Type** and **Revision** fields as documented in the **NDIS\_OBJECT\_HEADER** topic. To ensure seamless portability to 64-bit systems, set the **Size** field to `0xFFFF`.

## Related topics


[Overview of NDIS versions](overview-of-ndis-versions.md)

[Specifying NDIS Version Information](specifying-ndis-version-information.md)

 

