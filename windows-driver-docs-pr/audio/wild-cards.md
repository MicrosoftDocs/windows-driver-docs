---
title: Wild Cards
description: Wild Cards
ms.assetid: fc42fb2d-8df9-47d6-9034-c0588ee81c95
keywords: ["data-intersection handlers WDK audio , wild cards", "wild cards WDK audio", "data ranges WDK audio , wild cards"]
---

# Wild Cards


## <span id="wild_cards"></span><span id="WILD_CARDS"></span>


The header file Ks.h defines the following wild-card parameters for [**KS data ranges**](https://msdn.microsoft.com/library/windows/hardware/ff561658):

-   KSDATAFORMAT\_TYPE\_WILDCARD

-   KSDATAFORMAT\_SUBTYPE\_WILDCARD

-   KSDATAFORMAT\_SPECIFIER\_WILDCARD

The **MajorFormat**, **Subformat**, and **Specifier** members of the **DataRange** member of the [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure can be set to these values. A wild card matches any corresponding value to which it is being compared, including any data formats that might be defined in the future. System filters that can move data without understanding the data format are the primary users of wild cards. Adapter drivers should avoid specifying wild cards in the data ranges for their filter pins, but they should be prepared to accept wild cards in the data ranges for the client filter's pins.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Wild%20Cards%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




