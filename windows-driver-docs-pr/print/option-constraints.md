---
title: Option Constraints
author: windows-driver-content
description: Option Constraints
ms.assetid: dc399715-c238-4a6e-8ce0-3204aa0cca68
keywords:
- constraints WDK Unidrv
- printer options WDK Unidrv , constraints
- simultaneous printer options WDK Unidrv
- combining printer options WDK Unidrv
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Option Constraints


## <a href="" id="ddk-option-constraints-gg"></a>


It is sometimes necessary to constrain the ability of users to install or select certain printer options associated with printer features. The following types of option constraints can be specified:

-   You can constrain an option so that it cannot be selected if a conflicting option is already selected. These constraints are called [selection constraints](selection-constraints.md).

-   You can constrain an installable option so that it cannot be installed if a conflicting installable option is already installed. These constraints are called [installation constraints](installation-constraints.md).

-   You can constrain an option so that it cannot be selected if a conflicting installable option is already installed, or so that it cannot be selected if a required installable option is not installed. These constraints are called [constraints between selections and installations](constraints-between-selections-and-installations.md).

The driver's user interface code enforces constraints when the user chooses the **OK** button on the printer's property sheet dialog box. If invalid combinations of options have been selected, the user is given the choice of either correcting the conflicts by modifying the property sheet page or letting the driver attempt to make corrections automatically, based on [feature conflict priority](feature-conflict-priority.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Option%20Constraints%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


