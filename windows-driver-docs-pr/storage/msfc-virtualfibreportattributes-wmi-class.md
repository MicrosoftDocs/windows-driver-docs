---
title: MSFC\_VirtualFibrePortAttributes WMI Class
description: MSFC\_VirtualFibrePortAttributes WMI Class
ms.assetid: D605D63F-0EBF-44C0-8ADE-729F2DE48487
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_VirtualFibrePortAttributes WMI Class


A WMI client uses the MSFC\_VirtualFibrePortAttributes class to retrieve the properties of a virtual port.

The MSFC\_VirtualFibrePortAttributes class is defined as follows in *Npivwmi.mof*:

```mof
class MSFC_VirtualFibrePortAttributes  
{  
    [WmiDataId(1), Description("Status of the virtual port"):Amended,  
    uint32 Status;  
  
    [WmiDataId(2), Description("FC Id"):Amended]  
    uint32 FCId;  
      
    [WmiDataId(3), Description("Port symbolic name"):Amended]  
    uint16 VirtualName[64];  
  
    [WmiDataId(4), Description("An opaque tag passed in by the app. 128 bit so that a guid can be stored in it."):Amended]  
    uint8 Tag[16];  
  
    [WmiDataId(5), Description("The world wide port name of the virtual port"):Amended]  
    uint8 WWPN[8];   
  
    [WmiDataId(6), Description("The world wide node name of the virtual port"):Amended]  
    uint8 WWNN[8];   
  
    [WmiDataId(7), Description("The world wide node name of fabric"):Amended]  
    uint8 FabricWWN[8];  
};  
```

When compiled by the WMI tool suite, this class definition produces the following data structure:

[**MSFC\_VirtualFibrePortAttributes**](https://msdn.microsoft.com/library/windows/hardware/hh127628)

There are no methods associated with this WMI class.

 

 





