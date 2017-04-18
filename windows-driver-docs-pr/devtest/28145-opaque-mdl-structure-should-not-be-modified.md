---
title: C28145
description: Warning C28145 The opaque MDL structure should not be modified by a driver.
ms.assetid: efbd667b-fb0e-4a4d-bb6a-e8249c113a91
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28145


warning C28145: The opaque MDL structure should not be modified by a driver

The driver code is changing a member of an MDL structure.

The **MdlFlags** field is used as a proxy for all MDL fields. No fields should be modified, with the exception of MDL\_MAPPING\_CAN\_FAIL, which is used for drivers that need to be Microsoft Windows 98 or Windows NT (SP4) compatible, and MDL\_PAGES\_LOCKED, which is used for drivers that need to be Windows 2000 compatible.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28145%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




