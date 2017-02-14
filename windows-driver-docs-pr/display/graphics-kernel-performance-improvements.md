---
title: Graphics kernel performance improvements
description: To help evaluate graphics hardware performance, Windows Display Driver Model (WDDM) 1.3 and later drivers can optionally provide accurate timing information for API calls that are processed by the GPU. This capability is new starting with Windows 8.1.
ms.assetid: 8A2E1392-F0B4-4F5F-AFD9-DE8C6F3C2147
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Graphics%20kernel%20performance%20improvements%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




