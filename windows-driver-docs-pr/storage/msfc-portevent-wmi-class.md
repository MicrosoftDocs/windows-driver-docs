---
title: MSFC\_PortEvent WMI Class
description: MSFC\_PortEvent WMI Class
ms.assetid: 38b8e358-b118-4a0c-ac47-2f257d0ed1bf
---

# MSFC\_PortEvent WMI Class


## <span id="ddk_msfc_portevent_wmi_class_kr"></span><span id="DDK_MSFC_PORTEVENT_WMI_CLASS_KR"></span>


A WMI provider uses the MSFC\_PortEvent WMI class to report port events.

The MSFC\_PortEvent class is defined as follows in *Hbaapi.mof*:

```
class MSFC_PortEvent : WMIEvent {
  [key] 
  string InstanceName;
  boolean Active;
  [WmiDataId(1), Description("Type of event") : amended,
    EVENT_TYPES_QUALIFIERS] uint32  EventType;
  [WmiDataId(2), Description("Fabric port id") : amended]
    uint32 FabricPortId;
  [WmiDataId(3), Description("Port WWN") : amended,
    HBAType("HBA_WWN")] uint8  PortWWN[8];
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_PortEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562516)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSFC_PortEvent%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




