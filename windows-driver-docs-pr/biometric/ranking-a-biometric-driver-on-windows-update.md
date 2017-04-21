---
title: Ranking a Biometric Driver on Windows Update
description: Ranking a Biometric Driver on Windows Update
ms.assetid: fc8634ab-0ecd-4390-9834-825f60fe68ce
keywords:
- biometric drivers WDK , ranking on Windows Update
- ranking biometric drivers WDK biometric
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Ranking a Biometric Driver on Windows Update


Vendors who provide both legacy biometric and WBDI drivers can use the driver Feature Score to control which driver is installed from Windows Update.

Vendors who choose to write a single driver that supports legacy and WBDI should be aware that to work properly with the Windows Biometric Framework, the driver must support exclusive access. When exclusive access is disabled, the driver functions as a legacy driver. To review how to set the Exclusive value in the registry, see [Installing a Biometric Driver](installing-a-biometric-driver.md).

In addition, a biometric driver operating in legacy mode should not assign the GUID\_DEVINTERFACE\_BIOMETRIC\_READER device interface. Assigning this device interface causes the Windows Biometric Service to recognize the driver.

If Feature Score is set appropriately, the WBDI driver will only be installed on systems that do not have a biometric driver already in place.

If a customer decides to opt into a legacy stack, the customer can install a higher-ranked legacy driver over the WBDI driver.

### <span id="how_feature_score_works"></span><span id="HOW_FEATURE_SCORE_WORKS"></span>How Feature Score Works

Feature Score is represented in the third and fourth digit of the overall driver rank. For instance, *GG* is the feature score from the following driver rank:

```
0x00GG0000 
```

Lower feature numbers indicates better matches. The default feature score is 0xFF, which indicates that there is no preference based on the features of a driver.

Microsoft recommends a feature score of 0xa0 for legacy biometric drivers. The feature score should never be set to 0x00, in case there is a need to override it later.

The feature score for a driver is set by an INF FeatureScore directive in the [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) for the device.

For example, the following code sets the feature score of a driver to 0x20:

```
[DDInstallSectionName]
. . .
FeatureScore=x20
```

For more information about how to set the feature score on drivers, see [Feature Score (Windows Vista)](http://go.microsoft.com/fwlink/p/?linkid=132806).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Ranking%20a%20Biometric%20Driver%20on%20Windows%20Update%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




