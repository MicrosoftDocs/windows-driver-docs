---
title: WIA_IPS_DESKEW_X and WIA_IPS_DESKEW_Y Properties
description: WIA_IPS_DESKEW_X and WIA_IPS_DESKEW_Y Properties
ms.date: 04/20/2017
---

# WIA\_IPS\_DESKEW\_X and WIA\_IPS\_DESKEW\_Y Properties





The [**WIA\_IPS\_DESKEW\_X**](./wia-ips-deskew-x.md) and [**WIA\_IPS\_DESKEW\_Y**](./wia-ips-deskew-y.md) properties are implemented by the scanner driver if the driver supports deskewing. These two properties describe where the two upper corners of the skewed image are located within the bounding rectangle defined by [**WIA\_IPS\_XPOS**](./wia-ips-xpos.md), [**WIA\_IPS\_YPOS**](./wia-ips-ypos.md), [**WIA\_IPS\_XEXTENT**](./wia-ips-xextent.md), and [**WIA\_IPS\_YEXTENT**](./wia-ips-yextent.md) properties.

The valid values for WIA\_IPS\_DESKEW\_X must be between 0 and (WIA\_IPS\_XEXTENT − 1). The valid values for WIA\_IPS\_DESKEW\_Y must be between 0 and (WIA\_IPS\_YEXTENT − 1). A value of 0 for both properties means that no skew correction should be performed.

Only rectangular scanning areas are supported, so these two values uniquely define the position of the image to be deskewed. A deskew angle can be calculated from these two values.

 

