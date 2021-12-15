---
title: PIN Operations Log Filter
description: TextAnalysisTool Filter for PIN Operations
ms.date: 03/01/2021
---

# PIN Operations Log filter

To make searching log files easier, below is a PIN-operation-specific filter file for the [TextAnalysisTool](https://github.com/TextAnalysisTool/Releases). 

To use this filter:
 
1. Copy and paste the lines below and save them into a text file named "WwanPin.tat." 

2. Load the filter file into the TextAnalysisTool by clicking File > Load Filters.

```
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<TextAnalysisTool.NET version="2015-06-23" showOnlyFilteredLines="True">
  <filters>
    <filter enabled="n" excluding="n" backColor="90ee90" type="matches_text" case_sensitive="n" regex="n" text="maybeUnlockPin" />
    <filter enabled="n" excluding="n" foreColor="800000" type="matches_text" case_sensitive="n" regex="n" text="Received PinInfo" />
    <filter enabled="n" excluding="n" backColor="ffb6c1" type="matches_text" case_sensitive="n" regex="n" text="maybeCapturePin" />
    <filter enabled="n" excluding="n" foreColor="800080" type="matches_text" case_sensitive="n" regex="n" text="[Microsoft-Windows-WWAN-SVC-EVENTS]" />
    <filter enabled="n" excluding="n" foreColor="00008b" type="matches_text" case_sensitive="n" regex="n" text="PinAction" />
    <filter enabled="n" excluding="n" backColor="dda0dd" type="matches_text" case_sensitive="n" regex="n" text="tracePinDesc" />
    <filter enabled="n" excluding="n" foreColor="008000" type="matches_text" case_sensitive="n" regex="n" text="processPinInfoResponse" />
    <filter enabled="n" excluding="n" foreColor="0000ff" type="matches_text" case_sensitive="n" regex="n" text="processPinActionResponse" />
    <filter enabled="n" excluding="n" foreColor="dc143c" type="matches_text" case_sensitive="n" regex="n" text="processPinListResponse" />
    <filter enabled="n" excluding="n" type="matches_text" case_sensitive="n" regex="n" text="NDIS_STATUS_WWAN_PIN_INFO" />
  </filters>
</TextAnalysisTool.NET>
```
