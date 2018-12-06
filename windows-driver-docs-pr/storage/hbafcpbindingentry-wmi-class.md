---
title: HBAFCPBindingEntry WMI Class
description: HBAFCPBindingEntry WMI Class
ms.assetid: 58993d0d-2044-430d-b8f6-5ea3b68d460b
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# HBAFCPBindingEntry WMI Class


## <span id="ddk_hbafcpbindingentry_wmi_class_kr"></span><span id="DDK_HBAFCPBINDINGENTRY_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the HBAFCPBindingEntry class to define a binding between the information that the operating system uses to identify a SCSI device and the Fibre Channel protocol (FCP) identifier for the device. For an explanation of the Fibre Channel protocol, see the T11 committee's *dpANS Fibre Channel Protocol for SCSI* specification. For an explanation of this binding between operating system data that identifies a logical unit and FCP identifiers, see the T11 committee's *Fibre Channel HBA API* specification.

The HBAFCPBindingEntry class is defined as follows in *Hbaapi.mof*:

```cpp
class HBAFCPBindingEntry {
  [HBAType("HBA_FCPBINDINGTYPE"),
    Values{"TO_D_ID", "TO_WWN", "TO_OTHER"},
    ValueMap{"0", "1", "2"},
    WmiDataId(1)] uint32  Type;
  [HBAType("HBA_FCPSCSIENTRY"), WmiDataId(3)] HBAScsiID  ScsiId;
  [HBAType("HBA_FCID"), WmiDataId(2)] HBAFCPID  FCPId;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**HBAFCPBindingEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556034)

There are no methods associated with this WMI class.

 

 





