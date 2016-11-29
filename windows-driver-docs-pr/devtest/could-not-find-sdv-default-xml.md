---
title: Could not find Sdv-default.xml
description: Could not find Sdv-default.xml
ms.assetid: b8d928b0-8e6b-48de-98e2-554eb67c9a0b
---

# Could not find Sdv-default.xml


SDV reports this error when it cannot find the [global options file](global-and-local-options-files.md), sdv-default.xml, in the \\tools\\sdv\\data\\wdm or \\tools\\sdv\\data\\wdf subdirectories of the WDK. SDV creates the file in those directories when you install SDV and SDV requires that the files remain in those directories.

You can edit the values in the sdv-default.xml file in the \\tools\\sdv\\data\\wdm or \\tools\\sdv\\data\\wdf subdirectories, but you cannot move, delete, or rename them.

To create a custom options file for a particular driver (known as a [local options file](global-and-local-options-files.md)), copy the sdv-default.xml file from the \\tools\\sdv\\data\\wdm or \\tools\\sdv\\data\\wdf subdirectories to the driver's sources directory.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Could%20not%20find%20Sdv-default.xml%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




