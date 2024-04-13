---
title: C28645 Warning
description: Warning C28645 MessageBox was called using the question mark message symbol which is no longer recommended.
ms.date: 04/20/2017
f1_keywords: 
  - "C28645"
---

# C28645


warning C28645: MessageBox was called using the question mark message symbol which is no longer recommended

The use of the question mark message icon in a modal dialog box is no longer recommended because it does not clearly represent a specific type of message, and the phrasing of a message as a question could apply to any message type. In addition, users can confuse the message symbol question mark with Help information.

Therefore, do not use this question mark message symbol in your message boxes. The system continues to support its inclusion only for backward compatibility.

