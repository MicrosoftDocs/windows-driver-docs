---
title: Global and Local Options Files
description: Global and Local Options Files
ms.assetid: 9b367e9f-f711-4b76-b331-7563edebb79c
keywords:
- options files WDK Static Driver Verifier
- global options files WDK Static Driver Verifier
- local options files WDK Static Driver Verifier
ms.date: 04/02/2018
ms.localizationpriority: medium
---

# Global and Local Options Files


You can have multiple copies of the sdv-default.xml file on the system and you can edit the values in any copy of the file.

There are two types of options files:

-   The *global options file* is the sdv-default.xml file that SDV installs in the \\tools\\sdv\\data\\*&lt;drivermodel&gt;* subdirectories of the WDK. The values in these files apply to all SDV verifications, according to the driver model (WDM, WDF, NDIS, or Storport), except for verifications of drivers that have a local options file in their source directories.

-   A *local options file* is a copy of sdv-default.xml that is located in a driver's sources directory. The copy must have the sdv-default.xml file name. The local options file values apply only to verifications of that driver. When SDV finds a local options file in the driver's project directory, it uses that file and ignores the values in the global options file.

**Caution**   Do not move or delete the global options files from the \\tools\\sdv\\data\\*&lt;drivermodel&gt;* subdirectories and do not rename them. To create a local options file, make a copy of the global options file and place it in the driver's project directory. If the global options file is missing from the \\tools\\sdv\\data\\*&lt;drivermodel&gt;* subdirectories, SDV terminates the verification and displays the "Could not find Sdv-default.xml" error message.

 

 

 





