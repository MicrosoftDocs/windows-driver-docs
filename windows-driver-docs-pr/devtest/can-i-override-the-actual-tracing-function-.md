---
title: Can I override the actual tracing function
description: Can I override the actual tracing function
ms.date: 04/20/2017
---

# Can I override the actual tracing function?


Yes. You can do this by defining a custom WPP\_TRACE macro. You must define your version of this macro before you include the [trace message header (.tmh) file](trace-message-header-file.md) in the source file of your [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application.

For an example of how to define a custom WPP\_TRACE macro, see [Can I preserve the last-error code before TraceMessage is called?](can-i-preserve-the-last-error-code-before-tracemessage-is-called-.md).

 

 





