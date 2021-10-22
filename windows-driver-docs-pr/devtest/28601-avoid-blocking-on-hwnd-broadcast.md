---
title: C28601 warning
description: Warning C28601 Avoid blocking on HWND_BROADCAST.
ms.date: 04/20/2017
ms.localizationpriority: medium
f1_keywords: 
  - "C28601"
---

# C28601


warning C28601: Avoid blocking on HWND\_BROADCAST

This warning indicates that the application called **SendMessage** with the **HWND\_BROADCAST** flag, which blocks the thread until all the windows to which this message was broadcast respond. However, if there is another window that is not responding, the current thread will also be blocked.

To fix this, use **PostMessage** instead, so that it is not a blocking call. Alternatively, avoid the use of **HWND\_BROADCAST** to direct the message to a particular window.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following call could cause the process to stop responding.

```
SendMessage(HWND_BROADCAST, ... );
```

 

 





