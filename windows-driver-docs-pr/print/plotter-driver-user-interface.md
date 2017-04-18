---
title: Plotter Driver User Interface
author: windows-driver-content
description: Plotter Driver User Interface
ms.assetid: 681e9215-d34b-4991-9c0f-b9dbe23412f6
keywords: ["Plotter Driver WDK print , user interface", "MSPlot WDK print , user interface", "user interface WDK MSPlot"]
---

# Plotter Driver User Interface


## <a href="" id="ddk-plotter-driver-user-interface-gg"></a>


The plotter user interface employs [CPSUI](common-property-sheet-user-interface.md) to create the following two property sheet pages:

-   The **Device Settings** page for the printer property sheet, which is displayed when a user selects the **Properties** menu item from the printer folder or a printer window. This page lists printer-specific configuration settings.

-   The **Layout**, **Paper/Quality**, and **Advanced** pages for the document property sheet, which are displayed when a user selects the **Document Defaults** menu item from the printer folder or a printer window, or when an application calls the **PrinterProperties** or **DocumentProperties** functions (described in the Microsoft Windows SDK documentation). This page lists document-specific configuration settings.

These property sheets contain the plotter features and options specified by a plotter's minidriver. They also allow the user to modify option values.

The plotter's user interface is implemented as a user-mode [printer interface DLL](printer-interface-dll.md). Code within this DLL, in conjunction with CPSUI, specifies the contents of the property sheet pages. The DLL enforces constraints on which plotter options can be combined, based on information in the minidriver. It also ensures that users do not select options not installed on the plotter.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Plotter%20Driver%20User%20Interface%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


