---
title: I/O Status Blocks
author: windows-driver-content
description: I/O Status Blocks
ms.assetid: 59147bd1-6cd7-4fbe-b7bc-52e09ab88576
keywords: ["IRPs WDK kernel , I/O status blocks", "I/O status blocks WDK kernel", "status blocks WDK kernel", "IO_STATUS_BLOCK structure", "status information WDK IRPs", "IRPs WDK kernel , status information"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# I/O Status Blocks


## <a href="" id="ddk-i-o-status-blocks-kg"></a>


An I/O status block, which consists of an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure, is a part of each [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694). An I/O status block serves two purposes:

-   It provides a higher-level driver's [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine a way of determining whether the service worked when the IRP is completed.

-   It provides more information about why the service either worked or did not work.

Upon completion of a IRP, the **Status** field indicates whether the drivers that processed the IRP actually satisfied the request or failed the IRP with an error status. The **Information** field supplies the caller with more information about what actually occurred. For example, it contains the number of bytes actually transferred after a read or write operation.

For more information, see [Setting the I/O Status Block in an IRP](processing-irps-in-a-lowest-level-driver.md#ddk-setting-the-i-o-status-block-in-an-irp-kg).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20I/O%20Status%20Blocks%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


