---
title: MSFC\_TM WMI Class
description: MSFC\_TM WMI Class
ms.assetid: c81b9b2a-6381-4ff9-a579-bee53ac8678d
---

# MSFC\_TM WMI Class


## <span id="ddk_msfc_tm_wmi_class_kr"></span><span id="DDK_MSFC_TM_WMI_CLASS_KR"></span>


A WMI provider uses the MSFC\_TM WMI class to time stamp events.

The MSFC\_TM class is defined as follows in *Hbaapi.mof*:

```
class MSFC_TM {
  [WmiDataId(1)] uint32  tm_sec;
  [WmiDataId(2)] uint32  tm_min;
  [WmiDataId(3)] uint32  tm_hour;
  [WmiDataId(4)] uint32  tm_mday;
  [WmiDataId(5)] uint32  tm_mon;
  [WmiDataId(6)] uint32  tm_year;
  [WmiDataId(7)] uint32  tm_wday;
  [WmiDataId(8)] uint32  tm_yday;
  [WmiDataId(9)] uint32  tm_isdst;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_TM**](https://msdn.microsoft.com/library/windows/hardware/ff562520)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSFC_TM%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




