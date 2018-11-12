---
title: WDI non-TLV versioning
description: This section describes WDI non-TLV versioning
ms.assetid: 19B5BEE1-BE17-40E3-99FA-D9BF4492D020
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI non-TLV versioning


Data structures that are passed between WDI and the IHV miniport and contain a [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) (such as [**NDIS\_MINIPORT\_DRIVER\_WDI\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/mt297617)) follow the standard NDIS versioning model. The miniport must check the **Revision** and **Size** fields to ensure the fields it cares about are present, and ignore any extra fields or data without error. Ensure that newer revisions or larger sizes of such structures are not excluded.

All data structures without an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) (such as [**WDI\_FRAME\_METADATA**](https://msdn.microsoft.com/library/windows/hardware/dn897827)) follow the TLV versioning model, where WDI and the miniport use the size/revision determined by the lowest **WdiVersion** value from [**NDIS\_WDI\_INIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/mt297621) and [**NDIS\_MINIPORT\_DRIVER\_WDI\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/mt297617).

For example, if WDI sets **WdiVersion** in [**NDIS\_WDI\_INIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/mt297621) to **WDI\_VERSION\_1\_0**, and the miniport sets **WdiVersion** in [**NDIS\_MINIPORT\_DRIVER\_WDI\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/mt297617) to **WDI\_VERSION\_2\_0**, then both WDI and the miniport should use the structure sizes and definitions compatible with **WDI\_VERSION\_1\_0** for all structures without [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) fields. However, in the same situation but with structures that have an **NDIS\_OBJECT\_HEADER** field, WDI and the miniport may use a larger or newer structure as long as the **Revision** and **Size** fields are correctly set.

 

 





