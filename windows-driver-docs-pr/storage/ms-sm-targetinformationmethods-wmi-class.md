---
title: MS\_SM\_TargetInformationMethods WMI Class
description: MS\_SM\_TargetInformationMethods WMI Class
ms.assetid: faedf8cf-d69f-4a4c-bc32-fd6df102d027
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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MS_SM_TargetInformationMethods%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




