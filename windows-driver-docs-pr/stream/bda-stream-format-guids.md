---
title: BDA Stream Format GUIDs
description: BDA Stream Format GUIDs
MS-HAID:
- 'bdaref\_94229f51-2313-4c81-ab77-3e28c7518376.xml'
- 'stream.bda\_stream\_format\_guids'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 216fb02c-b49b-4b9f-b7a5-220c718fb202
---

# BDA Stream Format GUIDs


## <span id="ddk_bda_stream_format_guids_ks"></span><span id="DDK_BDA_STREAM_FORMAT_GUIDS_KS"></span>


A BDA minidriver uses BDA stream format GUIDs to specify the data formats it supports. A BDA minidriver assigns these GUIDs to members of a [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structure. The *Bdamedia.h* header file defines these GUIDs. Pins of filters specify the ranges of data formats they support to connect to pins of other filters that also support those ranges.

The following stream GUIDs are available in BDA:

<span id="KSDATAFORMAT_TYPE_BDA_ANTENNA"></span><span id="ksdataformat_type_bda_antenna"></span>KSDATAFORMAT\_TYPE\_BDA\_ANTENNA  
A BDA minidriver assigns this GUID to the **MajorFormat** member of the **DataRange** member of a [**KS\_DATARANGE\_BDA\_ANTENNA**](https://msdn.microsoft.com/library/windows/hardware/ff567343) structure to enable connecting to a specific upstream filter, such as a network provider filter.

<span id="KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT"></span><span id="ksdataformat_subtype_bda_mpeg2_transport"></span>KSDATAFORMAT\_SUBTYPE\_BDA\_MPEG2\_TRANSPORT  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

<span id="KSDATAFORMAT_SPECIFIER_BDA_TRANSPORT"></span><span id="ksdataformat_specifier_bda_transport"></span>KSDATAFORMAT\_SPECIFIER\_BDA\_TRANSPORT  
A BDA minidriver assigns this GUID to the **Specifier** member of either a KSDATARANGE structure or the **DataRange** member of a [**KS\_DATARANGE\_BDA\_TRANSPORT**](https://msdn.microsoft.com/library/windows/hardware/ff567346) structure to enable connecting to a pin of a filter that also assigns this specifier.

<span id="KSDATAFORMAT_TYPE_BDA_IF_SIGNAL"></span><span id="ksdataformat_type_bda_if_signal"></span>KSDATAFORMAT\_TYPE\_BDA\_IF\_SIGNAL  
A BDA minidriver assigns this GUID to the **MajorFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this major format.

<span id="KSDATAFORMAT_TYPE_MPEG2_SECTIONS"></span><span id="ksdataformat_type_mpeg2_sections"></span>KSDATAFORMAT\_TYPE\_MPEG2\_SECTIONS  
A BDA minidriver assigns this GUID to the **MajorFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this major format.

<span id="KSDATAFORMAT_SUBTYPE_ATSC_SI"></span><span id="ksdataformat_subtype_atsc_si"></span>KSDATAFORMAT\_SUBTYPE\_ATSC\_SI  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

<span id="KSDATAFORMAT_SUBTYPE_DVB_SI"></span><span id="ksdataformat_subtype_dvb_si"></span>KSDATAFORMAT\_SUBTYPE\_DVB\_SI  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

<span id="KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_PSIP"></span><span id="ksdataformat_subtype_bda_opencable_psip"></span>KSDATAFORMAT\_SUBTYPE\_BDA\_OPENCABLE\_PSIP  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

<span id="KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_OOB_PSIP"></span><span id="ksdataformat_subtype_bda_opencable_oob_psip"></span>KSDATAFORMAT\_SUBTYPE\_BDA\_OPENCABLE\_OOB\_PSIP  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

<span id="KSDATAFORMAT_TYPE_BDA_IP"></span><span id="ksdataformat_type_bda_ip"></span>KSDATAFORMAT\_TYPE\_BDA\_IP  
A BDA minidriver assigns this GUID to the **MajorFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this major format.

<span id="KSDATAFORMAT_SUBTYPE_BDA_IP"></span><span id="ksdataformat_subtype_bda_ip"></span>KSDATAFORMAT\_SUBTYPE\_BDA\_IP  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

<span id="KSDATAFORMAT_SPECIFIER_BDA_IP"></span><span id="ksdataformat_specifier_bda_ip"></span>KSDATAFORMAT\_SPECIFIER\_BDA\_IP  
A BDA minidriver assigns this GUID to the **Specifier** member of either a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this specifier.

<span id="KSDATAFORMAT_TYPE_BDA_IP_CONTROL"></span><span id="ksdataformat_type_bda_ip_control"></span>KSDATAFORMAT\_TYPE\_BDA\_IP\_CONTROL  
A BDA minidriver assigns this GUID to the **MajorFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this major format.

<span id="KSDATAFORMAT_SUBTYPE_BDA_IP_CONTROL"></span><span id="ksdataformat_subtype_bda_ip_control"></span>KSDATAFORMAT\_SUBTYPE\_BDA\_IP\_CONTROL  
A BDA minidriver assigns this GUID to the **SubFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this sub format.

<span id="KSDATAFORMAT_TYPE_MPE"></span><span id="ksdataformat_type_mpe"></span>KSDATAFORMAT\_TYPE\_MPE  
A BDA minidriver assigns this GUID to the **MajorFormat** member of a KSDATARANGE structure to enable connecting to a pin of a filter that also assigns this major format.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20BDA%20Stream%20Format%20GUIDs%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




