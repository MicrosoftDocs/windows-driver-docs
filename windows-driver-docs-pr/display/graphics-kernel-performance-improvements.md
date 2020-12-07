---
title: Graphics kernel performance improvements
description: To help evaluate graphics hardware performance, Windows Display Driver Model (WDDM) 1.3 and later drivers can optionally provide accurate timing information for API calls that are processed by the GPU. This capability is new starting with Windows 8.1.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Graphics kernel performance improvements


To help evaluate graphics hardware performance, Windows Display Driver Model (WDDM) 1.3 and later drivers can optionally provide accurate timing information for API calls that are processed by the GPU. This capability is new starting with Windows 8.1.

## <span id="Kernel_performance_reference"></span><span id="kernel_performance_reference"></span><span id="KERNEL_PERFORMANCE_REFERENCE"></span>Kernel performance reference


These reference topics describe how to implement this capability in your display miniport driver and user-mode display driver:

-   [*DxgkDdiCalibrateGpuClock*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_calibrategpuclock)
-   [*DxgkDdiFormatHistoryBuffer*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_formathistorybuffer)
-   [**DXGK\_HISTORY\_BUFFER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_history_buffer)
-   [**DXGK\_HISTORY\_BUFFER\_HEADER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_history_buffer_header)
-   [**DXGKARG\_CALIBRATEGPUCLOCK**](./index.md)
-   [**DXGKARG\_FORMATHISTORYBUFFER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_formathistorybuffer)
-   [**DXGKARG\_HISTORYBUFFERPRECISION**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_historybufferprecision)
-   [**DRIVER\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) (new **DxgkDdiCalibrateGpuClock** and **DxgkDdiFormatHistoryBuffer** members)
-   [**DXGK\_ALLOCATIONINFOFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_allocationinfoflags) (new **HistoryBuffer** member)
-   [**DXGK\_QUERYADAPTERINFOTYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) (new **DXGKQAITYPE\_HISTORYBUFFERPRECISION** constant value)
-   [*DxgkDdiCreateAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) (see "Allocating history buffers" in Remarks)

 

