---
title: Initiating Filtering
description: Initiating Filtering
ms.assetid: 79ae93bc-0a6d-412a-80ca-ec4f907fb814
keywords:
- filtering I/O operations WDK file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initiating Filtering


## <span id="ddk_initiating_filtering_if"></span><span id="DDK_INITIATING_FILTERING_IF"></span>


After calling [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305), a minifilter driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine typically calls [**FltStartFiltering**](https://msdn.microsoft.com/library/windows/hardware/ff544569) to begin filtering I/O operations.

Every minifilter driver must call [**FltStartFiltering**](https://msdn.microsoft.com/library/windows/hardware/ff544569) from its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine to notify the filter manager that the minifilter driver is ready to begin attaching to volumes and filtering I/O requests. After the minifilter driver calls **FltStartFiltering**, the filter manager treats the minifilter driver as a fully active minifilter driver, presenting it with I/O requests and notifications of volumes to attach to. The minifilter driver must be prepared to begin receiving these I/O requests and notifications even before **FltStartFiltering** returns.

In the MiniSpy sample driver, [**FltStartFiltering**](https://msdn.microsoft.com/library/windows/hardware/ff544569) is called as shown in the following code example:

```cpp
status = FltStartFiltering( MiniSpyData.FilterHandle );
if( !NT_SUCCESS( status )) {
  FltUnregisterFilter( MiniSpyData.FilterHandle );
}
```

If the call to [**FltStartFiltering**](https://msdn.microsoft.com/library/windows/hardware/ff544569) does not return STATUS\_SUCCESS, the minifilter driver must call [**FltUnregisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544606) to unregister itself.

 

 




