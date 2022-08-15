---
title: MS\_SM\_HbaApiVersion WMI Class
description: MS\_SM\_HbaApiVersion WMI Class
ms.date: 07/13/2022
---

# MS_SM_HbaApiVersion WMI Class

An HBA miniport driver that supports the Storage Management API uses the **MS_SM_HbaApiVersion** class to report the current HBA API version.

The **MS_SM_HbaApiVersion** class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SM_HbaApiVersion
{
    uint32 WmiHbaApiVersion;  
    uint32 HbaApiVersion;  
    string Description;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure. There are no methods associated with this WMI class.

``` cpp
typedef struct _MS_SM_HbaApiVersion {
  uint32 WmiHbaApiVersion;
  uint32 HbaApiVersion;
  string Description;
} MS_SM_HbaApiVersion, *PMS_SM_HbaApiVersion;
```

| Member | Meaning |
| ------ | ------- |
| **WmiHbaApiVersion** | The version information that the WMI provider supports. |
| **HbaApiVersion**    | The version that the miniport driver supports. |
| **Description**      | The description of the HBA. |
