---
title: Setting Attributes on a Parallel Device
author: windows-driver-content
description: Setting Attributes on a Parallel Device
MS-HAID:
- 'vspd\_e8d2cd3a-f9e8-48f5-9bde-e71ab3bfdb5c.xml'
- 'parports.setting\_attributes\_on\_a\_parallel\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 10df9a1b-99ec-46b1-b515-10fb20fe2aed
keywords: ["parallel devices WDK , attributes", "attributes WDK parallel devices"]
---

# Setting Attributes on a Parallel Device


## <a href="" id="ddk-setting-attributes-on-a-parallel-device-kg"></a>


A client uses following device control requests to set the indicated operations of a parallel device:

-   [**IOCTL\_PAR\_SET\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544103) initializes a parallel device.

-   [**IOCTL\_SERIAL\_SET\_TIMEOUTS**](https://msdn.microsoft.com/library/windows/hardware/ff544126) sets time outs for a parallel device.

-   [**IOCTL\_PAR\_SET\_READ\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff544107) sets an ECP or EPP read address (channel) for a parallel device.

-   [**IOCTL\_PAR\_SET\_WRITE\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff544115) sets an ECP or EPP write address (channel) for a parallel device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Setting%20Attributes%20on%20a%20Parallel%20Device%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


