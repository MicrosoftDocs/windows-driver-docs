---
title: Printer Driver and Plug-in Helper Interfaces
author: windows-driver-content
description: Printer Driver and Plug-in Helper Interfaces
MS-HAID:
- 'drvarch\_ab6690bb-4a09-453d-b7f9-2c8e9daac76e.xml'
- 'print.printer\_driver\_and\_plug\_in\_helper\_interfaces'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 21e5ae44-01e8-4f80-8d67-18e4d9c190c5
---

# Printer Driver and Plug-in Helper Interfaces


The [IPrintCoreHelper](https://msdn.microsoft.com/library/windows/hardware/ff552960) interface, which is available in Windows Vista and later, provides basic functionality that is available in all four core driver modules--Unidrv rendering, Unidrv user interface (UI), Pscript5 rendering, and Pscript5 UI. A single interface is provided to all four modules because:

-   The interface reflects the underlying architecture.

-   The interface provides the ability to write common code modules for plug-ins to perform certain behavior, such as constraints resolution.

You can use the **IPrintCoreHelper** interface to write a single UI replacement plug-in for Unidrv-based and Pscript5-based drivers.

Because of the differences between the Pscript5 and Unidrv driver infrastructures, there are two additional interfaces, [IPrintCoreHelperUni](https://msdn.microsoft.com/library/windows/hardware/ff552940) and [IPrintCoreHelperPS](https://msdn.microsoft.com/library/windows/hardware/ff552906), that inherit from the **IPrintCoreHelper** interface and that provide extended services based on the individual drivers. These interfaces are available only in their respective modules. The Pscript5 helper interface, **IPrintCoreHelperPS**, provides access to certain PostScript printer description (PPD) data, while the Unidrv helper interface, **IPrintCoreHelperUni**, provides the ability to access generic printer configuration (GPD) files by means of the GDL parser, which is new for Windows Vista.

This section provides the following topics:

[Unidrv and Pscript5 Helper Interfaces for Plug-ins](unidrv-and-pscript5-helper-interfaces-for-plug-ins.md)

[Publishing the Interfaces](publishing-the-interfaces.md)

[Details of the IPrintCoreHelper Interface](details-of-the-iprintcorehelper-interface.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Driver%20and%20Plug-in%20Helper%20Interfaces%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


