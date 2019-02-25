---
title: Using NDIS 6.30 Data Structures
description: Using NDIS 6.30 Data Structures
ms.assetid: 0CAD1CCE-5AF6-4EBD-85C9-040FA0D1C141
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using NDIS 6.30 Data Structures


NDIS can support multiple versions of the same data structure. For the Windows 8 and Windows Server 2012 operating systems, miniport drivers that use an NDIS 6.30 version of a structure must initialize the **Header** member of the structure with the correct version and size values. The **Header** member is an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure, and the driver must initialize the **Revision** member and **Size** member value of the **Header** member to the NDIS 6.30 version and size values.

**Note**  To determine the correct version and size information see the reference pages for each structure that includes a **Header** member. The reference pages for structures that contain a **Header** member and that were updated for NDIS 6.30 include new information for NDIS 6.30 drivers. If there is no update to the structure for NDIS 6.30, the information that is provided for earlier versions of NDIS also applies to NDIS 6.30 drivers.

 

The following structures were updated for NDIS 6.30:

- [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832)
- [**NDIS\_MINIPORT\_ADAPTER\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565920)
- [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)
- [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924)
- [**NDIS\_MINIPORT\_ADAPTER\_NATIVE\_802\_11\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565926)
- [**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566567)
- [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583)
- [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566705)
- [**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706)
- [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748)
- [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759)
- [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864)
- [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff567179)
- [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181)
- [**NDIS\_RECEIVE\_QUEUE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567204)
- [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211)
- [**NDIS\_RECEIVE\_SCALE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff567220)
- [**NDIS\_RSS\_PROCESSOR\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567274)
- [**NDIS\_SHARED\_MEMORY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567303)
 

 





