---
title: Canceling Requests for Special Pool
description: Canceling Requests for Special Pool
ms.assetid: fb18cb15-33ee-4e6d-856e-70c4ffbf8383
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





