---
title: Half-Duplex Mode Not Appropriate for Shipped Products
description: Half-Duplex Mode Not Appropriate for Shipped Products
ms.assetid: a586f340-5577-40ba-aa3e-11599f506223
---

# Half-Duplex Mode: Not Appropriate for Shipped Products


Half-duplex mode is intended for use only during the initial porting of a miniport from the SCSI port driver model to the Storport driver model. It restricts the port/miniport synchronization to that of SCSI port miniports, where a lock is used to synchronize the execution of its [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) and interrupt service routines. This results in spending more time at device IRQL (DIRQL), and reduces concurrency in I/O processing, which leads to lower performance. It is not compatible with the newer Storport interfaces and optimizations, and is therefore not appropriate for use in shipping products.

If you continue to ship a half-duplex miniport, you risk compatibility issues with future revisions of Storport.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Half-Duplex%20Mode:%20Not%20Appropriate%20for%20Shipped%20Products%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




