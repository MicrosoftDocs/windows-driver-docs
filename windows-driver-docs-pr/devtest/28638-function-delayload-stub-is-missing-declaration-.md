---
title: C28638
description: Warning C28638 function delayload stub is missing a matching declaration.
ms.assetid: 25999552-6316-414b-972d-25797f477b15
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28638


warning C28638: function delayload stub is missing a matching declaration

Many delay-load stubs can be implemented without including the header file where the functions are declared. Over time, the function signatures might change without updating all the corresponding delay-load stubs. If the delay-load stubs have the wrong signature, it leads to an access violation.

Typically, the **\#include &lt;header.h&gt;** that contains the function prototype for the delay-load stub being implemented is missing. A common mistake is to include the public header file while implementing delay-load stubs for both public and private ordinals (consequently omitting the private ones). The fix is to include the appropriate header file for the delay-load stub being implemented.

 

 





