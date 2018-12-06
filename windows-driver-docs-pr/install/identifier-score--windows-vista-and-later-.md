---
title: Identifier Score
description: Identifier Score
ms.assetid: c291205f-5152-419c-b6fa-0f720a5b628f
keywords:
- identifier score WDK device installations
- device identification strings WDK , identifier score driver ranking
- identifier-match-type score WDK device installations
- identifier-list-position score WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Identifier Score


A driver rank is formatted as 0x*SSGGTHHH*, where the value of 0x*SS*000000 is the [signature score](signature-score--windows-vista-and-later-.md), the value of 0x00*GG*0000 is the [feature score](feature-score--windows-vista-and-later-.md), and the value of 0x0000*THHH* is the identifier score.

The identifier score ranks a driver based on the type of match between a Plug and Play (PnP) [device identification string](device-identification-strings.md) that is reported by the bus driver of a device and a corresponding device identification string that is specified in an entry of an [**INF *Models* section**](inf-models-section.md) of a driver INF file.

The identifier score is a sum of an identifier-match-type score and an identifier-list-position score. The identifier-match-type score ranks a driver according to whether a device [hardware ID](hardware-ids.md) or a device [compatible ID](compatible-ids.md) matches a hardware ID or a compatible ID in an entry of an INF *Models* section. A match between a device hardware ID and a hardware ID in an entry of an INF Models section is called a hardware ID match. A match where at least one of the matching identifiers is a compatible ID is called a compatible ID match.

For a given identifier-match type, the identifier-list-position score ranks a driver according to the position of the matching identifier in the hardware ID list or the compatible ID list for a device and the position of the matching identifier in an entry of an INF *Models* section. Specifically, each device has an ordered list of hardware IDs and an ordered list of compatible IDs that are reported by the bus driver for the device. The identifiers are ordered in the list from the most specific to the most generic functionality. In addition, each INF *Models* section entry has one hardware ID and an optional list of compatible IDs that are listed in order of the most specific to the most generic functionality, as follows:

```cpp
device-description=install-section-name,hw-id,[compatible-id,...] ...
```

The first identifier in a device identifier list has an identifier-list-position score of 0x0000, the second identifier has an identifier-list-position score of 0x0001, and so on. Because an INF *Models* section entry only has one hardware ID, the identifier-list-position score of this hardware ID is always 0x0000.

The following lists the identifier scores for the four types of identifier-match types, where the value of 0x0000*T*000 is the identifier-match-type score and the value of 0x00000*HHH* is the identifier-list-position score:

-   A match between a device hardware ID and a hardware ID in an INF *Models* section entry is the best type of identifier match. A match of this type is called a *hardware ID match*.

    The identifier-match-type score is 0x00000000 and the value of 0x0000*HHH* is the identifier-list-position score of the matching hardware ID in the list of device hardware IDs.

    Identifier scores for this match type range from 0x00000000 through 0x00000FFF.

    For this type of match, the value 0x00000000 is the best identifier score and the value 0x00000FFF is the worst identifier score.

-   A match between a device hardware ID and a compatible ID in an INF *Models* section entry is the second best type of identifier match. A match of this type is called a *compatible ID match*.

    The identifier-match-type score is 0x00001000 and the value of 0x00000*HHH* equals the identifier-list-position score of the matching hardware ID in the list of device hardware IDs.

    Identifier scores for this match type range from 0x00001000 to 0x00001FFF.

    For this type of match, the value 0x00001000 is the best identifier score and the value 0x00001FFF is the worst identifier score.

-   A match between a device compatible ID and a hardware ID in an INF *Models* section entry is the third best type of identifier match. A match of this type is also known as a *compatible ID match*.

    The identifier-match-type score is 0x00002000 and the value of 0x00000*HHH* equals the identifier-list-position score of the matching compatible ID in the list of device compatible IDs.

    Identifier scores for this type of identifier match range from 0x00002000 to 0x00002FFF.

    For this type of match, the value 0x00002000 is the best identifier score and the value 0x00002FFF is the worst identifier score.

-   A match between a device compatible ID and a compatible ID in an INF *Models* section entry is the fourth best type of identifier match. A match of this type is also known as a *compatible ID match*. Identifier scores for this type of identifier match are in the range of 0x00003000 to 0x00003FFF, where:

    -   The identifier-match-type score is 0x3000.
    -   The value of 0x0*HHH* equals (*j* + *k*\*0x100), where *j* equals the identifier-list-position score of the matching device compatible ID and *k* equals the identifier-list-position score of the matching compatible ID in an INF *Models* section entry.

    For this type of match, the value 0x00003000 is the best identifier score and the value 0x00003FFF is the worst identifier score.

For more information about driver ranking, see [How Windows Ranks Drivers](how-setup-ranks-drivers--windows-vista-and-later-.md).

 

 





