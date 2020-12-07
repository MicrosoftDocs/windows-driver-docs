---
title: HBAScsiID WMI Class
description: HBAScsiID WMI Class
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# HBAScsiID WMI Class


## <span id="ddk_hbascsiid_wmi_class_kr"></span><span id="DDK_HBASCSIID_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the HBAScsiID class to identify a logical unit by means of the device's name in the operating system and its SCSI information.

The HBAScsiID class is defined as follows in Hbaapi.mof:

```cpp
class HBAScsiID { 
  [WmiDataId(1)] uint32  ScsiBusNumber;
  [WmiDataId(2)] uint32  ScsiTargetNumber;
  [WmiDataId(3)] uint32  ScsiOSLun;
  [WmiDataId(4),MAX(257)] uint16  OSDeviceName[];
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**HBAScsiID**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_hbascsiid)

There are no methods associated with this WMI class.

 

