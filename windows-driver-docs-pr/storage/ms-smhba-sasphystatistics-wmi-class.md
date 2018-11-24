---
title: MS\_SMHBA\_SASPHYSTATISTICS WMI Class
description: MS\_SMHBA\_SASPHYSTATISTICS WMI Class
ms.assetid: 72afc856-8232-492f-b8d2-4e88dd9fe723
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MS\_SMHBA\_SASPHYSTATISTICS WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_SASPHYSTATISTICS class to expose statistics that are associated with an adapter port. There should be one instance of this class for each port.

The MS\_SMHBA\_SASPHYSTATISTICS class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SMHBA_SASPHYSTATISTICS
{
    [WmiDataId(1)]
    sint64 SecondsSinceLastReset;

    [WmiDataId(2)]
    sint64 TxFrames;

    [WmiDataId(3)]
    sint64 TxWords;

    [WmiDataId(4)]
    sint64 RxFrames;

    [WmiDataId(5)]
    sint64 RxWords;

    [WmiDataId(6)]
    sint64 InvalidDwordCount;

    [WmiDataId(7)]
    sint64 RunningDisparityErrorCount;

    [WmiDataId(8)]
    sint64 LossofDwordSyncCount;

    [WmiDataId(9)]
    sint64 PhyResetProblemCount;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SMHBA\_SASPHYSTATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff563175)

There are no methods associated with this WMI class.

 

 





