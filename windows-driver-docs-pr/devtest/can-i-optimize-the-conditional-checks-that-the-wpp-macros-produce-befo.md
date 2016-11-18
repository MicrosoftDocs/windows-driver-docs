---
title: Can I optimize the conditional checks that the WPP macros produce before the tracing
description: Can I optimize the conditional checks that the WPP macros produce before the tracing
ms.assetid: 0d0ad0de-561f-4480-be91-2304242fee91
---

# Can I optimize the conditional checks that the WPP macros produce before the tracing?


You can remove the conditional check for WPP\_INIT\_TRACING so that it is not called through the WPP macros. You can do this only if WPP\_INIT\_TRACING is called before any attempt to trace is made within the source code of your [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application.

**Important**  You should not remove this check if tracing is made in your object constructors or macros. Otherwise, access violations could occur in your trace provider.

 

Before you include the [trace message header (.tmh) file](trace-message-header-file.md) in your source code, add the following definition to disable the conditional check for WPP\_INIT\_TRACING:

```
#define WPP_CHECK_INIT
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Can%20I%20optimize%20the%20conditional%20checks%20that%20the%20WPP%20macros%20produce%20before%20the%20tracing?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




