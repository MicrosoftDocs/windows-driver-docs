---
title: C28131
description: Warning C28131 The DriverEntry routine should save a copy of the argument, not the pointer, because the I/O Manager frees the buffer.
ms.assetid: 9661f17e-a19a-4230-a848-8233f635db09
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28131


warning C28131: The DriverEntry routine should save a copy of the argument, not the pointer, because the I/O Manager frees the buffer

The driver's *DriverEntry* routine is saving a copy of the pointer to the buffer instead of saving a copy of the buffer. Because the buffer is freed when the *DriverEntry* routine returns, the pointer to the buffer will soon be invalid.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28131%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




