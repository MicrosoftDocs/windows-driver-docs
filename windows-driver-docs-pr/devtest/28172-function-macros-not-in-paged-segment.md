---
title: C28172
description: Warning C28172 The function has PAGED\_CODE or PAGED\_CODE\_LOCKED but is not declared to be in a paged segment.
ms.assetid: c97bf9e8-583c-41ca-9c50-ac2af3dd5dc0
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28172


warning C28172: The function has PAGED\_CODE or PAGED\_CODE\_LOCKED but is not declared to be in a paged segment

A function that contains a PAGED\_CODE or PAGED\_CODE\_LOCKED macro has not been placed in paged memory by using **\#pragma alloc\_text** or **\#pragma code\_seg**. The Code Analysis tool infers that a section is pageable when the section name begins with PAGE. This error is reported at the line number corresponding to the first brace (**{**) in the function.

This error usually occurs when the function was intended to be paged, but one of the pragmas was omitted or misplaced, or when a function changed from paged to non-paged. For more information, see [Warning C28170](28170---the-current-function--function--has-been-declared-to-be-in-a-p.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28172%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




