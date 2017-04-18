---
title: Global and Local Options Files
description: Global and Local Options Files
ms.assetid: 9b367e9f-f711-4b76-b331-7563edebb79c
keywords: ["options files WDK Static Driver Verifier", "global options files WDK Static Driver Verifier", "local options files WDK Static Driver Verifier"]
---

# Global and Local Options Files


You can have multiple copies of the sdv-default.xml file on the system and you can edit the values in any copy of the file.

There are two types of options files:

-   The *global options file* is the sdv-default.xml file that SDV installs in the \\tools\\sdv\\data\\*&lt;drivermodel&gt;* subdirectories of the WDK. The values in these files apply to all SDV verifications, according to the driver model (WDM, WDF, NDIS, or Storport), except for verifications of drivers that have a local options file in their source directories.

-   A *local options file* is a copy of sdv-default.xml that is located in a driver's sources directory. The copy must have the sdv-default.xml file name. The local options file values apply only to verifications of that driver. When SDV finds a local options file in the driver's project directory, it uses that file and ignores the values in the global options file.

**Caution**   Do not move or delete the global options files from the \\tools\\sdv\\data\\*&lt;drivermodel&gt;* subdirectories and do not rename them. To create a local options file, make a copy of the global options file and place it in the driver's project directory. If the global options file is missing from the \\tools\\sdv\\data\\*&lt;drivermodel&gt;* subdirectories, SDV terminates the verification and displays the [Could not find Sdv-default.xml](could-not-find-sdv-default-xml.md) error message.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Global%20and%20Local%20Options%20Files%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




