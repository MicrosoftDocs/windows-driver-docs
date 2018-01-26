---
title: MSFC\_FibrePortHBAAttributes WMI Class
description: MSFC\_FibrePortHBAAttributes WMI Class
ms.assetid: 028afadf-1a2d-4792-8b6c-d53359af64c1
---

# MSFC\_FibrePortHBAAttributes WMI Class


## <span id="ddk_msfc_fibreporthbaattributes_wmi_class_kr"></span><span id="DDK_MSFC_FIBREPORTHBAATTRIBUTES_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the FCbre channel HBA API uses the MSFC\_FibrePortHBAAttributes WMI class to expose attribute information associated with a Fibre Channel port. There should be one instance of this class for each port.

The MSFC\_FibrePortHBAAttributes class is defined as follows in *Hbaapi.mof*:

```
class MSFC_FibrePortHBAAttributes {
  [key] 
  string InstanceName;
  boolean Active;
  [Description ("Unique identifier for the port. "
    "This identifier must be unique among all "
    "ports on all adapters. The same value for "
    "in other classes that expose port information"
    "the identifier must be used for the same port") : amended,
    WmiRefClass("MSFC_FibrePort"),
    WmiRefProperty("UniquePortId"),
    WmiDataId(1)
    ] uint64 UniquePortId;
  [HBA_STATUS_QUALIFIERS, WmiDataId(2)] HBA_STATUS  HBAStatus;
  [HBAType("HBA_PORTATTRIBUTES"),WmiDataId(3)]
    MSFC_HBAPortAttributesResults Attributes;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_FibrePortHBAAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff562499)

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSFC_FibrePortHBAAttributes%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




