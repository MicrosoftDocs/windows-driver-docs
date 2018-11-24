---
title: Ranking a Biometric Driver on Windows Update
description: Ranking a Biometric Driver on Windows Update
ms.assetid: fc8634ab-0ecd-4390-9834-825f60fe68ce
keywords:
- biometric drivers WDK , ranking on Windows Update
- ranking biometric drivers WDK biometric
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Ranking a Biometric Driver on Windows Update


Vendors who provide both legacy biometric and WBDI drivers can use the driver Feature Score to control which driver is installed from Windows Update.

Vendors who choose to write a single driver that supports legacy and WBDI should be aware that to work properly with the Windows Biometric Framework, the driver must support exclusive access. When exclusive access is disabled, the driver functions as a legacy driver. To review how to set the Exclusive value in the registry, see [Installing a Biometric Driver](installing-a-biometric-driver.md).

In addition, a biometric driver operating in legacy mode should not assign the GUID\_DEVINTERFACE\_BIOMETRIC\_READER device interface. Assigning this device interface causes the Windows Biometric Service to recognize the driver.

If Feature Score is set appropriately, the WBDI driver will only be installed on systems that do not have a biometric driver already in place.

If a customer decides to opt into a legacy stack, the customer can install a higher-ranked legacy driver over the WBDI driver.

### <span id="how_feature_score_works"></span><span id="HOW_FEATURE_SCORE_WORKS"></span>How Feature Score Works

Feature Score is represented in the third and fourth digit of the overall driver rank. For instance, *GG* is the feature score from the following driver rank:

```cpp
0x00GG0000 
```

Lower feature numbers indicates better matches. The default feature score is 0xFF, which indicates that there is no preference based on the features of a driver.

Microsoft recommends a feature score of 0xa0 for legacy biometric drivers. The feature score should never be set to 0x00, in case there is a need to override it later.

The feature score for a driver is set by an INF FeatureScore directive in the [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) for the device.

For example, the following code sets the feature score of a driver to 0x20:

```cpp
[DDInstallSectionName]
. . .
FeatureScore=x20
```

For more information about how to set the feature score on drivers, see [Feature Score (Windows Vista)](http://go.microsoft.com/fwlink/p/?linkid=132806).

 

 





