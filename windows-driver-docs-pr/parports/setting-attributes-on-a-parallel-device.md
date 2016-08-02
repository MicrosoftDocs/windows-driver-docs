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


