---
title: Functionality of the PCMCIA\_INTERFACE\_STANDARD Interface
description: Functionality of the PCMCIA\_INTERFACE\_STANDARD Interface
MS-HAID:
- 'mcch2\_a8029e6d-4c7f-439e-8f01-0cc3368ff3f4.xml'
- 'PCMCIA.functionality\_of\_the\_pcmcia\_interface\_standard\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 301b4165-4753-4d55-9760-17628174c043
---

# Functionality of the PCMCIA\_INTERFACE\_STANDARD Interface


## <a href="" id="ddk-functionality-of-the-pcmcia-interface-standard-interface-kg"></a>


This section describes the functionality of the PCMCIA\_INTERFACE\_STANDARD interface that PCMCIA bus driver supports in Windows 2000 and later operating systems. The PCMCIA\_INTERFACE\_STANDARD interface provides a set of routines that can be called directly by a PCMCIA driver. These interface routines support the following operations:

-   Modify the attributes of the memory window that is mapped by the PCMCIA bus driver

-   Set the *Vpp* (secondary power source) level for the device

-   Determine if the card memory is write-protected

For more information about the routines provided by the PCMCIA\_INTERFACE\_STANDARD interface, see [PCMCIA\_INTERFACE\_STANDARD Interface Memory Card Routines](https://msdn.microsoft.com/library/windows/hardware/ff537607).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Functionality%20of%20the%20PCMCIA_INTERFACE_STANDARD%20Interface%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




