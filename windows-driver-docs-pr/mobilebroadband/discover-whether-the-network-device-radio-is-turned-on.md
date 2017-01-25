---
title: Discover whether the network device radio is turned on
description: Discover whether the network device radio is turned on
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: deded77d-8810-498c-a5ae-44885189c061
---

# Discover whether the network device radio is turned on


If the user starts the mobile broadband app directly from its tile, the mobile broadband device might be turned off. This will usually happen if the device entered a power-saving mode or the end user turned on airplane mode (which disables the network devices). If this is the case, getting the [**CurrentRadioState**](https://msdn.microsoft.com/library/windows/apps/hh770613) property of the [**MobileBroadbandDeviceInformation**](https://msdn.microsoft.com/library/windows/apps/br207361) object for the network device in question will return [**MobileBroadbandRadioState**](https://msdn.microsoft.com/library/windows/apps/hh758385).**Off**. (Alternatively, if the radio is turned on, the **CurrentRadioState** property will return **MobileBroadbandRadioState**.**On**.)

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Discover%20whether%20the%20network%20device%20radio%20is%20turned%20on%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





