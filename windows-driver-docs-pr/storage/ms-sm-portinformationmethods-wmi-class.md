---
title: MS\_SM\_PortInformationMethods WMI Class
description: MS\_SM\_PortInformationMethods WMI Class
ms.assetid: 5bf44288-7e1f-48e6-aa02-1e706b73f046
---

# MS\_SM\_PortInformationMethods WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SM\_PortInformationMethods class to query port attributes.

The MS\_SM\_PortInformationMethods class is defined as follows in *Hbaapi.mof*:

```
class MS_SM_PortInformationMethods
{
    [key]
    string  InstanceName;
    boolean Active;

    [Implemented, WmiMethodId(1)]
    void SM_GetPortType(
                [in ] 
                 uint32  PortIndex,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out, HBA_PORTTYPE_QUALIFIERS ]
                 uint32  PortType
                );

    [Implemented, WmiMethodId(2)]
    void SM_GetAdapterPortAttributes(
                [in ] 
                 uint32  PortIndex,
                [in,
                 cpp_quote("#define SM_PORT_SPECIFIC_ATTRIBUTES_MAXSIZE "
                           " max(sizeof(MS_SMHBA_FC_Port), "
                           " sizeof(MS_SMHBA_SAS_Port))")
                ]
                 uint32  PortSpecificAttributesMaxSize,
                [out, HBA_STATUS_QUALIFIERS ] 
                 HBA_STATUS  HBAStatus,
                [out, HBAType("MS_SMHBA_PORTATTRIBUTES") ] 
                 MS_SMHBA_PORTATTRIBUTES  PortAttributes
                );

    [Implemented, WmiMethodId(3)]
    void SM_GetDiscoveredPortAttributes(
                [in ] uint32  PortIndex,
                [in ] uint32  DiscoveredPortIndex,
                [in ] uint32  PortSpecificAttributesMaxSize,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out, HBAType("MS_SMHBA_PORTATTRIBUTES") ]
                 MS_SMHBA_PORTATTRIBUTES PortAttributes
                );

    [Implemented, WmiMethodId(4)]
    void SM_GetPortAttributesByWWN(
                [in, HBAType("HBA_WWN")] uint8  PortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [in ]
                 uint32 PortSpecificAttributesMaxSize,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out, HBAType("MS_SMHBA_PORTATTRIBUTES") ]
                 MS_SMHBA_PORTATTRIBUTES PortAttributes
                );

    [Implemented, WmiMethodId(5)]
    void SM_GetProtocolStatistics(
                [in ] uint32  PortIndex,
                [in ] uint32  ProtocolType,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out, HBAType("MS_SMHBA_PROTOCOLSTATISTICS") ]
                 MS_SMHBA_PROTOCOLSTATISTICS ProtocolStatistics
                );

    [Implemented, 
     Description("Typical counters SMHBA_SASPHYSTATISTICS (9 counters) or"
                 " MSFC_HBAPortStatistics (15 counters)"),
     WmiMethodId(6)
    ]
    void SM_GetPhyStatistics(
                [in ] uint32  PortIndex,
                [in ] uint32  PhyIndex,
                [in ] uint32  InNumOfPhyCounters,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out] uint32  TotalNumOfPhyCounters, 
                [out] uint32  OutNumOfPhyCounters, 
                [out, WmiSizeIs("OutNumOfPhyCounters")]
                 sint64 PhyCounter[]
                );

    [Implemented, WmiMethodId(7)]
    void SM_GetFCPhyAttributes(
                [in ] uint32  PortIndex,
                [in ] uint32  PhyIndex,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out, HBAType("MS_SMHBA_FC_PHY") ]
                 MS_SMHBA_FC_PHY PhyType
                );

    [Implemented, WmiMethodId(8)]
    void SM_GetSASPhyAttributes(
                [in ] uint32  PortIndex,
                [in ] uint32  PhyIndex,
                [out, HBA_STATUS_QUALIFIERS ]
                 HBA_STATUS HBAStatus,
                [out, HBAType("MS_SMHBA_SAS_PHY") ]
                 MS_SMHBA_SAS_PHY PhyType
                );

    [Implemented, WmiMethodId(10)]
    void SM_RefreshInformation();
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

MS\_SM\_PortInformationMethods

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MS_SM_PortInformationMethods%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




