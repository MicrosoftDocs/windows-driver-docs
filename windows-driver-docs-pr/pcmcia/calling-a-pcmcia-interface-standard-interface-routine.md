---
title: Calling a PCMCIA\_INTERFACE\_STANDARD Interface Routine
description: Calling a PCMCIA\_INTERFACE\_STANDARD Interface Routine
MS-HAID:
- 'mcch2\_051ca28a-f0dc-481e-ab30-476a555f56b8.xml'
- 'PCMCIA.calling\_a\_pcmcia\_interface\_standard\_interface\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 468d2037-a7d5-4851-9f41-d1e6c9006750
---

# Calling a PCMCIA\_INTERFACE\_STANDARD Interface Routine


## <a href="" id="ddk-calling-a-pcmcia-interface-standard-interface-routine-kg"></a>


This section describes how to call a PCMCIA\_INTERFACE\_STANDARD interface routine.

After a driver obtains an [PCMCIA\_INTERFACE\_STANDARD Interface Memory Card Routines](https://msdn.microsoft.com/library/windows/hardware/ff537607) structure from the PCMCIA bus driver, the driver can call the interface routines.

Each interface routine requires a context pointer. The driver must use the **Context** member value returned by the PCMCIA bus driver in the PCMCIA\_INTERFACE\_STANDARD structure. If the context pointer is not valid, the system behavior is not defined, and the system might halt.

The PCMCIA\_INTERFACE\_STANDARD interface routines can be called at IRQL &lt;= DISPATCH\_LEVEL. To maintain overall system performance, it is strongly recommended that a driver call these routines at IRQL &lt; DISPATCH\_LEVEL. Calling an interface routine at IRQL DISPATCH\_LEVEL can cause the caller to block system operation for a significant period of time.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Calling%20a%20PCMCIA_INTERFACE_STANDARD%20Interface%20Routine%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




