---
title: MSFC_NPIVLUNMappingInformationEx WMI Class (Windows Drivers)
description: Learn more about the MSFC_NPIVLUNMappingInformationEx WMI Class.
ms.date: 10/14/2022
---

# MSFC\_NPIVLUNMappingInformationEx WMI Class

A WMI client uses the **MSFC\_NPIVLUNMappingInformationEx** class to retrieve LUN to virtual port mapping information. This class includes the port number associated with the LUN.

The **MSFC\_NPIVLUNMappingInformationEx** class is defined as follows in *Npivwmi.mof*:

```mof
    class MSFC_NPIVLUNMappingInformationEx
    {
        [WmiDataId(1), Description("The world wide port name of the virtual port"):Amended]
        uint8 WWPNVirtualPort[8];
    
        [WmiDataId(2), Description("The world wide port name of the physical port"):Amended]
        uint8 WWPNPhysicalPort[8];
    
        [WmiDataId(3),
         Description("The SCSI Port ID associated with this LUN, matching the SCSI_ADDRESS"):Amended,
         read
        ]
        uint8 PortNumber;
    
        [WmiDataId(4),
         Description("The SCSI Path ID associated with this LUN, matching the SCSI_ADDRESS"):Amended,
         read
        ] uint8 OSBus;
    
        [WmiDataId(5),
         Description("The SCSI Target ID associated with this LUN, matching the SCSI_ADDRESS"):Amended,
         read
        ] uint8 OSTarget;
    
        [WmiDataId(6),
         Description("The SCSI LUN, matching the SCSI_ADDRESS"):Amended,
         read
        ] uint8 OSLUN;
    };
```

When compiled by the WMI tool suite, this class definition produces the following data structure:

**MSFC\_NPIVLUNMappingInformationEx**

There are no methods associated with this WMI class.
