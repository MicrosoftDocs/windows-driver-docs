---
title: MSFC\_NPIVLUNMappingInformation WMI Class
description: MSFC\_NPIVLUNMappingInformation WMI Class
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_NPIVLUNMappingInformation WMI Class


A WMI client uses the MSFC\_LUNMappingInformation class to retrieve LUN to virtual port mapping information.

The MSFC\_NPIVLUNMappingInformation class is defined as follows in *Npivwmi.mof*:

```mof
class MSFC_NPIVLUNMappingInformation  
{  
    [WmiDataId(1), Description("The world wide port name of the virtual port"):Amended]  
     uint8 WWPNVirtualPort[8];  
  
    [WmiDataId(2), Description("The world wide port name of the physical port"):Amended]  
    uint8 WWPNPhysicalPort[8];  
  
    [WmiDataId(3),  
    read  
    ] uint8 OSBus;  
  
    [WmiDataId(4),  
    read  
    ] uint8 OSTarget;  
  
    [WmiDataId(5),  
    read  
    ] uint8 OSLUN;  
};  
```

When compiled by the WMI tool suite, this class definition produces the following data structure:

[**MSFC\_NPIVLUNMappingInformation**](/windows-hardware/drivers/ddi/npivwmi/ns-npivwmi-_msfc_npivlunmappinginformation)

There are no methods associated with this WMI class.

 

