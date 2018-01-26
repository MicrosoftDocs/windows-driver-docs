---
title: MS\_SM\_AdapterInformationQuery WMI Class
description: MS\_SM\_AdapterInformationQuery WMI Class
ms.assetid: 3a396a73-6ade-455a-ac3f-fd0175cc704e
---

# MS\_SM\_AdapterInformationQuery WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SM\_AdapterInformationQuery class to expose attribute information that is associated with a SAS adapter.

The MS\_SM\_AdapterInformationQuery class is defined as follows in *Hbaapi.mof*:

```
class MS_SM_AdapterInformationQuery
{
    [key] 
    string  InstanceName;
    boolean Active;

    [Description ("Unique identifier for the adapter. This idenitifer must "
                  "be unique among all adapters. The same "
                  "value for the identifier must be used for the same adapter "
                  "in other classes that expose adapter information"),

  // WmiRefClass("MS_SM_ChannelAdapter"),  // ?? need a new ref class
     WmiRefProperty("UniqueAdapterId"),
     WmiDataId(1)
    ]
    uint64 UniqueAdapterId;             // CIM_FibreChannelAdapter REF
                                        // ?? need a new REF 

    [HBA_STATUS_QUALIFIERS, 
     WmiDataId(2)
    ]
    HBA_STATUS HBAStatus;

    [WmiDataId(3)]
    uint32 NumberOfPorts;   

    [WmiDataId(4)]
    uint32 VendorSpecificID;

    [
     cpp_quote("\n"
     "   //******************************************************************\n"
     "   //\n"
     "   //  The string type is variable length (up to MaxLen).              \n"
     "   //  Each string starts with a ushort that holds the strings length  \n"
     "   //  (in bytes) followed by the WCHARs that make up the string.      \n"
     "   //\n"
     "   //******************************************************************\n"
     "\n"),

     MaxLen(64), 
     WmiDataId(5)
    ]
    string Manufacturer;

    [MaxLen(64), WmiDataId(6)]
    string SerialNumber;

    [MaxLen(256), WmiDataId(7)]
    string Model;

    [MaxLen(256), WmiDataId(8)]
    string ModelDescription;

    [MaxLen(256), WmiDataId(9)]
    string HardwareVersion;

    [MaxLen(256), WmiDataId(10)]
    string DriverVersion;

    [MaxLen(256), WmiDataId(11)]
    string OptionROMVersion;

    [MaxLen(256), WmiDataId(12)]
    string FirmwareVersion;

    [MaxLen(256), WmiDataId(13)]
    string DriverName;

    [MaxLen(256), WmiDataId(14)]
    string HBASymbolicName;

    [MaxLen(256), WmiDataId(15)]
    string RedundantOptionROMVersion;

    [MaxLen(256), WmiDataId(16)]
    string RedundantFirmwareVersion;

    [MaxLen(256), WmiDataId(17)]
    string MfgDomain;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SM\_AdapterInformationQuery**](https://msdn.microsoft.com/library/windows/hardware/ff563194)

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MS_SM_AdapterInformationQuery%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




