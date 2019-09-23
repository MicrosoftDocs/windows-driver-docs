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


After calling [**FltRegisterFilter**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltregisterfilter), a minifilter driver's [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize) routine typically calls [**FltStartFiltering**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltstartfiltering) to begin filtering I/O operations.

Every minifilter driver must call [**FltStartFiltering**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltstartfiltering) from its [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize) routine to notify the filter manager that the minifilter driver is ready to begin attaching to volumes and filtering I/O requests. After the minifilter driver calls **FltStartFiltering**, the filter manager treats the minifilter driver as a fully active minifilter driver, presenting it with I/O requests and notifications of volumes to attach to. The minifilter driver must be prepared to begin receiving these I/O requests and notifications even before **FltStartFiltering** returns.

In the MiniSpy sample driver, [**FltStartFiltering**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltstartfiltering) is called as shown in the following code example:

```cpp
status = FltStartFiltering( MiniSpyData.FilterHandle );
if( !NT_SUCCESS( status )) {
  FltUnregisterFilter( MiniSpyData.FilterHandle );
}
```

If the call to [**FltStartFiltering**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltstartfiltering) does not return STATUS\_SUCCESS, the minifilter driver must call [**FltUnregisterFilter**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltunregisterfilter) to unregister itself.

 

 




