---
title: Discover whether the network device radio is turned on
description: Discover whether the network device radio is turned on
ms.assetid: deded77d-8810-498c-a5ae-44885189c061
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Discover whether the network device radio is turned on


If the user starts the mobile broadband app directly from its tile, the mobile broadband device might be turned off. This will usually happen if the device entered a power-saving mode or the end user turned on airplane mode (which disables the network devices). If this is the case, getting the [**CurrentRadioState**](https://msdn.microsoft.com/library/windows/apps/hh770613) property of the [**MobileBroadbandDeviceInformation**](https://msdn.microsoft.com/library/windows/apps/br207361) object for the network device in question will return [**MobileBroadbandRadioState**](https://msdn.microsoft.com/library/windows/apps/hh758385).**Off**. (Alternatively, if the radio is turned on, the **CurrentRadioState** property will return **MobileBroadbandRadioState**.**On**.)

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






