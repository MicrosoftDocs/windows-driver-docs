---
title: MSFC\_FC4STATISTICS WMI Class
description: MSFC\_FC4STATISTICS WMI Class
ms.assetid: 49cd4104-1fe8-46ec-9216-c5c078666c02
---

# MSFC\_FC4STATISTICS WMI Class


## <span id="ddk_msfc_fc4statistics_wmi_class_kr"></span><span id="DDK_MSFC_FC4STATISTICS_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the MSFC\_FC4STATISTICS WMI class to report traffic statistics on a port of type Nx\_Port for the indicated FC-4 protocol in response to a call to the [**GetFC4Statistics**](getfc4statistics.md) WMI method.

The MSFC\_FC4STATISTICS class is defined as follows in *Hbaapi.mof*:

```
class MSFC_FC4STATISTICS {
  [WmiDataId(1)] uint64  InputRequests;
  [WmiDataId(2)] uint64  OutputRequests;
  [WmiDataId(3)] uint64  ControlRequests;
  [WmiDataId(4)] uint64  InputMegabytes;
  [WmiDataId(5)] uint64  OutputMegabytes;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_FC4STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff562492)

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSFC_FC4STATISTICS%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




