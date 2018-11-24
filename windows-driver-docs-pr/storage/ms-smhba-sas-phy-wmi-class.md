---
title: MS\_SMHBA\_SAS\_PHY WMI Class
description: MS\_SMHBA\_SAS\_PHY WMI Class
ms.assetid: c4fcf9ae-d2ab-4791-bf1e-55087fe03185
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MS\_SMHBA\_SAS\_PHY WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_SAS\_PHY class to expose the physical attributes of the associated SAS port. There should be one instance of this class for each port.

The MS\_SMHBA\_SAS\_PHY class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SMHBA_SAS_PHY
{
    [WmiDataId(1)]
    uint8   PhyIdentifier;

    [WmiDataId(2), HBAType("HBA_SASPHYSPEED")]
    uint32  NegotiatedLinkRate;

    [WmiDataId(3), HBAType("HBA_SASPHYSPEED")]
    uint32  ProgrammedMinLinkRate;

    [WmiDataId(4), HBAType("HBA_SASPHYSPEED")]
    uint32  HardwareMinLinkRate;

    [WmiDataId(5), HBAType("HBA_SASPHYSPEED")]
    uint32  ProgrammedMaxLinkRate;

    [WmiDataId(6), HBAType("HBA_SASPHYSPEED")]
    uint32  HardwareMaxLinkRate;

    [WmiDataId(7), HBAType("HBA_WWN") ]
    uint8   domainPortWWN[8];
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SMHBA\_SAS\_PHY**](https://msdn.microsoft.com/library/windows/hardware/ff563181)

There are no methods associated with this WMI class.

 

 





