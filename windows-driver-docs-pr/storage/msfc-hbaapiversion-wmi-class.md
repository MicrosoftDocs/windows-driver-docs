---
title: MSFC_HbaApiVersion WMI Class
description: MSFC_HbaApiVersion WMI Class
ms.date: 07/13/2022
---

# MSFC_HbaApiVersion WMI Class

An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the **MSFC_HbaApiVersion** class to report the HBA API version that is currently supported.

The **MSFC_HbaApiVersion** class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_HbaApiVersion
{
    uint32 WmiHbaApiVersion;
    uint32 HbaApiVersion;
    string Description;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure. There are no methods associated with this WMI class.

``` cpp
typedef struct _MSFC_HbaApiVersion {
  uint32 WmiHbaApiVersion;
  uint32 HbaApiVersion;
  string Description;
} MSFC_HbaApiVersion, *PMSFC_HbaApiVersion;
```

| Member | Meaning |
| ------ | ------- |
| **WmiHbaApiVersion** | The version information that the WMI provider supports. |
| **HbaApiVersion**    | The version that the miniport driver supports. |
| **Description**      | The description of the HBA. |
