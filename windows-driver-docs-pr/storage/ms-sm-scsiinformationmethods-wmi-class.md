---
title: MS\_SM\_ScsiInformationMethods WMI Class
description: MS\_SM\_ScsiInformationMethods WMI Class
ms.assetid: 13e70e48-5364-4a63-8a83-d5ac02c8d17f
---

# MS\_SM\_ScsiInformationMethods WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SM\_ScsiInformationMethods WMI class to send SCSI commands. This WMI class has no data blocks. Therefore, the WMI tool suite generates structures that hold parameter data for the methods that belong to the class, but it does not generate a structure that corresponds to the class itself.

The MOF syntax for each method that belongs to this class is described in the reference page for the method. The following topics describe these methods and their accompanying structures:

[**SM\_ScsiInquiry**](sm-scsiinquiry.md)

[**SM\_ScsiReportLuns**](sm-scsireportluns.md)

[**SM\_ScsiReadCapacity**](sm-scsireadcapacity.md)

The MS\_SM\_ScsiInformationMethods class is defined as follows in *Hbaapi.mof*:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MS_SM_ScsiInformationMethods%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




