---
title: MS\_SMHBA\_PORTATTRIBUTES WMI Class
description: MS\_SMHBA\_PORTATTRIBUTES WMI Class
ms.date: 10/17/2018
---

# MS\_SMHBA\_PORTATTRIBUTES WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_PORTATTRIBUTES class to expose the port attributes. There should be one instance of this class for each port.

The MS\_SMHBA\_PORTATTRIBUTES class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SMHBA_PORTATTRIBUTES 
{
    [HBA_PORTTYPE_QUALIFIERS, WmiDataId(1)]
    uint32 PortType;

    [HBA_PORTSTATE_QUALIFIERS, WmiDataId(2)]
    uint32 PortState;

    [WmiDataId(3),
     Description("Size of MS_SMHBA_SAS_Port or MS_SMHBA_FC_Port")
    ]
    uint32 PortSpecificAttributesSize;

    [MaxLen(256), WmiDataId(4)]
    string OSDeviceName;

    [WmiDataId(5)]
    uint64 Reserved;

    [WmiDataId(6),
     Description(" MS_SMHBA_SAS_Port or MS_SMHBA_FC_Port Buffer"),
     WmiSizeIs("PortSpecificAttributesSize")
    ]
    uint8 PortSpecificAttributes[];
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SMHBA\_PORTATTRIBUTES**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_ms_smhba_portattributes)

There are no methods associated with this WMI class.

 

