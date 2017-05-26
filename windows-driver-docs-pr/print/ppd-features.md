---
title: PPD Features
author: windows-driver-content
description: PPD Features
ms.assetid: ee78031a-2138-4d0c-ac8a-5328aa54d904
keywords:
- PPD files WDK Pscript
- non-PPD features WDK Pscript
- driver features WDK Pscript
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PPD Features


## <a href="" id="ddk-ppd-features-gg"></a>


PPD features are defined in the PPD file within **\*OpenUI**/**\*CloseUI** structure keyword pairs, and in certain PPD keywords that are treated similarly by the Pscript driver. Although **EnumFeatures** lists the **\*LeadingEdge** and **\*UseHWMargins** keywords, they are not defined within PPD **\*OpenUI**/**\*CloseUI** structure keyword pairs. Consequently, the **GetOptions** and **SetOptions** methods ignore these keywords if they appear in the feature list. The PPD feature/option keywords are case sensitive.

**SetOptions** handles certain PPD features in a special way:

-   If the printer's PPD file includes the **\*OutputOrder** feature keyword and **SetOptions** is called to change the option selection for this feature, then the **%PageOrder** driver feature setting will be changed to match the new output order. This is done in order to prevent the spooler from performing unnecessary page order simulation.

-   If the printer's PPD file includes the **\*OutputBin** feature keyword and **SetOptions** is called to change the option selection for this feature, and the change causes the current setting of the **%PageOrder** driver feature to be the opposite of the printer's page ordering, and **%MetafileSpooling** is "False", then **%MetafileSpooling** will be reset to "True".

-   When spooler EMF spooling is enabled, and **Collate** is set to "True" (this can be set either directly in the public portion of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure or by calling **SetOptions** on the PPD's **\*Collate** feature keyword), but the **Collate** feature is not currently available, and **%MetafileSpooling** is "False", then **%MetafileSpooling** will be reset to "True". This is done when all requested settings in the **SetOptions** call are applied.

-   If **Duplex** is set to simplex (this can be set either directly in the public portion of the DEVMODE structure or by calling **SetOptions** on the PPD's **\*Duplex** feature keyword), but **%PagePerSheet** is set to "Booklet", then **%PagePerSheet** will be changed to "2". This is done when all requested settings in the **SetOptions** call are applied.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PPD%20Features%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


