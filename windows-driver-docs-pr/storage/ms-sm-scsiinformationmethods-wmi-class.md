---
title: MS\_SM\_ScsiInformationMethods WMI Class
description: MS\_SM\_ScsiInformationMethods WMI Class
ms.assetid: 13e70e48-5364-4a63-8a83-d5ac02c8d17f
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MS\_SM\_ScsiInformationMethods WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SM\_ScsiInformationMethods WMI class to send SCSI commands. This WMI class has no data blocks. Therefore, the WMI tool suite generates structures that hold parameter data for the methods that belong to the class, but it does not generate a structure that corresponds to the class itself.

The MOF syntax for each method that belongs to this class is described in the reference page for the method. The following topics describe these methods and their accompanying structures:

[**SM\_ScsiInquiry**](sm-scsiinquiry.md)

[**SM\_ScsiReportLuns**](sm-scsireportluns.md)

[**SM\_ScsiReadCapacity**](sm-scsireadcapacity.md)

The MS\_SM\_ScsiInformationMethods class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SM_ScsiInformationMethods
{
    [key]
    string  InstanceName;
    boolean Active;

    [Implemented, WmiMethodId(1)]
    void SM_ScsiInquiry(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DiscoveredPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [in, HBAType("HBA_SCSILUN")]
                 uint64 SmhbaLUN,
                [in ]
                 uint8  Cdb[6],
                [in ]
                 uint32 InRespBufferMaxSize,
                [in ]
                 uint32 InSenseBufferMaxSize,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out]
                 uint8  ScsiStatus,
                [out]
                 uint32 OutRespBufferSize,
                [out]
                 uint32 OutSenseBufferSize,
                [out, WmiSizeIs("OutRespBufferSize") ]
                 uint8 RespBuffer[],
                [out, WmiSizeIs("OutSenseBufferSize") ]
                 uint8 SenseBuffer[]
                );

    [Implemented, WmiMethodId(2)]
    void SM_ScsiReportLuns(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DiscoveredPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [in ]
                 uint8  Cdb[12],
                [in ]
                 uint32 InRespBufferMaxSize,
                [in ]
                 uint32 InSenseBufferMaxSize,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out]
                 uint8  ScsiStatus,
                [out]
                 uint32 TotalRespBufferSize,
                [out]
                 uint32 OutRespBufferSize,
                [out]
                 uint32 OutSenseBufferSize,
                [out, WmiSizeIs("OutRespBufferSize") ]
                 uint8 RespBuffer[],
                [out, WmiSizeIs("OutSenseBufferSize") ]
                 uint8 SenseBuffer[]
                );
 
    [Implemented, WmiMethodId(3)]
    void SM_ScsiReadCapacity(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DiscoveredPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [in, HBAType("HBA_SCSILUN")]
                 uint64 SmhbaLUN,
                [in ]
                 uint8  Cdb[16],
                [in ]
                 uint32 InRespBufferMaxSize,
                [in ]
                 uint32 InSenseBufferMaxSize,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out]
                 uint8  ScsiStatus,
                [out]
                 uint32 OutRespBufferSize,
                [out]
                 uint32 OutSenseBufferSize,
                [out, WmiSizeIs("OutRespBufferSize") ]
                 uint8  RespBuffer[],
                [out, WmiSizeIs("OutSenseBufferSize") ]
                 uint8  SenseBuffer[]
                );
};
```

 

 





