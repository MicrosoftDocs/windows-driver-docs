---
title: Initiating Filtering
author: windows-driver-content
description: Initiating Filtering
ms.assetid: 79ae93bc-0a6d-412a-80ca-ec4f907fb814
keywords: ["filtering I/O operations WDK file system minifilter"]
---

# Initiating Filtering


## <span id="ddk_initiating_filtering_if"></span><span id="DDK_INITIATING_FILTERING_IF"></span>


After calling [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305), a minifilter driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine typically calls [**FltStartFiltering**](https://msdn.microsoft.com/library/windows/hardware/ff544569) to begin filtering I/O operations.

Every minifilter driver must call [**FltStartFiltering**](https://msdn.microsoft.com/library/windows/hardware/ff544569) from its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine to notify the filter manager that the minifilter driver is ready to begin attaching to volumes and filtering I/O requests. After the minifilter driver calls **FltStartFiltering**, the filter manager treats the minifilter driver as a fully active minifilter driver, presenting it with I/O requests and notifications of volumes to attach to. The minifilter driver must be prepared to begin receiving these I/O requests and notifications even before **FltStartFiltering** returns.

In the MiniSpy sample driver, [**FltStartFiltering**](https://msdn.microsoft.com/library/windows/hardware/ff544569) is called as shown in the following code example:

```
status = FltStartFiltering( MiniSpyData.FilterHandle );
if( !NT_SUCCESS( status )) {
  FltUnregisterFilter( MiniSpyData.FilterHandle );
}
```

If the call to [**FltStartFiltering**](https://msdn.microsoft.com/library/windows/hardware/ff544569) does not return STATUS\_SUCCESS, the minifilter driver must call [**FltUnregisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544606) to unregister itself.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Initiating%20Filtering%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


