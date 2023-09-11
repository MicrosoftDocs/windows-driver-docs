---
title: .scroll_prefs (Control Source Scrolling Preferences)
description: The .scroll_prefs command controls the positioning of the source in a Source window when scrolling to a line.
keywords: [".scroll_prefs (Control Source Scrolling Preferences) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .scroll_prefs (Control Source Scrolling Preferences)
api_type:
- NA
---

# .scroll\_prefs (Control Source Scrolling Preferences)


The **.scroll\_prefs** command controls the positioning of the source in a Source window when scrolling to a line.

```dbgcmd
.scroll_prefs Before After 
.scroll_prefs 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Before______"></span><span id="_______before______"></span><span id="_______BEFORE______"></span> *Before*   
Specifies how many source lines before the line you are scrolling to should be visible in the Source window.

<span id="_______After______"></span><span id="_______after______"></span><span id="_______AFTER______"></span> *After*   
Specifies how many source lines after the line you are scrolling to should be visible in the Source window.

### Environment

This command is available only in WinDbg and cannot be used in script files.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

When this command is used with no parameters, the current source scrolling preferences are displayed.

 

 





