---
title: MB Analyzing Logs
description: MB Analyzing Logs
ms.date: 03/01/2021
ms.localizationpriority: medium
---

# MobileBroadband Analyzing logs

[TextAnalysisTool](https://github.com/TextAnalysisTool/Releases) is an extensive text filtering tool that is useful for complex traces with numerous ETW providers. You can filter the logs of interest using the .tat files.

To collect the logs, follow the steps in [MobileBroadband Collecting logs](mb-collecting-logs.md).

Use the .tat filters included in the specific feature to filter the logs:

```
*  Copy and paste the lines into a <name>.tat file
*  Open the log of interest in TextAnalysisTool
*  Load the filter file(<name>.tat) into TextAnalysisTool by clicking File > Load Filters
```