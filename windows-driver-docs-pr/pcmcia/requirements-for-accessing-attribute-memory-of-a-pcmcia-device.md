---
title: Requirements for Accessing Attribute Memory of a PCMCIA Device
description: Requirements for Accessing Attribute Memory of a PCMCIA Device
MS-HAID:
- 'pamch1\_6d6ba262-48bf-4a88-81ea-79eb232c1584.xml'
- 'PCMCIA.requirements\_for\_accessing\_attribute\_memory\_of\_a\_pcmcia\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8af41eb0-c057-43c9-a50f-b7d88e1bed6a
keywords: ["attribute memory WDK PCMCIA bus , requirements"]
---

# Requirements for Accessing Attribute Memory of a PCMCIA Device


## <a href="" id="ddk-requirements-for-accessing-attribute-memory-of-a-pcmcia-device-kg"></a>


This section describes the requirements for the following types of access to attribute memory of a PCMCIA device:

<a href="" id="query-device-information"></a>**Query Device Information**  
A driver typically queries the following device information:

-   Identity of the device

-   Device parameters, such as capacity or speed that the driver uses to configure a device

-   Static data, such as a MAC address

Information queries are usually read-only, and are done relatively infrequently.

<a href="" id="configure-a-device"></a>**Configure a Device**  
Some drivers require write access to configuration registers in attribute memory.

A driver usually configures a device infrequently.

Note that the PCMCIA bus driver manages the standard PCMCIA configuration registers in attribute memory. Drivers must not write to these registers. If they do, unpredictable system behavior can occur. System setup and the Plug and Play manager support INF file directives - for example, the [**INF LogConfig Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547448) - that must be used to configure these registers.

<a href="" id="operate-a-device"></a>**Operate a device**  
Some PCMCIA devices use control registers located in attribute memory. Drivers must typically directly access these registers within an ISR. Accesses of this type can be relatively high in frequency, and require fast direct memory access.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Requirements%20for%20Accessing%20Attribute%20Memory%20of%20a%20PCMCIA%20Device%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




