---
title: Providing DEVMODE Structure Additions
author: windows-driver-content
description: Providing DEVMODE Structure Additions
MS-HAID:
- 'custdrvr\_e4f470d5-853a-4f48-8b25-d12e235e7172.xml'
- 'print.providing\_devmode\_structure\_additions'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7ce698f5-14c7-484d-be3d-b41c690b9576
keywords: ["user interface plug-ins WDK print , DEVMODEW structure additions", "UI plug-ins WDK print , DEVMODEW structure additions", "DEVMODEW", "private DEVMODE WDK print", "public DEVMODE WDK print"]
---

# Providing DEVMODE Structure Additions


## <a href="" id="ddk-providing-devmode-structure-additions-gg"></a>


Your UI plug-in can add its own private members to the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure, as illustrated in the following figure.

![diagram illustrating public and private devmode sections](images/dvmdstru.png)

A UI plug-in can use these private DEVMODE members to store values associated with customized printer options. The plug-in makes these options available to the user by [modifying a driver-supplied property sheet page](modifying-a-driver-supplied-property-sheet-page.md) or by [adding new property sheet pages](adding-new-property-sheet-pages.md).

If your UI plug-in adds private DEVMODE members, the [**OEM\_DMEXTRAHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff559588) structure must prefix the added members.

You are not required to add members to the DEVMODE structure, but if you do, your UI plug-in must implement the [**IPrintOemUI::DevMode**](https://msdn.microsoft.com/library/windows/hardware/ff554167) method. This method's purpose, depending on input arguments, is to return the size of, initialize, convert, or validate the additional DEVMODE members.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Providing%20DEVMODE%20Structure%20Additions%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


