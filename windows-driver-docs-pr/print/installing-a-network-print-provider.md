---
title: Installing a Network Print Provider
author: windows-driver-content
description: Installing a Network Print Provider
MS-HAID:
- 'provider\_ec0b4e3a-7ee8-4732-bf65-298700892c46.xml'
- 'print.installing\_a\_network\_print\_provider'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 448101f8-cb26-4a6f-807d-f110978321da
keywords: ["print providers WDK , installing", "network print providers WDK , installing", "installing print providers WDK"]
---

# Installing a Network Print Provider


## <a href="" id="ddk-installing-a-network-print-provider-gg"></a>


To install a new network print provider, you must supply an installer that copies the provider DLL into the target system's \\System32 subdirectory and then calls **AddPrintProvidor** (described in the Microsoft Windows SDK documentation). This function creates a registry entry for the provider and adds the provider to the end of the spooler's list of installed providers. The function then loads the provider DLL and calls the provider's [**InitializePrintProvidor**](https://msdn.microsoft.com/library/windows/hardware/ff551614) function.

To create a connection to a printer supported by a network print provider, a user invokes the Add Printer Wizard and chooses the "Network printer server" option. The user specifies a print queue using the \\\\*Server*\\*Printer* format, and the provider's **OpenPrinter** function must recognize that print queue name.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20a%20Network%20Print%20Provider%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


