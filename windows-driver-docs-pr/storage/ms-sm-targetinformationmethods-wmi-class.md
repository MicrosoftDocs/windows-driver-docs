---
title: MS\_SM\_TargetInformationMethods WMI Class
description: MS\_SM\_TargetInformationMethods WMI Class
ms.assetid: faedf8cf-d69f-4a4c-bc32-fd6df102d027
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MS\_SM\_TargetInformationMethods WMI Class


A WMI client uses the MS\_SM\_TargetInformationMethods WMI class to query an HBA miniport driver for fibre channel protocol (FCP) information. The HBA miniport driver for FCP is defined in the section about FCP Information Functions in the T11 committee's *Fibre Channel HBA API* specification. This WMI class has no data blocks. Therefore, the WMI tool suite generates structures that hold parameter data for the methods that belong to the class, but it does not generate a structure that corresponds to the class itself.

The MOF syntax for each method that belongs to this class is described in the reference page for the method. The following topics describe these methods and their accompanying structures:

[**SM\_GetTargetMapping**](sm-gettargetmapping.md)

[**SM\_GetBindingCapability**](sm-getbindingcapability.md)

[**SM\_GetBindingSupport**](sm-getbindingsupport.md)

[**SM\_SetBindingSupport**](sm-setbindingsupport.md)

[**SM\_GetPersistentBinding**](sm-getpersistentbinding.md)

[**SM\_SetPersistentBinding**](sm-setpersistentbinding.md)

[**SM\_RemovePersistentBinding**](sm-removepersistentbinding.md)

[**SM\_GetLUNStatistics**](sm-getlunstatistics.md)

The MS\_SM\_TargetInformationMethods class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SM_TargetInformationMethods
{
    [key]
    string  InstanceName;
    boolean Active;

    [Implemented, WmiMethodId(1)]
    void SM_GetTargetMapping(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [in ]
                 uint32 InEntryCount,
                [out, HBA_STATUS_QUALIFIERS]
                 HBA_STATUS HBAStatus,
                [out] 
                 uint32 TotalEntryCount,
                [out] 
                 uint32 OutEntryCount,
                [out, WmiSizeIs("OutEntryCount")]
                 MS_SMHBA_SCSIENTRY Entry[]
                );

    [Implemented, WmiMethodId(2)]
    void SM_GetBindingCapability(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus,
                [out, HBAType("SMHBA_BIND_CAPABILITY")] uint32 Flags
                );

    [Implemented, WmiMethodId(3)]
    void SM_GetBindingSupport(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [out, HBA_STATUS_QUALIFIERS]
                 HBA_STATUS HBAStatus,
                [out, HBAType("SMHBA_BIND_CAPABILITY")]
                 uint32 Flags
                );

    [Implemented, WmiMethodId(4)]
    void SM_SetBindingSupport(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [in, HBAType("SMHBA_BIND_CAPABILITY")]
                 uint32 Flags,
                [out, HBA_STATUS_QUALIFIERS]
                 HBA_STATUS HBAStatus
                );

    [Implemented, WmiMethodId(5)]
    void SM_GetPersistentBinding(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [in ]
                 uint32 InEntryCount,
                [out, HBA_STATUS_QUALIFIERS]
                 HBA_STATUS HBAStatus,
                [out]
                 uint32 TotalEntryCount,
                [out]
                 uint32 OutEntryCount,
                [out, WmiSizeIs("OutEntryCount")]
                 MS_SMHBA_BINDINGENTRY Entry[]
                );

    [Implemented, WmiMethodId(6)]
    void SM_SetPersistentBinding(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [in ] uint32 InEntryCount,
                [in, WmiSizeIs("InEntryCount")]
                 MS_SMHBA_BINDINGENTRY Entry[],
                [out, HBA_STATUS_QUALIFIERS]
                 HBA_STATUS HBAStatus,
                [out ] uint32 OutStatusCount,
                [out, WmiSizeIs("OutStatusCount")]
                 HBA_STATUS EntryStatus[]
                );

    [Implemented, WmiMethodId(7)]
    void SM_RemovePersistentBinding(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [in ]
                 uint32 EntryCount,
                [in, WmiSizeIs("EntryCount")]
                 MS_SMHBA_BINDINGENTRY Entry[],
                [out, HBA_STATUS_QUALIFIERS]
                 HBA_STATUS HBAStatus
                );

    [Implemented, WmiMethodId(8)]
    void SM_GetLUNStatistics(
                [in, HBAType("HBA_SCSIID")]
                 HBAScsiID Lunit,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out, HBAType("MS_SMHBA_PROTOCOLSTATISTICS") ]
                 MS_SMHBA_PROTOCOLSTATISTICS ProtocolStatistics
                );
};
```

 

 





