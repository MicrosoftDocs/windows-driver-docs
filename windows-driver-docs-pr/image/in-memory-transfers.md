---
title: In-Memory Transfers
author: windows-driver-content
description: In-Memory Transfers
ms.assetid: 90238354-e47c-41c7-bb6b-6337f39f63f0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# In-Memory Transfers


## <a href="" id="ddk-in-memory-transfers-si"></a>


**Note**  In-memory transfers are for operating systems prior to Windows Vista.

 

An *in-memory data transfer* is a transfer of imaging data from the WIA minidriver into a memory buffer that the WIA service has allocated. The WIA application that initiates the data transfer always determines the size of the data transfer buffer. The size of this data transfer buffer cannot be less than the value that the minidriver defines in the [**WIA\_IPA\_BUFFER\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551527) property.

After the WIA application determines the buffer size, it requests the WIA service to begin the data transfer. The WIA service then allocates the memory buffer of the requested size (according to the constraints that the preceding paragraph mentioned) and requests that the WIA minidriver begin the data transfer and place the data into the supplied buffer. The WIA minidriver fills the buffer with data and returns it to the WIA service, which then returns the data to the requesting WIA application. This process is repeated until there is no more data to transfer.

The following diagram illustrates a memory transfer of an image.

![diagram illustrating an image memory transfer](images/wia-imagedatamem.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20In-Memory%20Transfers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


