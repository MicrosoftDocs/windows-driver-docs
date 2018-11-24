---
title: HBAFCPBindingEntry2 WMI Class
description: HBAFCPBindingEntry2 WMI Class
ms.assetid: b9423b59-1d55-4487-bebb-e3eb786fc1be
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# HBAFCPBindingEntry2 WMI Class


## <span id="ddk_hbafcpbindingentry2_wmi_class_kr"></span><span id="DDK_HBAFCPBINDINGENTRY2_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the HBAFCPBindingEntry2 class to define a binding between the information that the operating system uses to identify a logical unit on a SCSI device and the Fibre Channel protocol (FCP) identifier for the logical unit. For an explanation of the FCP, see the T11 committee's *dpANS Fibre Channel Protocol for SCSI* specification. For an explanation of this binding between SCSI and FCP identifiers, see the T11 committee's *Fibre Channel HBA API* specification.

The HBAFCPBindingEntry2 class is defined as follows in *Hbaapi.mof*:

```cpp
class HBAFCPBindingEntry2 {
  [WmiDataId(1), HBA_BIND_TYPE_QUALIFIERS] HBA_BIND_TYPE  Type;
  [HBAType("HBA_FCPSCSIENTRY"), WmiDataId(4)] HBAScsiID  ScsiId;
  [HBAType("HBA_FCID"), WmiDataId(2)] HBAFCPID  FCPId;
  [HBAType("HBA_LUID"), WmiDataId(3)] uint8  Luid[256];
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**HBAFCPBindingEntry2**](https://msdn.microsoft.com/library/windows/hardware/ff556035)

There are no methods associated with this WMI class.

 

 





