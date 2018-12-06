---
title: MS\_SMHBA\_FC\_Port WMI Class
description: MS\_SMHBA\_FC\_Port WMI Class
ms.assetid: 671f14e4-c591-4df2-85a1-2db3f802ef5e
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MS\_SMHBA\_FC\_Port WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_FC\_Port class to expose the port attributes of the associated FC adapter. There should be one instance of this class for each port.

The MS\_SMHBA\_FC\_Port class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SMHBA_FC_Port 
{
    [HBAType("HBA_WWN"), WmiDataId(1)]
    uint8   NodeWWN[8];

    [HBAType("HBA_WWN"), WmiDataId(2)]
    uint8   PortWWN[8];

    [WmiDataId(3)]
    uint32  FcId;

    [HBAType("HBA_COS"), WmiDataId(4)]
    uint32  PortSupportedClassofService;

    [HBAType("HBA_FC4TYPES"), WmiDataId(5)]
    uint8   PortSupportedFc4Types[32];

    [HBAType("HBA_FC4TYPES"), WmiDataId(6)]
    uint8   PortActiveFc4Types[32];

    [HBAType("HBA_WWN"), WmiDataId(7)]
    uint8   FabricName[8];

    [WmiDataId(8)]
    uint32  NumberofDiscoveredPorts;

    [WmiDataId(9)] 
    uint8   NumberofPhys;

    [MaxLen(256), WmiDataId(10)]
    string  PortSymbolicName;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SMHBA\_FC\_Port**](https://msdn.microsoft.com/library/windows/hardware/ff563162)

There are no methods associated with this WMI class.

 

 





