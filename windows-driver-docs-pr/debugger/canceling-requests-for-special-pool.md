---
title: Canceling Requests for Special Pool
description: Canceling Requests for Special Pool
ms.assetid: fb18cb15-33ee-4e6d-856e-70c4ffbf8383
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Canceling Requests for Special Pool


## <span id="ddk_canceling_requests_for_special_pool_dtools"></span><span id="DDK_CANCELING_REQUESTS_FOR_SPECIAL_POOL_DTOOLS"></span>


You can use GFlags to cancel a request for allocation from the special pool if the request was made by using GFlags. You cannot use GFlags to cancel a request for special pool that was made by using Driver Verifier.

In Windows Vista and later versions of Windows, you can also use the command line to cancel special pool requests. For information, see [**GFlags Commands**](gflags-commands.md).

**To cancel requests for special pool**

1.  Select the System Registry tab or the Kernel Flags tab.

    On Windows Vista and later versions of Windows, this option is available on both tabs. On earlier versions of Windows, it is available only on the **System Registry** tab.

2.  Delete the text or hexadecimal value from the **Kernel Special Pool Tag** box.

3.  Click **Apply**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Canceling%20Requests%20for%20Special%20Pool%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




