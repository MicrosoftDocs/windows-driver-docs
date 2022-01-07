---
title: MS\_SM\_HbaApiVersion WMI Class
description: MS\_SM\_HbaApiVersion WMI Class
ms.date: 10/17/2018
---

# MS\_SM\_HbaApiVersion WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SM\_HbaApiVersion class to report the current HBA API version.

The MS\_SM\_HbaApiVersion class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SM_HbaApiVersion
{
    uint32 WmiHbaApiVersion;  
    uint32 HbaApiVersion;  
    string Description;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SM\_HbaApiVersion**](/previous-versions/windows/hardware/drivers/ff563211(v=vs.85))

There are no methods associated with this WMI class.

 

