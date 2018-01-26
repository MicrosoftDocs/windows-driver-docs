---
title: MSFC\_HBAPortAttributesResults WMI Class
description: MSFC\_HBAPortAttributesResults WMI Class
ms.assetid: f268a653-e3ee-47d0-9af8-925dc0545a2b
---

# MSFC\_HBAPortAttributesResults WMI Class


## <span id="ddk_msfc_hbaportattributesresults_wmi_class_kr"></span><span id="DDK_MSFC_HBAPORTATTRIBUTESRESULTS_WMI_CLASS_KR"></span>


A WMI client uses the MSFC\_HBAPortAttributesResults WMI class to query an HBA miniport driver for the attributes of a port on the HBA.

The MSFC\_HBAPortAttributesResults class is defined as follows in *Hbaapi.mof*:

```
class MSFC_HBAPortAttributesResults {
    [HBAType("HBA_WWN"), WmiDataId(1) ] uint8  NodeWWN[8];
    [HBAType("HBA_WWN"), WmiDataId(2) ] uint8  PortWWN[8];
    [ WmiDataId(3) ] uint32 PortFcId;
    [HBAType("HBA_PORTTYPE"), Values{"Unknown", "Other",
      "Not present", "Fabric", "Public Loop",
      "HBA_PORTTYPE_FLPORT", "Fabric Port",
      "Fabric expansion port", "Generic Fabric Port",
      "Private Loop", "Point to Point"} : amended,
      ValueMap{"1", "2", "3", "5", "6", "7", "8", "9",
      "10", "20", "21"},
      WmiDataId(4) ] uint32  PortType;
    [HBAType("HBA_PORTSTATE"), Values{"Unknown", "Operational",
      "User Offline", 
      "Bypassed", "In diagnostics mode", "Link Down", 
      "Port Error", "Loopback"} : amended,
      ValueMap{"1","2","3","4","5","6","7","8"},
      WmiDataId(5) ] uint32  PortState;
    [HBAType("HBA_COS"), WmiDataId(6) ] 
      uint32 PortSupportedClassofService;
   [HBAType("HBA_FC4TYPES"), WmiDataId(7)] 
      uint8 PortSupportedFc4Types[32];
    [HBAType("HBA_FC4TYPES"), WmiDataId(8)]
      uint8 PortActiveFc4Types[32];
    [HBAType("HBA_PORTSPEED"),
      Values{"1 GBit/sec", "2 GBit/sec", "10 GBit/sec", 
      "4 GBit/sec"} : amended,
      ValueMap{"1", "2", "4", "8"},
      WmiDataId(9)] uint32  PortSupportedSpeed;
    [HBAType("HBA_PORTSPEED"),
      Values{"1 GBit/sec", "2 GBit/sec", 
      "10 GBit/sec", "4 GBit/sec"} : amended,
      ValueMap{"1", "2", "4", "8"},
      WmiDataId(10) ] uint32  PortSpeed;
    [WmiDataId(11) ] uint32  PortMaxFrameSize;
    [HBAType("HBA_WWN"), WmiDataId(12) ] uint8  FabricName[8];
    [ WmiDataId(13) ] uint32  NumberofDiscoveredPorts;
};
```

When compiled this class definition produces the following data structure:

[**MSFC\_HBAPortAttributesResults**](https://msdn.microsoft.com/library/windows/hardware/ff562510)

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSFC_HBAPortAttributesResults%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




