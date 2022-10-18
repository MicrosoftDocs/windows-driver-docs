---
title: MSFC_NPIVCapabilities WMI Class (Windows Drivers)
description: Learn more about the MSFC_NPIVCapabilities WMI Class.
ms.date: 10/14/2022
---

# MSFC\_NPIVCapabilities WMI Class

The **MSFC\_NPIVCapabilities** class indicates that DH-CHAP authentication capability is available for virtual or physical ports.

The **MSFC\_NPIVCapabilities** class is defined as follows in *Npivwmi.mof*:

```mof
    class MSFC_NPIVCapabilities
    {
        [key, read] 
        string InstanceName;
    
        [read]
        boolean Active;
    
        [WmiDataId(1), Description("DH-CHAP available for physical port"):Amended]
        boolean DhChapAvailableOnPhysicalPort;
    
        [WmiDataId(2), Description("DH-CHAP available for virtual ports"):Amended]
        boolean DhChapAvailableOnVirtualPorts;
    
        [WmiDataId(3), Description("Number of virtual ports that can be created on this physical FC port"):Amended]
        uint16 MaxVirtualPortCount;
    };
```

When compiled by the WMI tool suite, this class definition produces the following data structure:

**MSFC\_NPIVCapabilities**

There are no methods associated with this WMI class.
