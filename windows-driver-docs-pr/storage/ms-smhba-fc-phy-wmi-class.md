---
title: MS\_SMHBA\_FC\_PHY WMI Class
description: MS\_SMHBA\_FC\_PHY WMI Class
ms.date: 10/17/2018
---

# MS\_SMHBA\_FC\_PHY WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_FC\_PHY class to expose the physical attributes of the associated FC port. There should be one instance of this class for each port.

The MS\_SMHBA\_FC\_PHY class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SMHBA_FC_PHY 
{
    [WmiDataId(1), HBAType("HBA_FCPHYSPEED")]
    uint32  PhySupportSpeed;

    [WmiDataId(2), HBAType("HBA_FCPHYSPEED")]
    uint32  PhySpeed;      

    [WmiDataId(3), HBAType("HBA_FCPHYTYPE")]
    uint8   PhyType;

    [WmiDataId(4)]
    uint32  MaxFrameSize; 
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SMHBA\_FC\_PHY**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_ms_smhba_fc_phy)

There are no methods associated with this WMI class.

 

