---
title: eSIM Download and Install Log Filter
description: TextAnalysisTool Filter for eSIM Download and Install
ms.assetid: 0C812829-D91A-44FC-8BE6-F8264B13F6C7
ms.date: 03/01/2021
ms.localizationpriority: medium
---

# eSIM Download and Install Log Filter

To load an eSIM download and install log filter:

1. Copy and paste the lines below and save them into a text file named "esimdownload.tat." 

```
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<TextAnalysisTool.NET version="2015-08-17" showOnlyFilteredLines="True">
  <filters>
    <filter enabled="y" excluding="n" description="" type="matches_text" case_sensitive="n" regex="n" text="RpcDownloadProfile" />
    <filter enabled="y" excluding="n" description="" type="matches_text" case_sensitive="n" regex="n" text="LuiAsyncResult" />
    <filter enabled="y" excluding="n" description="" type="matches_text" case_sensitive="n" regex="n" text="DownloadSequenceEvent" />
  </filters>
</TextAnalysisTool.NET>
```

2. Load the filter file into the TextAnalysisTool by clicking File > Load Filters.