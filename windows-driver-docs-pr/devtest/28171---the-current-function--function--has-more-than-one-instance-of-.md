---
title: C28171
description: Warning C28171 The function has more than one instance of PAGED\_CODE or PAGED\_CODE\_LOCKED.
ms.assetid: 7a3740aa-53fc-4219-9606-edc0e9bd9879
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28171


warning C28171: The function has more than one instance of PAGED\_CODE or PAGED\_CODE\_LOCKED

This warning indicates that there is more than one instance of the PAGED\_CODE or PAGED\_CODE\_LOCKED macro in a function. This error is reported at the second or subsequent instances of the PAGED\_CODE or PAGED\_CODE\_LOCKED macro.

Functions in a paged section must have exactly one instance of the PAGED\_CODE or PAGED\_CODE\_LOCKED macro and the macro should appear at the beginning of the function between the first brace (**{**) and the first conditional statement, and after any declarations.

PREfast for Drivers uses these macros when **\#pragma alloc\_text** or **\#pragma code\_seg** is used to move a function into a pageable code section. The Code Analysis tool infers that a section is pageable when the section name begins with PAGE. For more information, see [Warning C28170](28170---the-current-function--function--has-been-declared-to-be-in-a-p.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28171%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




