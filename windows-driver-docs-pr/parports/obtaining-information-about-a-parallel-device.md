---
title: Obtaining Information about a Parallel Device
author: windows-driver-content
description: Obtaining Information about a Parallel Device
MS-HAID:
- 'vspd\_8cd04c2c-ffe5-4cfc-85e7-67edbef79078.xml'
- 'parports.obtaining\_information\_about\_a\_parallel\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a891718a-9e2c-4823-a0b9-5cbe770c3f85
keywords: ["parallel devices WDK , obtaining information"]
---

# Obtaining Information about a Parallel Device


## <a href="" id="ddk-obtaining-information-about-a-parallel-device-kg"></a>


In addition to [connecting to a parallel device](connecting-to-a-parallel-device.md), a client can use the following device control requests to obtain additional information about a parallel device:

[**IOCTL\_IEEE1284\_GET\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff543975)

[**IOCTL\_PAR\_GET\_DEFAULT\_MODES**](https://msdn.microsoft.com/library/windows/hardware/ff544061)

[**IOCTL\_PAR\_GET\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff544067)

[**IOCTL\_PAR\_IS\_PORT\_FREE**](https://msdn.microsoft.com/library/windows/hardware/ff544073)

[**IOCTL\_PAR\_QUERY\_DEVICE\_ID\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff544080)

[**IOCTL\_PAR\_QUERY\_DEVICE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff544076)

[**IOCTL\_PAR\_QUERY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544086)

[**IOCTL\_PAR\_QUERY\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff544091)

[**IOCTL\_PAR\_QUERY\_RAW\_DEVICE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff544100)

[**IOCTL\_SERIAL\_GET\_TIMEOUTS**](https://msdn.microsoft.com/library/windows/hardware/ff544120)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Obtaining%20Information%20about%20a%20Parallel%20Device%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


