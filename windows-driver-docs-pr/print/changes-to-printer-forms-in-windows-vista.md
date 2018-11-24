---
title: Changes to Printer Forms in Windows Vista
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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




