---
title: BDA Stream Format GUIDs
description: A BDA minidriver uses BDA stream format GUIDs to specify the data formats it supports.
ms.date: 10/07/2021
---

# BDA Stream Format GUIDs

A BDA minidriver uses BDA stream format GUIDs to specify the data formats it supports. A BDA minidriver assigns these GUIDs to members of a [**KSDATARANGE**](/previous-versions/ff561658(v=vs.85)) structure. The *Bdamedia.h* header file defines these GUIDs. Pins of filters specify the ranges of data formats they support to connect to pins of other filters that also support those ranges.

The following stream GUIDs are available in BDA:

**KSDATAFORMAT_TYPE_BDA_ANTENNA**  
A BDA minidriver assigns this GUID to the **MajorFormat** member of the **DataRange** member of a [**KS_DATARANGE_BDA_ANTENNA**](/windows-hardware/drivers/ddi/bdamedia/ns-bdamedia-tagks_datarange_bda_antenna) structure to enable connecting to a specific upstream filter, such as a network provider filter.

**KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT**  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

**KSDATAFORMAT_SPECIFIER_BDA_TRANSPORT**  
A BDA minidriver assigns this GUID to the **Specifier** member of either a KSDATARANGE structure or the **DataRange** member of a [**KS_DATARANGE_BDA_TRANSPORT**](/windows-hardware/drivers/ddi/bdamedia/ns-bdamedia-tagks_datarange_bda_transport) structure to enable connecting to a pin of a filter that also assigns this specifier.

**KSDATAFORMAT_TYPE_BDA_IF_SIGNAL**  
A BDA minidriver assigns this GUID to the **MajorFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this major format.

**KSDATAFORMAT_TYPE_MPEG2_SECTIONS**  
A BDA minidriver assigns this GUID to the **MajorFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this major format.

**KSDATAFORMAT_SUBTYPE_ATSC_SI**  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

**KSDATAFORMAT_SUBTYPE_DVB_SI**  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

**KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_PSIP**  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

**KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_OOB_PSIP**  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

**KSDATAFORMAT_TYPE_BDA_IP**  
A BDA minidriver assigns this GUID to the **MajorFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this major format.

**KSDATAFORMAT_SUBTYPE_BDA_IP**  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

**KSDATAFORMAT_SPECIFIER_BDA_IP**  
A BDA minidriver assigns this GUID to the **Specifier** member of either a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this specifier.

**KSDATAFORMAT_TYPE_BDA_IP_CONTROL**  
A BDA minidriver assigns this GUID to the **MajorFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this major format.

**KSDATAFORMAT_SUBTYPE_BDA_IP_CONTROL**  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

**KSDATAFORMAT_TYPE_MPE**  
A BDA minidriver assigns this GUID to the **MajorFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this major format.
