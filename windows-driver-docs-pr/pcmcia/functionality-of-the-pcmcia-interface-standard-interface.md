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

 

 





