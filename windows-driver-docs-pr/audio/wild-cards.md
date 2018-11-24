---
title: Wild Cards
description: Wild Cards
ms.assetid: fc42fb2d-8df9-47d6-9034-c0588ee81c95
keywords:
- data-intersection handlers WDK audio , wild cards
- wild cards WDK audio
- data ranges WDK audio , wild cards
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Wild Cards


## <span id="wild_cards"></span><span id="WILD_CARDS"></span>


The header file Ks.h defines the following wild-card parameters for [**KS data ranges**](https://msdn.microsoft.com/library/windows/hardware/ff561658):

-   KSDATAFORMAT\_TYPE\_WILDCARD

-   KSDATAFORMAT\_SUBTYPE\_WILDCARD

-   KSDATAFORMAT\_SPECIFIER\_WILDCARD

The **MajorFormat**, **Subformat**, and **Specifier** members of the **DataRange** member of the [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure can be set to these values. A wild card matches any corresponding value to which it is being compared, including any data formats that might be defined in the future. System filters that can move data without understanding the data format are the primary users of wild cards. Adapter drivers should avoid specifying wild cards in the data ranges for their filter pins, but they should be prepared to accept wild cards in the data ranges for the client filter's pins.

 

 




