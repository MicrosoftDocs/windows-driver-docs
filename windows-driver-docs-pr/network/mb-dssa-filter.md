---
title: DSSA Log Filter
description: TextAnalysisTool Filter for DSSA
ms.assetid: 4d575360-e867-4025-bb7d-575e1795c7e5
ms.date: 03/01/2021
---

# DSSA Log Filter

To make searching log files easier, below is a DSSA filter file for the [TextAnalysisTool](https://github.com/TextAnalysisTool/Releases). 

To use the DSSA log filter: 

1. Copy and paste the lines below and save them into a text file named "esimdownload.tat."

```
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<TextAnalysisTool.NET version="2016-06-16" showOnlyFilteredLines="True">
  <filters>
    <filter enabled="y" excluding="n" description="" backColor="add8e6" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]QUERY OID_WWAN_DEVICE_CAPS_EX" />
    <filter enabled="y" excluding="n" description="" backColor="ffb6c1" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	StatusCode	: NDIS_STATUS_WWAN_DEVICE_SLOT" />
    <filter enabled="y" excluding="n" description="" backColor="f0e68c" type="matches_text" case_sensitive="n" regex="n" text="SET OID_WWAN_SYS_SLOTMAPPINGS" />
    <filter enabled="y" excluding="n" description="" backColor="90ee90" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]QUERY OID_WWAN_SYS_CAPS" />
    <filter enabled="y" excluding="n" description="" backColor="ffb6c1" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]		Executor Index" />
    <filter enabled="y" excluding="n" description="" backColor="add8e6" type="matches_text" case_sensitive="n" regex="n" text="CAPS_MULTI_SIM" />
    <filter enabled="y" excluding="n" description="" backColor="f08080" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	StatusCode	: NDIS_STATUS_WWAN_SLOT_INFO" />
    <filter enabled="y" excluding="n" description="" backColor="f08080" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	SlotState" />
    <filter enabled="y" excluding="n" description="" backColor="90ee90" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	StatusCode	: NDIS_STATUS_WWAN_SYS_CAPS_INFO" />
    <filter enabled="y" excluding="n" description="" backColor="90ee90" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	NumberOfExecutors" />
    <filter enabled="y" excluding="n" description="" backColor="90ee90" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	NumberOfSlots" />
    <filter enabled="n" excluding="n" description="" backColor="afeeee" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	ReadyState" />
    <filter enabled="y" excluding="n" description="" backColor="add8e6" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	StatusCode	: NDIS_STATUS_WWAN_DEVICE_CAPS_EX" />
    <filter enabled="y" excluding="n" description="" backColor="f0e68c" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	SlotMapListHeader" />
    <filter enabled="y" excluding="n" description="" backColor="f0e68c" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	Executor Index" />
    <filter enabled="y" excluding="n" description="" backColor="f08080" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	SlotIndex" />
    <filter enabled="y" excluding="n" description="" backColor="dda0dd" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]QUERY OID_WWAN_SYS_SLOTMAPPINGS" />
    <filter enabled="y" excluding="n" description="" backColor="dcdcdc" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]QUERY OID_WWAN_SLOT_INFO_STATUS" />
    <filter enabled="y" excluding="n" description="" backColor="d3d3d3" type="matches_text" case_sensitive="n" regex="n" text="[WwanDimCommon]	Slot Index" />
  </filters>
</TextAnalysisTool.NET>
```

2.  Load the filter file into the TextAnalysisTool by clicking File > Load Filters.
