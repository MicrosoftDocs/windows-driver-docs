---
title: Using IRP Priority Hints
author: windows-driver-content
description: Using IRP Priority Hints
ms.assetid: c34afff2-32f2-451b-ab16-ff048d5c3204
---

# Using IRP Priority Hints


An *IRP priority hint* is an [**IO\_PRIORITY\_HINT**](https://msdn.microsoft.com/library/windows/hardware/ff550594) value that is associated with an IRP. IRP priority hints provide a simple hinting mechanism to indicate the relative importance of IRPs. A driver can use the priority hint for an IRP when choosing the order that the IRP is processed. IRP priority hints are available on Windows Vista and later operating systems.

For more information about IRP priority hints, see the [I/O Prioritization in Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=67877) white paper on the Windows Hardware Developer Central (WHDC) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20IRP%20Priority%20Hints%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


