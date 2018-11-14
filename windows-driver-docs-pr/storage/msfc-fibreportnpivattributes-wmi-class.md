---
title: MSFC\_FibrePortNPIVAttributes WMI Class
description: MSFC\_FibrePortNPIVAttributes WMI Class
ms.assetid: A778E00A-476C-4763-B652-3312B7913F9C
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_FibrePortNPIVAttributes WMI Class


A WMI client uses the MSFC\_FibrePortNPIVAttributes class to retrieve information about virtual ports created for a physical port.

The MSFC\_FibrePortNPIVAttributes class is defined as follows in *Npivwmi.mof*:

```mof
class MSFC_FibrePortNPIVAttributes   
{  
    [WmiDataId(1), Description("The world wide port name of the physical port"):Amended]  
     uint8 WWPN[8];   
  
    [WmiDataId(2), Description("The world wide node name of the physical port"):Amended]  
     uint8 WWNN[8];   
  
    [WmiDataId(3),  
     read,  
     Description("Number of virtual ports on this adapter."):Amended  
    ]uint32 NumberVirtualPorts;  
  
     [WmiDataId(4),  
      read,  
      Description("Array of virtual ports."):Amended,
      WmiSizeIs("NumberVirtualPorts")  
     ]  
     MSFC_VirtualFibrePortAttributes VirtualPorts[];  
};
```

When compiled by the WMI tool suite, this class definition produces the following data structure:

[**MSFC\_FibrePortNPIVAttributes**](https://msdn.microsoft.com/library/windows/hardware/hh127623)

There are no methods associated with this WMI class.

 

 





