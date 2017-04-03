---
title: C28638
description: Warning C28638 function delayload stub is missing a matching declaration.
ms.assetid: 25999552-6316-414b-972d-25797f477b15
---

# C28638


warning C28638: function delayload stub is missing a matching declaration

Many delay-load stubs can be implemented without including the header file where the functions are declared. Over time, the function signatures might change without updating all the corresponding delay-load stubs. If the delay-load stubs have the wrong signature, it leads to an access violation.

Typically, the **\#include &lt;header.h&gt;** that contains the function prototype for the delay-load stub being implemented is missing. A common mistake is to include the public header file while implementing delay-load stubs for both public and private ordinals (consequently omitting the private ones). The fix is to include the appropriate header file for the delay-load stub being implemented.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28638%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




