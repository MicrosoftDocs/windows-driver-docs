---
title: MS\_SM\_EventControl WMI Class
description: MS\_SM\_EventControl WMI Class
ms.assetid: d5c6a308-2782-4846-81f9-f4932d8caac6
---

# MS\_SM\_EventControl WMI Class


The MS\_SM\_EventControl WMI class defines WMI methods that allow WMI clients to control the delivery of link, port, and target events. This WMI class has no data blocks. Therefore, the WMI tool suite generates declarations for structures that hold parameter data for the methods that belong to the class, but it does not generate a structure declaration that corresponds to the class itself.

The MOF syntax for each method that belongs to this class is described in the reference page for the method. The following topics describe these methods and their accompanying structures:

[**SM\_AddTarget**](sm-addtarget.md)

[**SM\_RemoveTarget**](sm-removetarget.md)

[**SM\_AddPort**](sm-addport.md)

[**SM\_RemovePort**](sm-removeport.md)

[**SM\_AddLink**](sm-addlink.md)

[**SM\_RemoveLink**](sm-removelink.md)

The MS\_SM\_EventControl class is defined as follows in *Hbaapi.mof*:

```
class MS_SM_EventControl 
{ 
    [key] 
    string  InstanceName; 
    boolean Active; 

    //
    // These methods are used to control delivery of MS_SM_TargetEvents
//
    [ Implemented, WmiMethodId(1) ]
    void SM_AddTarget(
            [in, HBAType("HBA_WWN") ] uint8 HbaPortWWN[8],
            [in, HBAType("HBA_WWN") ] uint8 DiscoveredPortWWN[8],
            [in, HBAType("HBA_WWN") ] uint8 DomainPortWWN[8],
            [in ] uint32  AllTargets,
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );

    [ Implemented, WmiMethodId(2) ]
    void SM_RemoveTarget(
            [in, HBAType("HBA_WWN") ] uint8 HbaPortWWN[8],
            [in, HBAType("HBA_WWN") ] uint8 DiscoveredPortWWN[8],
            [in, HBAType("HBA_WWN") ] uint8 DomainPortWWN[8],
            [in ] uint32  AllTargets,
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );


//
// These methods are used to control delivery of MS_SM_PortEvents
//
    [ Implemented, WmiMethodId(3) ]
    void SM_AddPort(
            [in, HBAType("HBA_WWN") ] uint8 PortWWN[8],
            [in, EVENT_TYPES_QUALIFIERS ] uint32 EventType,
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );

    [ Implemented, WmiMethodId(4) ]
    void SM_RemovePort(
            [in, HBAType("HBA_WWN") ] uint8 PortWWN[8],
            [in, EVENT_TYPES_QUALIFIERS ] uint32 EventType,
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );

//
// These methods are used to control delivery of MSFC_LinkEvents
//
    [ Implemented, WmiMethodId(10) ]
    void SM_AddLink(
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );

    [ Implemented, WmiMethodId(11) ]
    void SM_RemoveLink(
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );
};
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MS_SM_EventControl%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




