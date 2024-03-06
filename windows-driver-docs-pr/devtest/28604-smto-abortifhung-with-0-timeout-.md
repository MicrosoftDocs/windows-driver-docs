---
title: C28604 Warning
description: Warning C28604 Avoid calling SendMessageTimeout with SMTO_ABORTIFHUNG with a timeout of 0.
ms.date: 04/20/2017
f1_keywords: 
  - "C28604"
---

# C28604


warning C28604: Avoid calling SendMessageTimeout with SMTO\_ABORTIFHUNG with a timeout of 0

The Code Analysis tool reports this warning when applications call **SendMessageTimeout** with the **SMTO\_ABORTIFHUNG** flag and a time-out period of zero. Using **SendMessageTimeout** this way can be problematic because the time-out period has no effect, and the call is treated as a blocking call.

Specify a nonzero value for time-out period.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following function call can cause the process to not respond indefinitely.

```
fNeedsCallbackEvent = (0 != SendMessageTimeout(
_hwnd, 
WM_NULL, 
0,
0, 
SMTO_ABORTIFHUNG,
0,
&dwResult)); 
```

The following function call does not have this problem.

```
fNeedsCallbackEvent = (0 != SendMessageTimeout(
_hwnd, 
WM_NULL, 
0,
0,
SMTO_ABORTIFHUNG,
1000,  
&dwResult)); 
```

