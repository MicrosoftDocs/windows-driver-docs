---
title: MS\_SMHBA\_SAS\_Port WMI Class
description: MS\_SMHBA\_SAS\_Port WMI Class
ms.assetid: d3528212-f884-4db8-aadc-eb4ca15814da
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MS\_SMHBA\_SAS\_Port WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_SAS\_Port class to expose the attributes that are associated with a SAS port. There should be one instance of this class for each port.

The MS\_SMHBA\_SAS\_Port class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SMHBA_SAS_Port 
{
    [HBAType("HBA_SASPORTPROTOCOL"), WmiDataId(1)]
    uint32  PortProtocol;

    [HBAType("HBA_WWN"), WmiDataId(2)]
    uint8   LocalSASAddress[8];

    [HBAType("HBA_WWN"), WmiDataId(3)]
    uint8   AttachedSASAddress[8];

    [WmiDataId(4)]
    uint32  NumberofDiscoveredPorts;

    [WmiDataId(5)]
    uint32  NumberofPhys;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SMHBA\_SAS\_Port**](https://msdn.microsoft.com/library/windows/hardware/ff563186)

There are no methods associated with this WMI class.

 

 





