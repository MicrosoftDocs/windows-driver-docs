---
title: eSIM Profile Operations Log Filter
description: TextAnalysisTool Filter for eSIM Profile Operations
ms.date: 03/01/2021
ms.localizationpriority: medium
---

# eSIM Profile Operations Log Filter

To load an eSIM Profile Operation log filter:

1. Copy and paste the lines below and save them into a text file named "esimoperation.tat." This filter is for the "EnableProfile" operation. For other operations, replace "RpcEnableProfile" with one of the strings below that is specific to the operation.

```
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<TextAnalysisTool.NET version="2015-08-17" showOnlyFilteredLines="True">
  <filters>
    <filter enabled="y" excluding="n" description="" type="matches_text" case_sensitive="n" regex="n" text="RpcEnableProfile" />
    <filter enabled="y" excluding="n" description="" type="matches_text" case_sensitive="n" regex="n" text="OpenChannel" />
    <filter enabled="y" excluding="n" description="" type="matches_text" case_sensitive="n" regex="n" text="CloseChannel" />
    <filter enabled="y" excluding="n" description="" type="matches_text" case_sensitive="n" regex="n" text="CardResetComplete" />
    <filter enabled="y" excluding="n" description="" type="matches_text" case_sensitive="n" regex="n" text="LuiAsyncResult" />
    <filter enabled="y" excluding="n" description="" type="matches_text" case_sensitive="n" regex="n" text="WwapiEsimUpdate" />
    <filter enabled="y" excluding="n" description="" type="matches_text" case_sensitive="n" regex="n" text="SendApdu" />
  </filters>
</TextAnalysisTool.NET>
``` 

```
Enable Profile  - RpcEnableProfile
Disable Profile - RpcDisableProfile
Delete Profile  - RpcDeleteProfile
Set Nick Name   - RpcSetProfileNickname
Reset eSim      - RpcWipeEsim
```

2. Load the filter file into the TextAnalysisTool by clicking File > Load Filters. 

