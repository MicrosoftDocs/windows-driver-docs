---
title: Autoconfiguration Flow for GPD in Windows Vista
author: windows-driver-content
description: Autoconfiguration Flow for GPD in Windows Vista
MS-HAID:
- 'autocfg\_98e70186-0e3f-4c0d-afb9-fcf5664fafed.xml'
- 'print.autoconfiguration\_flow\_for\_gpd\_in\_windows\_vista'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 41468218-fa05-4431-a57d-3056449f2e2e
keywords: ["GPD files WDK GDL extensions , autoconfiguration flow", "in-box autoconfiguration support WDK printer , sequence of steps"]
---

# Autoconfiguration Flow for GPD in Windows Vista


Autoconfiguration follows the following sequence:

1.  Port Monitor sends to the spooler a notification that contains any values that formerly were not in the cache or that changed.

2.  The spooler responds to the notification from the port monitor by calling [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564).

3.  Printer\_Event\_Configuration is passed to the driver that contains any and all new values. The driver is notified that the value of an attribute has changed, and the registry is also updated.

4.  If the notification is too big, Reduced Schema Event is called.

5.  The PPD file is parsed, including all GDL file extensions and GDL content within the PPD. All GDL content in either GDL file extensions or throughout the PPD file must be surrounded with **\*Ifdef**: GDL\_Enabled and **\*Endif**: GDL\_Enabled.

6.  Your plug-in will retrieve the value for **\*MSBidiValue**, which will be based on the current string value for **\*QueryString**. For example, a **\*QueryString** value of "\\Printer.Configuration.DuplexUnit:Installed" will represent a **\*BidiValue** value of BOOL(TRUE).

7.  Your plug-in will update the driver UI according to the latest configuration.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autoconfiguration%20Flow%20for%20GPD%20in%20Windows%20Vista%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


