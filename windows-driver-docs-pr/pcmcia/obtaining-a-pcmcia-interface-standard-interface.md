---
title: Obtaining a PCMCIA\_INTERFACE\_STANDARD Interface
description: Obtaining a PCMCIA\_INTERFACE\_STANDARD Interface
MS-HAID:
- 'mcch2\_136e3e61-0080-48cf-8372-1f276a39139e.xml'
- 'PCMCIA.obtaining\_a\_pcmcia\_interface\_standard\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 475bf66a-5b6e-4a06-95f7-b7280dd7276d
---

# Obtaining a PCMCIA\_INTERFACE\_STANDARD Interface


## <a href="" id="ddk-obtaining-a-pcmcia-interface-standard-interface-kg"></a>


This section describes how a driver can obtain a PCMCIA\_INTERFACE\_STANDARD interface for a PCMCIA memory card from the PCMCIA bus driver.

A driver obtains a PCMCIA\_INTERFACE\_STANDARD interface by creating and sending an IRP\_MJ\_PNP request that specifies a [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) minor function code. The driver carries out the following operations:

-   Allocates and zero-fills a [PCMCIA\_INTERFACE\_STANDARD Interface Memory Card Routines](https://msdn.microsoft.com/library/windows/hardware/ff537607) structure in the paged memory pool.

-   Creates an IRP for the query interface request and gets the next stack location for the new IRP.

-   Sets the following members in the new stack location:
    -   The **Parameters.QueryInterface.Interface** member points to the driver-allocated PCMCIA\_INTERFACE\_STANDARD structure that was allocated by the driver.
    -   The **Parameters.QueryInterface.InterfaceType** member specifies a standard PCMCIA interface by the GUID value GUID\_PCMCIA\_INTERFACE\_STANDARD.
-   Sets a completion routine and sends the request down the driver stack.

If the request is successful, the PCMCIA bus driver fills in the PCMCIA\_INTERFACE\_STANDARD structure pointed to by **Parameters.QueryInterface.Interface**.

A driver must be running at IRQL &lt; DISPATCH\_LEVEL to send this request down the driver stack.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Obtaining%20a%20PCMCIA_INTERFACE_STANDARD%20Interface%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




