---
title: Initializing a Subunit Driver and Establishing Pin Connections
description: Initializing a Subunit Driver and Establishing Pin Connections
ms.assetid: 08c7a604-3aa5-4ee0-be55-b58bea0e6df1
keywords:
- Avc.sys function driver WDK , initializing subunit drivers
- Avc.sys function driver WDK , pin connections
- pin connections WDK AV/C
- connections WDK AV/C
- initializing AV/C subunit drivers
- pin counts WDK AV/C
- formats WDK AV/C
- data formats WDK AVStream
- AVCCONNECTINFO
- external plug connections WDK AV/C
- KSPIN_DESCRIPTOR
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a Subunit Driver and Establishing Pin Connections


To initialize a subunit driver and establish pin connections, complete the following procedure:

1.  Submit an [**AVC\_FUNCTION\_GET\_PIN\_COUNT**](https://msdn.microsoft.com/library/windows/hardware/ff554158) request. Use the resulting pin count in the subsequent functions in this procedure to indicate the pin (offsets range from 0 to PinCount-1).

2.  For each pin, submit an [**AVC\_FUNCTION\_GET\_PIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff554160) request. To complete the kernel streaming (KS) filter's definition, use the returned [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) member of the [**AVC\_PIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff554185) structure that was passed with the **AVC\_FUNCTION\_GET\_PIN\_DESCRIPTOR** request. *Avc.sys* fills in the **MediumsCount**, **Mediums**, **DataFlow**, and **Communication** members of KSPIN\_DESCRIPTOR. The subunit driver is permitted to copy the KSPIN\_DESCRIPTOR structure and override any of the members, although it is recommended that it leave the medium list intact (the list might contain GUIDs synthesized for permanent subunit plug connections).

    The pointers in the KSPIN\_DESCRIPTOR structure point to the paged pool that remains until the subunit driver's physical device object (PDO) is removed. Care must be taken not to destroy the contents.

    The subunit driver is permitted to replace the pointer if it has a better, or more preferable, structure to point to. However, the subunit driver must not free these memory ranges. If the subunit driver uses AVStream (instead of the Stream class), then it should use the **KsEdit** routine to replace such memory references.

    Note that *Avc.sys* does *not* fill in the KSPIN\_DESCRIPTOR's **Interfaces**, **DataRanges**, **Category**, **Name**, or **ConstrainedDataRanges** members. The subunit driver fills in these members, as well as the **IntersectHandler** and optional **Context** members (described in step 3) if the lower-filter driver, *Avcstrm.sys*, is not present.

    Regardless of the origin of the **DataRanges** member, each standard range must be paired with a duplicate range that has an [**AVCPRECONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554103) structure appended (by using the appropriate specifier GUIDs) to support both device-to-computer *and* device-to-device connections. *Avc.sys* can provide an AVCPRECONNECTINFO structure for each pin through the [**AVC\_FUNCTION\_GET\_CONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554154) request.

3.  The **IntersectHandler** routine creates a **DataFormat** structure for a matching pair of **DataRanges** structures. The intersection routine is either supplied in the result of **AVC\_FUNCTION\_GET\_PIN\_DESCRIPTOR** or provided by the subunit driver. If the subunit driver provides its own intersection handler, see [**AV/C Intersect Handler**](https://msdn.microsoft.com/library/windows/hardware/ff556379). For more information about data intersection, see [DataRange Intersections in AVStream](data-range-intersections-in-avstream.md).

    The **DataFormat** structure for matching AVCPRECONNECTINFO ranges has an [**AVCCONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554101) structure appended to it. This structure is a copy of the local pin's AVCPRECONNECTINFO structure with the **Flags** member replaced by the **hPlug** member. The **hPlug** member must remain **NULL** if the **KSPIN\_FLAG\_AVC\_PERMANENT** bit is set. If the **KSPIN\_FLAG\_AVC\_PCRONLY** or **KSPIN\_FLAG\_AVC\_FIXEDPCR** bits were set in **Flags**, the **UnitPlugNumber** and **DataFlow** members would be used to obtain an **hPlug** handle from *61883.sys*. Any other combination of bits (or no bits) means that the **hPlug** can be obtained for any available plug number (by using the **DataFlow** member to determine plug direction).

    The **IntersectHandler** routine must pass the resulting AVCCONNECTINFO structure down to *Avc.sys* (described in step 4). Passing AVCCONNECTINFO ensures that *Avc.sys* can later make any necessary plug connections within the unit itself (for example, connections between unit input or output plugs with subunit destination or source plugs).

4.  Finally, when the data format is set on a pin (after format negotiation and data intersection), the pin must examine the format for an AVCCONNECTINFO structure. If this structure is found, then the pin does not move data to or from the IEEE 1394 bus from or to the computer. Instead, it uses [**AVC\_FUNCTION\_SET\_CONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554171) to send the AVCCONNECTINFO contents to a lower driver. Potentially, both the lower-filter driver (for example, *Avcstrm.sys*) and the *Avc.sys* driver perform connection operations, but, at this point, only the AVCCONNECTINFO contents should be cached (no connection operations performed). The lower driver does not cache an AVCCONNECTINFO that it provided. In this way, only one pin makes **hPlug** connections between units. If there is no lower-filter driver, the subunit driver should decide whether to deliver the AVCCONNECTINFO to the lower driver. *Avc.sys* does not need to see AVCCONNECTINFO structures for plug control register (PCR)-only connections.

    If the subunit is not using a lower-filter driver to manage stream formats , the subunit driver sets up IEEE 1394 serial bus plug connections. For more information, see [AV/C Streaming Overview](av-c-streaming-overview.md).

    The subunit driver should cache the **hPlug** member from the format to set up a peer-to-peer connection if:

    -   The **hPlug** member does not match the one created by the subunit driver.
    -   The **DeviceID** member does not match the one that the subunit driver received in AVCPRECONNECTINFO.
    -   The **DataFlow** member does not match the data flow of the subunit's pin.

5.  When pin connection resources are to be acquired, submit an [**AVC\_FUNCTION\_ACQUIRE**](https://msdn.microsoft.com/library/windows/hardware/ff554148) request. The lower driver (or the subunit driver itself) uses any cached AVCCONNECTINFO to make the **hPlug** connections. The internal connections between subunit and unit plugs are made by *Avc.sys* upon receiving the **AVC\_FUNCTION\_ACQUIRE** request, using the cached AVCCONNECTINFO. *Avc.sys* does not cache information nor attempt internal plug connections if it has no internal plug control or the connection is marked as permanent.

6.  When pin connection resources are to be released, submit an [**AVC\_FUNCTION\_RELEASE**](https://msdn.microsoft.com/library/windows/hardware/ff554169) request. The lower driver and *Avc.sys* keep any cached AVCCONNECTINFO so that alternating *acquire* and *release* operations can be performed.

7.  Submit an [**AVC\_FUNCTION\_CLR\_CONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554149) structure to remove the cached AVCCONNECTINFO data.

Note that the **AVC\_FUNCTION\_SET\_CONNECTINFO** structure must be called once with the AVCCONNECTINFO structure that is created during data intersection (the local AVCCONNECTINFO) and once again with the AVCCONNECTINFO structure that is passed when setting the format (the foreign AVCCONNECTINFO). For connections between subunits of different devices, a filter driver (for example, *Avcstrm.sys)* caches the foreign information (the foreign **hPlug**), and *Avc.sys* caches the local information. For connections between subunits within the same device, the filter driver does not cache any information, and *Avc.sys* caches only the information for the foreign subunit. The filter driver must pass all **AVC\_FUNCTION\_SET\_CONNECTINFO** requests down to *Avc.sys*, so that it can be shielded from decision-making about the subunit plug connection .

The AV/C connection lock bit is set when it makes the connection. Output pins (source plugs) expose multiple pin instances allowing overlay connections (from the same output to an additional input). However, if overlay connections are allowed, nothing prevents a *disconnect* command from deleting all of the existing connections; this is inherent in the AV/C specification. When overlaying connections, the subunit sends multiple **AVC\_FUNCTION\_SET\_CONNECTINFO** and **AVC\_FUNCTION\_ACQUIRE** request pairs (without intervening **AVC\_FUNCTION\_RELEASE** requests). Furthermore, this same behavior can result when a second computer is introduced to the IEEE 1394 bus or a second incompatible application is run on the same computer.

AV/C external plug connections are not directly supported by *Avc.sys*, but *Avc.sys* can still establish internal connections between subunit plugs and external plugs by providing synthesized AVCCONNECTINFO structures. The subunit driver can create an AVCCONNECTINFO structure by using the [**AVC\_FUNCTION\_GET\_UNIQUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff554166) function code to fill in the **DeviceID** member, supplying the unit address 0xff and the external plug number (plug number joined with 0x80 by using the logical OR operator) for the **SubunitAddress** and **SubunitPlugNumber** members and supplying the correct data flow direction in the **DataFlow** member. The **hPlug** and **UnitPlugNumber** members should be set to **NULL**. The number of input and output external plugs can be detected through the **AVC\_FUNCTION\_GET\_EXT\_PLUG\_COUNTS** function.

An approach that allows *Avc.sys* to make the proper internal plug connections and exposes possible external plug connections to applications is to have filter factories for each possible external plug. The resulting filter instances expose an appropriate input or output pin, which in turn provides AVCCONNECTINFO structures.

 

 




