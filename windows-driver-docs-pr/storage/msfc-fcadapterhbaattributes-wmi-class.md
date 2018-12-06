---
title: MSFC\_FCAdapterHBAAttributes WMI Class
description: MSFC\_FCAdapterHBAAttributes WMI Class
ms.assetid: fa0ff9c2-e7cc-4000-bd18-ade953e57dcc
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_FCAdapterHBAAttributes WMI Class


## <span id="ddk_msfc_fcadapterhbaattributes_wmi_class_kr"></span><span id="DDK_MSFC_FCADAPTERHBAATTRIBUTES_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the MSFC\_FCAdapterHBAAttributes WMI class to expose attribute information associated with a Fibre Channel adapter.

The MSFC\_FCAdapterHBAAttributes class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_FCAdapterHBAAttributes {
  [key] 
  string InstanceName;
  boolean Active;
  [Description ("Unique identifier for the adapter. This"
                "identifier must be unique among all"
                "adapters. The same value for the "
                "identifier must be used for the same"
                "adapter in other classes that expose"
                "adapter information") : amended,
   WmiRefClass("MSFC_FibreChannelAdapter"),
   WmiRefProperty("UniqueAdapterId"),
   WmiDataId(1)] uint64  UniqueAdapterId;
  [HBA_STATUS_QUALIFIERS, WmiDataId(2)] HBA_STATUS HBAStatus;
  [HBAType("HBA_WWN"),WmiDataId(3)] uint8  NodeWWN[8];
  [WmiDataId(4)] uint32  VendorSpecificID;
  [WmiDataId(5)] uint32 NumberOfPorts;
  [WmiDataId(6)] string  Manufacturer;
  [MaxLen(64), WmiDataId(7)] string SerialNumber; 
  [MaxLen(256), WmiDataId(8)] string Model; 
  [MaxLen(256), WmiDataId(9)] string ModelDescription; 
  [MaxLen(256), WmiDataId(10)] string NodeSymbolicName; 
  [MaxLen(256), WmiDataId(11)] string HardwareVersion; 
  [MaxLen(256), WmiDataId(12)] string DriverVersion; 
  [MaxLen(256), WmiDataId(13)] string OptionROMVersion; 
  [MaxLen(256), WmiDataId(14)] string FirmwareVersion; 
  [MaxLen(256), WmiDataId(15)] string DriverName; 
  [MaxLen(256), WmiDataId(16)] string MfgDomain;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_FCAdapterHBAAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff562495)

There are no methods associated with this WMI class.

 

 





