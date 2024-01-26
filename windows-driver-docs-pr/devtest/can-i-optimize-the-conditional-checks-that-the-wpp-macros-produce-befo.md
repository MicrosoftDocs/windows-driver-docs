---
title: Optimizing Conditional Checks that the WPP Macros Produce Before Tracing
description: Can I optimize the conditional checks that the WPP macros produce before the tracing
ms.date: 04/20/2017
---

# Can I optimize the conditional checks that the WPP macros produce before the tracing?


You can remove the conditional check for WPP\_INIT\_TRACING so that it is not called through the WPP macros. You can do this only if WPP\_INIT\_TRACING is called before any attempt to trace is made within the source code of your [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application.

**Important**  You should not remove this check if tracing is made in your object constructors or macros. Otherwise, access violations could occur in your trace provider.


Before you include the [trace message header (.tmh) file](trace-message-header-file.md) in your source code, add the following definition to disable the conditional check for WPP\_INIT\_TRACING:

```
#define WPP_CHECK_INIT
```

