---
title: MSFC\_FibrePortHBAStatistics WMI Class
description: MSFC\_FibrePortHBAStatistics WMI Class
ms.assetid: 24c787b6-b9f7-4c9b-8d1d-6b2796f65622
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_FibrePortHBAStatistics WMI Class


## <span id="ddk_msfc_fibreporthbastatistics_wmi_class_kr"></span><span id="DDK_MSFC_FIBREPORTHBASTATISTICS_WMI_CLASS_KR"></span>


A WMI client uses the MSFC\_FibrePortHBAStatistics class to query an HBA miniport driver for statistics related to a port on an HBA. The MSFC\_FibrePortHBAStatistics class reports all of the information in the [MSFC\_HBAPortStatistics WMI Class](msfc-hbaportstatistics-wmi-class.md) plus some identifier information for the port.

The MSFC\_FibrePortHBAStatistics class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_FibrePortHBAStatistics
{
    [key] 
    string InstanceName;
    boolean Active;
    [
     Description ("Unique identifier for the port. "
                   "This identifier must be unique "
                   "among all ports on all adapters."
                   "The same value for the identifier "
                   "must be used for the same port "
                   "in other classes that expose port "
                   "information") : amended,
     WmiRefClass("MSFC_FibrePort"),
     WmiRefProperty("UniquePortId"),
     WmiDataId(1)
    ]
    uint64 UniquePortId;
    [WmiDataId(2),
     HBA_STATUS_QUALIFIERS
    ]
    uint32 HBAStatus;
    // Note 4 byte padding
    [ WmiDataId(3) ]
    MSFC_HBAPortStatistics Statistics;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_FibrePortHBAStatistics**](https://msdn.microsoft.com/library/windows/hardware/ff562503)

There are no methods associated with this WMI class.

 

 





