---
title: Autoconfig Flow in Windows Vista for PPD
author: windows-driver-content
description: Autoconfig Flow in Windows Vista for PPD
ms.assetid: 60675cd3-fe98-4772-aa1b-a73529480d8a
keywords: ["PPD files WDK autoconfiguration , sequence of steps", "in-box autoconfiguration support WDK printer , sequence of steps"]
---

# Autoconfig Flow in Windows Vista for PPD


Autoconfig follows the following sequence:

1.  Port Monitor sends to the spooler a notification containing any values that formerly were not in the cache or that changed.

2.  Spooler responds to the notification from the port monitor by calling DrvPrinterEvent.

3.  Printer\_Event\_Configuration is passed to the driver containing any and all new values. The driver is notified that the value of an attribute has changed. The registry is also updated.

4.  If the notification is too big, a Reduced Schema Event is called.

5.  The PPD file is parsed including all GDL file extensions and GDL content within the PPD. All GDL content in either GDL file extensions or throughout the PPD file must be surrounded with `*Ifdef: GDL_Enabled` and `*Endif: GDL_Enabled`.

6.  The IHV plug-in will retrieve the value for **\*MSBidiValue** which will be based on the current string value for **\*QueryString**. For example, a **\*QueryString** value of \\Printer.Configuration.DuplexUnit:Installed will represent a **\*BidiValue** value of BOOL(TRUE).

7.  The IHV plug-in will update the driver UI according to the latest configuration.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autoconfig%20Flow%20in%20Windows%20Vista%20for%20PPD%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


