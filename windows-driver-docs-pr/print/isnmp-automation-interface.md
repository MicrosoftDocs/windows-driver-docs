---
title: ISNMP Automation Interface
author: windows-driver-content
description: ISNMP Automation Interface
MS-HAID:
- 'webfnc\_4ff82461-8ece-4336-8f86-9461ad4ec8d7.xml'
- 'print.isnmp\_automation\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 63f2f14d-ea9d-437c-9853-06889219627d
---

# ISNMP Automation Interface


## <span id="ddk_isnmp_automation_interface_gg"></span><span id="DDK_ISNMP_AUTOMATION_INTERFACE_GG"></span>


The Automation interface for the **ISNMP** object is essentially an OLE automation wrapper for the functions in the Simple Network Management Protocol (SNMP) Management API. The **ISNMP** interface enables an ASP Web page to set and retrieve values associated with SNMP object identifiers (OIDs). For more information about the SNMP Management API, see the Windows SDK documentation.

The **ISNMP** interface works only with printers that use Microsoft's standard TCIP/IP [*port monitor*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-port-monitor). **ISNMP** is supported in Microsoft Windows 2000 and later versions of Windows. (However, the [**ISNMP::GetAsByte**](isnmp-getasbyte.md) property is supported only in Windows XP and later versions of Windows.)

The programmatic identifier for the **ISNMP** object is OlePrn.OleSNMP.

For more information about how to access printers from ASP Web pages, see [Internet Printing](https://msdn.microsoft.com/library/windows/hardware/ff551735).

The methods in the **ISNMP** interface are described in the following section:

[ISNMP Methods](isnmp-methods.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ISNMP%20Automation%20Interface%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


