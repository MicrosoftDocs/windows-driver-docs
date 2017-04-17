---
title: Storing and Transferring Audio Data
author: windows-driver-content
description: Storing and Transferring Audio Data
ms.assetid: c8d0af2f-1c3d-49d5-96ca-de1703f85448
---

# Storing and Transferring Audio Data


## <a href="" id="ddk-storing-and-transferring-audio-data-si"></a>


Some WIA drivers for Microsoft Windows Me and Windows XP used the following three WIA properties to store audio data:

[**WIA\_IPC\_AUDIO\_AVAILABLE**](https://msdn.microsoft.com/library/windows/hardware/ff552530)

[**WIA\_IPC\_AUDIO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552534)

[**WIA\_IPC\_AUDIO\_DATA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff552538)

These properties are obsolete and should no longer be used.

Audio for a picture item should be represented as an attachment. This provides easy access to all audio formats that the WIA minidriver supports. Audio content is transferred in the same way that other items in the WIA item tree are transferred.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Storing%20and%20Transferring%20Audio%20Data%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


