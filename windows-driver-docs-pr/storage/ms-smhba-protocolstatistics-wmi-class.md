---
title: MS_SMHBA_PROTOCOLSTATISTICS WMI Class
description: MS\_SMHBA\_PROTOCOLSTATISTICS WMI Class
ms.date: 10/17/2018
---

# MS\_SMHBA\_PROTOCOLSTATISTICS WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_PROTOCOLSTATISTICS class to expose the traffic statistics.

The MS\_SMHBA\_PROTOCOLSTATISTICS class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SMHBA_PROTOCOLSTATISTICS
{
    [WmiDataId(1)]
    sint64 SecondsSinceLastReset;

    [WmiDataId(2)]
    sint64 InputRequests;

    [WmiDataId(3)]
    sint64 OutputRequests;

    [WmiDataId(4)]
    sint64 ControlRequests;

    [WmiDataId(5)]
    sint64 InputMegabytes;

    [WmiDataId(6)]
    sint64 OutputMegabytes;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SMHBA\_PROTOCOLSTATISTICS**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_ms_smhba_protocolstatistics)

There are no methods associated with this WMI class.

 

