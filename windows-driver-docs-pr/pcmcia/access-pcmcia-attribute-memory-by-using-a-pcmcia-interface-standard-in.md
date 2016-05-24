---
title: Access PCMCIA Attribute Memory by Using a PCMCIA\_INTERFACE\_STANDARD Interface
description: Access PCMCIA Attribute Memory by Using a PCMCIA\_INTERFACE\_STANDARD Interface
MS-HAID:
- 'pamch1\_3e3e298d-5af2-46b3-b296-69006d4c6095.xml'
- 'PCMCIA.access\_pcmcia\_attribute\_memory\_by\_using\_a\_pcmcia\_interface\_standard\_in'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cd73a8da-1441-4e95-a955-97235ad091ce
keywords: ["PCMCIA_INTERFACE_STANDARD", "attribute memory WDK PCMCIA bus , PCMCIA_INTERFACE_STANDARD interface"]
---

# Access PCMCIA Attribute Memory by Using a PCMCIA\_INTERFACE\_STANDARD Interface


## <a href="" id="ddk-access-pcmcia-attribute-memory-by-using-a-pcmcia-interface-standar"></a>


This section describes how a driver can use a PCMCIA\_INTERFACE\_STANDARD interface to access attribute memory.

The PCMCIA interface standard is provided primarily for memory card drivers and file systems.

A driver can use the [**PCMCIA\_MODIFY\_MEMORY\_WINDOW**](https://msdn.microsoft.com/library/windows/hardware/ff537610) interface routine supported by the PCMCIA\_INTERFACE\_STANDARD interface. PCMCIA\_MODIFY\_MEMORY\_WINDOW sets the attributes of a memory window for a PCMCIA memory card. The memory window is mapped by the PCMCIA bus driver. Note that this routine does not provide a permanent window, it only modifies the current settings for an existing window. In addition, settings are not persistent over a change in the system power state.

For more information, see [PCMCIA\_INTERFACE\_STANDARD Interface for Memory Cards](https://msdn.microsoft.com/library/windows/hardware/ff537606).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Access%20PCMCIA%20Attribute%20Memory%20by%20Using%20a%20PCMCIA_INTERFACE_STANDARD%20Interface%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




