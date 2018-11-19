---
title: NFC client driver power management requirements
ms.assetid: FBA0821B-859F-4A44-998E-E00162FBD265
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
description: Information about meeting the requirements for NFP devices on connected standby. platforms
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFC client driver power management requirements


The NFC client driver must implement D0 and D3 power handling callbacks as follows in order to meet the requirements for NFP devices on connected standby platforms:

-   The NFC client driver must ensure when the driver is going from the D3 -&gt; D0 state that it can resume in less than 100ms. This is to ensure that NFC operations can take place immediately on switching the screen ON.

-   The NFC client driver must also ensure the power consumption is less than 1mW when in the D3 state. This is to ensure there is no significant power consumption when in screen OFF.

To meet these goals, the following are recommended for the NFC client drivers:

-   For NFC controllers that can meet these requirements by going to power-removed or hard powered down, we recommend the NFC client driver re-initialize the chipset during D0 -&gt; D3 and then from D3 -&gt; D0 transitions.

-   For NFC controllers that require patch download due to absence of non-volatile (that is, RAM based) memory , we recommend the NFC client driver enable and disable standby mode during D0 -&gt; D3 and D3 -&gt; D0 transitions, respectively. A full initialization is done (HostActionStart) when going from D3Final -&gt; D0 and deinitialization (HostActionStop) is done when going from D0 -&gt; D3Final.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  
