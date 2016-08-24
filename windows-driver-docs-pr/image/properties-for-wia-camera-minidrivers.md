---
title: Properties for WIA Camera Minidrivers
author: windows-driver-content
description: Properties for WIA Camera Minidrivers
MS-HAID:
- 'WIA\_arch\_b9ccab2f-89b6-4bb2-aabb-1c38aecdd207.xml'
- 'image.properties\_for\_wia\_camera\_minidrivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3a5e61d7-1ca8-44a8-b24a-7a5929d424a5
---

# Properties for WIA Camera Minidrivers


## <a href="" id="ddk-properties-for-wia-camera-minidrivers-si"></a>


The following is the complete list of all WIA properties unique to WIA camera minidrivers.

### Required Properties on Camera Root Items (Microsoft Windows XP and Windows Me)

A WIA minidriver supplies the following property:

[**WIA\_DPC\_PICTURES\_TAKEN**](https://msdn.microsoft.com/library/windows/hardware/ff550431)

### Optional Properties on Camera Root Items (Windows XP and Windows Me)

A WIA minidriver supplies the following properties:

[**WIA\_DPC\_ARTIST**](https://msdn.microsoft.com/library/windows/hardware/ff550313)

[**WIA\_DPC\_BATTERY\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff550317)

[**WIA\_DPC\_BURST\_INTERVAL**](https://msdn.microsoft.com/library/windows/hardware/ff550322)

[**WIA\_DPC\_BURST\_NUMBER**](https://msdn.microsoft.com/library/windows/hardware/ff550327)

[**WIA\_DPC\_CAPTURE\_DELAY**](https://msdn.microsoft.com/library/windows/hardware/ff550328)

[**WIA\_DPC\_CAPTURE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff550334)

[**WIA\_DPC\_COMPRESSION\_SETTING**](https://msdn.microsoft.com/library/windows/hardware/ff550337)

[**WIA\_DPC\_CONTRAST**](https://msdn.microsoft.com/library/windows/hardware/ff550343)

[**WIA\_DPC\_COPYRIGHT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff550348)

[**WIA\_DPC\_DIGITAL\_ZOOM**](https://msdn.microsoft.com/library/windows/hardware/ff550353)

[**WIA\_DPC\_DIMENSION**](https://msdn.microsoft.com/library/windows/hardware/ff550357)

[**WIA\_DPC\_EFFECT\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff550360)

[**WIA\_DPC\_EXPOSURE\_COMP**](https://msdn.microsoft.com/library/windows/hardware/ff550364)

[**WIA\_DPC\_EXPOSURE\_INDEX**](https://msdn.microsoft.com/library/windows/hardware/ff550367)

[**WIA\_DPC\_EXPOSURE\_METERING\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff550371)

[**WIA\_DPC\_EXPOSURE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff550379)

[**WIA\_DPC\_EXPOSURE\_TIME**](https://msdn.microsoft.com/library/windows/hardware/ff550382)

[**WIA\_DPC\_FLASH\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff550384)

[**WIA\_DPC\_FNUMBER**](https://msdn.microsoft.com/library/windows/hardware/ff550390)

[**WIA\_DPC\_FOCAL\_LENGTH**](https://msdn.microsoft.com/library/windows/hardware/ff550393)

[**WIA\_DPC\_FOCUS\_DISTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff550400)

[**WIA\_DPC\_FOCUS\_MANUAL\_DIST**](https://msdn.microsoft.com/library/windows/hardware/ff550403)

[**WIA\_DPC\_FOCUS\_METERING**](https://msdn.microsoft.com/library/windows/hardware/ff550410)

[**WIA\_DPC\_FOCUS\_METERING\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff550414)

[**WIA\_DPC\_FOCUS\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff550416)

[**WIA\_DPC\_PAN\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/ff550424)

[**WIA\_DPC\_PICT\_HEIGHT**](https://msdn.microsoft.com/library/windows/hardware/ff550437)

[**WIA\_DPC\_PICT\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff550445)

[**WIA\_DPC\_PICTURES\_REMAINING**](https://msdn.microsoft.com/library/windows/hardware/ff550427)

[**WIA\_DPC\_POWER\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff550448)

[**WIA\_DPC\_RGB\_GAIN**](https://msdn.microsoft.com/library/windows/hardware/ff550454)

[**WIA\_DPC\_SHARPNESS**](https://msdn.microsoft.com/library/windows/hardware/ff550460)

[**WIA\_DPC\_THUMB\_HEIGHT**](https://msdn.microsoft.com/library/windows/hardware/ff550465)

[**WIA\_DPC\_THUMB\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff550470)

[**WIA\_DPC\_TILT\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/ff550475)

[**WIA\_DPC\_TIMELAPSE\_INTERVAL**](https://msdn.microsoft.com/library/windows/hardware/ff550479)

[**WIA\_DPC\_TIMELAPSE\_NUMBER**](https://msdn.microsoft.com/library/windows/hardware/ff550483)

[**WIA\_DPC\_TIMER\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff550489)

[**WIA\_DPC\_TIMER\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/ff550499)

[**WIA\_DPC\_UPLOAD\_URL**](https://msdn.microsoft.com/library/windows/hardware/ff550503)

[**WIA\_DPC\_WHITE\_BALANCE**](https://msdn.microsoft.com/library/windows/hardware/ff550507)

[**WIA\_DPC\_ZOOM\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/ff550511)

### Required Properties on Camera Child Items Able to Transfer Data

A WIA minidriver supplies the following properties:

[**WIA\_IPC\_THUMBNAIL**](https://msdn.microsoft.com/library/windows/hardware/ff552550)

[**WIA\_IPC\_THUMBNAIL\_HEIGHT**](https://msdn.microsoft.com/library/windows/hardware/ff552552)

[**WIA\_IPC\_THUMBNAIL\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff552558)

### Optional Properties on Camera Child Items Able to Transfer Data

A WIA minidriver supplies the following properties:

[**WIA\_IPC\_AUDIO\_AVAILABLE**](https://msdn.microsoft.com/library/windows/hardware/ff552530)

[**WIA\_IPC\_AUDIO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552534)

[**WIA\_IPC\_AUDIO\_DATA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff552538)

[**WIA\_IPC\_NUM\_PICT\_PER\_ROW**](https://msdn.microsoft.com/library/windows/hardware/ff552542)

[**WIA\_IPC\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/ff552548)

[**WIA\_IPC\_TIMEDELAY**](https://msdn.microsoft.com/library/windows/hardware/ff552560)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Properties%20for%20WIA%20Camera%20Minidrivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


