---
title: Security During Postmortem Debugging
description: Security During Postmortem Debugging
keywords: ["security considerations, postmortem debugging", "postmortem debugging, security considerations"]
ms.date: 11/25/2024
ms.topic: concept-article
---

# Security During Postmortem Debugging

Only an administrator can enable [postmortem debugging](enabling-postmortem-debugging.md).

However, postmortem debugging is enabled for the entire system, not just for one user. Thus, after it has been enabled, any application crash will activate the debugger that has been chosen -- even if the current user does not have administrative privileges.

Also, a postmortem debugger inherits the same privileges as the application that crashed. Thus, if a Windows service such as CSRSS and LSASS crashes, the debugger will have very high-level privileges.

You should take this into account when choosing to enable postmortem debugging.
 