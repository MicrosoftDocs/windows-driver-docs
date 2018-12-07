---
title: WIA_IPS_DESKEW_X and WIA_IPS_DESKEW_Y Properties
description: WIA_IPS_DESKEW_X and WIA_IPS_DESKEW_Y Properties
ms.assetid: 748b08f7-e838-4df8-abcb-4ff1cdd20f7e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_DESKEW\_X and WIA\_IPS\_DESKEW\_Y Properties





The [**WIA\_IPS\_DESKEW\_X**](https://msdn.microsoft.com/library/windows/hardware/ff552581) and [**WIA\_IPS\_DESKEW\_Y**](https://msdn.microsoft.com/library/windows/hardware/ff552587) properties are implemented by the scanner driver if the driver supports deskewing. These two properties describe where the two upper corners of the skewed image are located within the bounding rectangle defined by [**WIA\_IPS\_XPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552663), [**WIA\_IPS\_YPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552671), [**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661), and [**WIA\_IPS\_YEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552669) properties.

The valid values for WIA\_IPS\_DESKEW\_X must be between 0 and (WIA\_IPS\_XEXTENT − 1). The valid values for WIA\_IPS\_DESKEW\_Y must be between 0 and (WIA\_IPS\_YEXTENT − 1). A value of 0 for both properties means that no skew correction should be performed.

Only rectangular scanning areas are supported, so these two values uniquely define the position of the image to be deskewed. A deskew angle can be calculated from these two values.

 

 




