---
title: Print Capabilities Support in GDI-based, Monolithic Print Drivers
author: windows-driver-content
description: Print Capabilities Support in GDI-based, Monolithic Print Drivers
ms.assetid: 4b8116a8-7aee-44cb-9c9d-560662b61073
keywords:
- Print Capabilities WDK , GDI-based monolithic print drivers
- GDI-based monolithic print drivers WDK
- monolithic print drivers WDK
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Print Capabilities Support in GDI-based, Monolithic Print Drivers


To provide complete Print Ticket and Print Capabilities support, GDI-based, monolithic print drivers and [XPSDrv print drivers](xpsdrv-printer-drivers.md) that cannot use the GPD printer interface DLL must implement the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375). GDI-based, monolithic print drivers are not required to support this interface although this could limit the printer's features that are exposed in the PrintCapabilities document and supported by the PrintTicket document. XPSDrv print drivers, however, must implement **IPrintTicketProvider**.

**Note**   For Windows 7, the **MxdcGetPDEVAdjustment** function has new parameters for landscape rotation. For more information, see [**MxdcXDCGetPDEVAdjustment**](https://msdn.microsoft.com/library/windows/hardware/ff557558).

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Capabilities%20Support%20in%20GDI-based,%20Monolithic%20Print%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


