---
title: Debugging Still Image Components
description: Debugging still image components
ms.date: 04/21/2023
---

# Debugging still image components

To aid the debugging of vendor-supplied still image components, the still image event monitor's behavior can be modified with command-line options, using the **Run** option of the **Start** menu. The following options are available:

| Command line option | Definition |
|--|--|
| **stimon /h** | Hides the message window. |
| **Stimon /r** | Refreshes the event monitor's device list. |
| **Stimon /t***number* | Modifies the polling interval to the number of seconds specified by *number*. Typically used for increasing the polling interval. |
| **Stimon /v** | Makes a window visible that displays event monitor messages. |

The event monitor can be stopped and started by using the Computer Management window. The event monitor is listed as the "Still Image Service".
