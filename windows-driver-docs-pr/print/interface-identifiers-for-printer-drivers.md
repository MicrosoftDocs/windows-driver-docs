---
title: Interface Identifiers for Printer Drivers
author: windows-driver-content
description: Interface Identifiers for Printer Drivers
MS-HAID:
- 'custdrvr\_f26b006e-edec-4272-8e4e-9be75b383556.xml'
- 'print.interface\_identifiers\_for\_printer\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8182cba5-4461-4ca0-8b01-342519609b1f
keywords: ["COM interfaces WDK print , interface identifiers", "interface identifiers WDK print", "plug-ins WDK print , interface identifiers", "identifiers WDK printer", "GUIDs WDK printer"]
---

# Interface Identifiers for Printer Drivers


## <a href="" id="ddk-interface-identifiers-for-printer-drivers-gg"></a>


A set of GUIDs is defined in prcomoem.h. Each of these GUIDs is an interface identifier for one of the COM interfaces used for communication between the printer drivers (Unidrv and Pscript5) and plug-ins.

For Windows 2000 and Windows XP, the following GUIDs are defined:

**IID\_IPrintOemUI**
**IID\_IPrintOemUI2** (Pscript5 UI plug-ins on Windows XP and later versions of the Windows operating system)
**IID\_IPrintOemDriverUI**
**IID\_IPrintCoreUI2** (Pscript5 UI plug-ins on Windows XP and later versions of the Windows operating system)
**IID\_IPrintOemUni**
**IID\_IPrintOemUni2** (Unidrv render plug-ins on Windows XP and later versions of the Windows operating system)
**IID\_IPrintOemUni3** (Unidrv render plug-ins on Windows Vista and later versions of the Windows operating system)
**IID\_IPrintOemDriverUni**
**IID\_IPrintOemPS**
**IID\_IPrintOemPS2** (Pscript5 render plug-ins on Windows XP and later versions of the Windows operating system)
**IID\_IPrintOemDriverPS**
**IID\_IPrintCorePS2** (Pscript5 render plug-ins on Windows XP and later versions of the Windows operating system)
Each GUID identifies one version of one interface. If a new version of an interface is defined, a new GUID is added to the list.

User interface plug-ins and rendering plug-ins must identify the interface versions they support. The printer driver (Unidrv or Pscript5) calls a plug-in's **IUnknown::QueryInterface** method (described in the Windows SDK documentation), specifying an interface identifier as input. If the plug-in supports the specified version, the method must return a pointer to the interface along with a return status of S\_OK. Otherwise, it must return E\_NOINTERFACE. The driver starts with the interface identifier for the most recent version and continues to call **QueryInterface** with earlier version identifiers until the method returns S\_OK or the driver exhausts the list of version identifiers.

Likewise, Unidrv and Pscript5 provide **IUnknown::QueryInterface** methods for the [IPrintOemDriverUI](iprintoemdriverui-com-interface.md), [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) COM interfaces. Plug-ins should call the appropriate interface's **QueryInterface** method to determine the driver's supported interface version and to receive an interface pointer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Interface%20Identifiers%20for%20Printer%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


