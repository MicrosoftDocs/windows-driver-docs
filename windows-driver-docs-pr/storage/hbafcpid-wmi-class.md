---
title: HBAFCPID WMI Class
description: HBAFCPID WMI Class
ms.assetid: 6b0d0f79-a7a8-4341-955b-2c3068936a1d
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# HBAFCPID WMI Class


## <span id="ddk_hbafcpid_wmi_class_kr"></span><span id="DDK_HBAFCPID_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the HBAFCPID class to define a Fibre Channel protocol (FCP) identifier for a logical unit. The FCP identifier specifies the name of the machine the logical unit is located on and the HBA port through which it can be accessed.

The miniport driver uses this identifier to construct a binding between the information that the operating system uses to identify a logical unit and the FCP identifier for the logical unit. For information about this kind of binding, see [**HBAFCPBindingEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556034). For an explanation of the Fibre Channel protocol, see the T11 committee's *dpANS Fibre Channel Protocol for SCSI* specification.

The HBAFCPID class is defined as follows in *Hbaapi.mof*:

```cpp
class HBAFCPID {
  [WmiDataId(1)] uint32  Fcid;
  [HBAType("HBA_WWN"), WmiDataId(2)] uint8  NodeWWN[8];
  [HBAType("HBA_WWN"), WmiDataId(3)] uint8  PortWWN[8];
  [WmiDataId(4)] uint64  FcpLun;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**HBAFCPID**](https://msdn.microsoft.com/library/windows/hardware/ff556038)

There are no methods associated with this WMI class.

 

 





