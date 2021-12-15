---
title: LTE Attach Operation Log Filter
description: TextAnalysisTool Filter for the LTE Attach Operation
ms.date: 03/01/2021
---
# LTE Attach Log Filter

To load a [TextAnalysisTool](mb-analyzing-logs.md) filter for the LTE Attach operation:

1. Copy and paste the lines below and save them into a text file named "lte-attach.tat." 
1. Load the filter file into the TextAnalysisTool by clicking File > Load Filters.

```
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<TextAnalysisTool.NET version="2014-04-22" showOnlyFilteredLines="True">
  <filters>
    <filter enabled="y" excluding="n" type="matches_text" case_sensitive="n" regex="n" text="SaveModemConfiguredLteAttachConfig" />
    <filter enabled="y" excluding="n" type="matches_text" case_sensitive="n" regex="n" text="[WwanProtDim] StatusCode : NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG (0x4004103d)" />
    <filter enabled="y" excluding="n" type="matches_text" case_sensitive="n" regex="n" text="WwanPmSetDMConfigProfile" />
    <filter enabled="y" excluding="n" type="matches_text" case_sensitive="n" regex="n" text="CWwanDataExecutor::OnLteAttachProfileUpdate" />
    <filter enabled="y" excluding="n" type="matches_text" case_sensitive="n" regex="n" text="ReadyState  : WwanReadyStateInitialized" />
    <filter enabled="y" excluding="n" color="ff0000" type="matches_text" case_sensitive="n" regex="n" text="WwanPmGetLteAttachProfileInEffect" />
    <filter enabled="y" excluding="n" color="0000ff" type="matches_text" case_sensitive="n" regex="n" text="IsSameLTEAttachAPN" />
    <filter enabled="y" excluding="n" type="matches_text" case_sensitive="n" regex="n" text="[WwanProtDim] ReadyState" />
    <filter enabled="n" excluding="n" type="matches_text" case_sensitive="n" regex="n" text="LTEAttachConfig" />
  </filters>
</TextAnalysisTool.NET>
```
