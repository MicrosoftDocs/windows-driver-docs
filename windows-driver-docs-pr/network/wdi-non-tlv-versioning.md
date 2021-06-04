---
title: WDI non-TLV versioning
description: This section describes WDI non-TLV versioning
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI non-TLV versioning


Data structures that are passed between WDI and the IHV miniport and contain a [**NDIS\_OBJECT\_HEADER**](/windows-hardware/drivers/ddi/objectheader/ns-objectheader-ndis_object_header) (such as [**NDIS\_MINIPORT\_DRIVER\_WDI\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_miniport_driver_wdi_characteristics)) follow the standard NDIS versioning model. The miniport must check the **Revision** and **Size** fields to ensure the fields it cares about are present, and ignore any extra fields or data without error. Ensure that newer revisions or larger sizes of such structures are not excluded.

All data structures without an [**NDIS\_OBJECT\_HEADER**](/windows-hardware/drivers/ddi/objectheader/ns-objectheader-ndis_object_header) (such as [**WDI\_FRAME\_METADATA**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_frame_metadata)) follow the TLV versioning model, where WDI and the miniport use the size/revision determined by the lowest **WdiVersion** value from [**NDIS\_WDI\_INIT\_PARAMETERS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_wdi_init_parameters) and [**NDIS\_MINIPORT\_DRIVER\_WDI\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_miniport_driver_wdi_characteristics).

For example, if WDI sets **WdiVersion** in [**NDIS\_WDI\_INIT\_PARAMETERS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_wdi_init_parameters) to **WDI\_VERSION\_1\_0**, and the miniport sets **WdiVersion** in [**NDIS\_MINIPORT\_DRIVER\_WDI\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_miniport_driver_wdi_characteristics) to **WDI\_VERSION\_2\_0**, then both WDI and the miniport should use the structure sizes and definitions compatible with **WDI\_VERSION\_1\_0** for all structures without [**NDIS\_OBJECT\_HEADER**](/windows-hardware/drivers/ddi/objectheader/ns-objectheader-ndis_object_header) fields. However, in the same situation but with structures that have an **NDIS\_OBJECT\_HEADER** field, WDI and the miniport may use a larger or newer structure as long as the **Revision** and **Size** fields are correctly set.

 

