---
title: Changes to Printer Forms in Windows Vista
author: windows-driver-content
description: Changes to Printer Forms in Windows Vista
ms.assetid: 6e970cbd-1c7f-4c48-8d05-a29f922a3f33
keywords:
- printer forms WDK
- forms WDK printer
- special forms WDK printer
- special paper sizes WDK printer
- paper sizes WDK forms
- custom forms WDK printer
- FORM_INFO_2 data structure WDK printer
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Changes to Printer Forms in Windows Vista


Before Windows Vista, forms were identified internally by using the name and size of the form. This method, however, did not always work well when the print servers and the client computers used printer drivers that were localized to different languages. In Windows Vista, the print spooler has been improved so printer drivers can support client computers and print servers that are localized to different languages.

Windows Vista adds the FORM\_INFO\_2 data structure, which is a superset of the FORM\_INFO\_1 data structure that contains additional members for the information that you need to enable printer drivers to work across systems with different languages.

The Unidrv printer driver was also upgraded for Windows Vista to use the FORM\_INFO\_2 data structure and to fill in the additional members by using the data from the GPD file. You can upgrade monolithic printer drivers that use the FORM\_INFO\_1 structure to use the FORM\_INFO\_2 structure if they need the additional information that the new structure provides.

This section describes how you can update the GPD file of your Unidrv printer driver or the code in your monolithic printer driver to use the new members that the FORM\_INFO\_2 data structure provides.

This section describes the following improvements in printer forms for Windows Vista:

[FORM\_INFO\_2 Data Structure](form-info-2-data-structure.md)

[Improved Form Matching Algorithm](improved-form-matching-algorithm.md)

[Improved Form-to-Tray Matching Algorithm](improved-form-to-tray-matching-algorithm.md)

For more information about using printer forms, see the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Changes%20to%20Printer%20Forms%20in%20Windows%20Vista%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


