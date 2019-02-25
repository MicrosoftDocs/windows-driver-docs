---
title: Graphics kernel performance improvements
description: To help evaluate graphics hardware performance, Windows Display Driver Model (WDDM) 1.3 and later drivers can optionally provide accurate timing information for API calls that are processed by the GPU. This capability is new starting with Windows 8.1.
ms.assetid: 8A2E1392-F0B4-4F5F-AFD9-DE8C6F3C2147
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Graphics kernel performance improvements


To help evaluate graphics hardware performance, Windows Display Driver Model (WDDM) 1.3 and later drivers can optionally provide accurate timing information for API calls that are processed by the GPU. This capability is new starting with Windows 8.1.

## <span id="Kernel_performance_reference"></span><span id="kernel_performance_reference"></span><span id="KERNEL_PERFORMANCE_REFERENCE"></span>Kernel performance reference


These reference topics describe how to implement this capability in your display miniport driver and user-mode display driver:

-   [*DxgkDdiCalibrateGpuClock*](https://msdn.microsoft.com/library/windows/hardware/dn467321)
-   [*DxgkDdiFormatHistoryBuffer*](https://msdn.microsoft.com/library/windows/hardware/dn439360)
-   [**DXGK\_HISTORY\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/dn439361)
-   [**DXGK\_HISTORY\_BUFFER\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn439362)
-   [**DXGKARG\_CALIBRATEGPUCLOCK**](https://msdn.microsoft.com/library/windows/hardware/dn467320)
-   [**DXGKARG\_FORMATHISTORYBUFFER**](https://msdn.microsoft.com/library/windows/hardware/dn439358)
-   [**DXGKARG\_HISTORYBUFFERPRECISION**](https://msdn.microsoft.com/library/windows/hardware/dn439359)
-   [**DRIVER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff556169) (new **DxgkDdiCalibrateGpuClock** and **DxgkDdiFormatHistoryBuffer** members)
-   [**DXGK\_ALLOCATIONINFOFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff560966) (new **HistoryBuffer** member)
-   [**DXGK\_QUERYADAPTERINFOTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff562010) (new **DXGKQAITYPE\_HISTORYBUFFERPRECISION** constant value)
-   [*DxgkDdiCreateAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559606) (see "Allocating history buffers" in Remarks)

 

 





