---
title: NFC client driver power management requirements
author: windows-driver-content
ms.assetid: FBA0821B-859F-4A44-998E-E00162FBD265
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
description: 
---

# NFC client driver power management requirements


The NFC client driver must implement D0 and D3 power handling callbacks as follows in order to meet the requirements for NFP devices on connected standby platforms:

-   The NFC client driver must ensure when the driver is going from the D3 -&gt; D0 state that it can resume in less than 100ms. This is to ensure that NFC operations can take place immediately on switching the screen ON.

-   The NFC client driver must also ensure the power consumption is less than 1mW when in the D3 state. This is to ensure there is no significant power consumption when in screen OFF.

To meet these goals, the following are recommended for the NFC client drivers:

-   For NFC controllers that can meet these requirements by going to power-removed or hard powered down, we recommend the NFC client driver re-initialize the chipset during D0 -&gt; D3 and then from D3 -&gt; D0 transitions.

-   For NFC controllers that require patch download due to absence of non-volatile (that is, RAM based) memory , we recommend the NFC client driver enable and disable standby mode during D0 -&gt; D3 and D3 -&gt; D0 transitions, respectively. A full initialization is done (HostActionStart) when going from D3Final -&gt; D0 and deinitialization (HostActionStop) is done when going from D0 -&gt; D3Final.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFC%20client%20driver%20power%20management%20requirements%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




