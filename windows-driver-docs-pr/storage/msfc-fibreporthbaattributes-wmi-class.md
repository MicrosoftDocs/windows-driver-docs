---
title: MSFC\_FibrePortHBAAttributes WMI Class
description: MSFC\_FibrePortHBAAttributes WMI Class
ms.assetid: 028afadf-1a2d-4792-8b6c-d53359af64c1
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_FibrePortHBAAttributes WMI Class


## <span id="ddk_msfc_fibreporthbaattributes_wmi_class_kr"></span><span id="DDK_MSFC_FIBREPORTHBAATTRIBUTES_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the FCbre channel HBA API uses the MSFC\_FibrePortHBAAttributes WMI class to expose attribute information associated with a Fibre Channel port. There should be one instance of this class for each port.

The MSFC\_FibrePortHBAAttributes class is defined as follows in *Hbaapi.mof*:

```cpp
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

 

 





