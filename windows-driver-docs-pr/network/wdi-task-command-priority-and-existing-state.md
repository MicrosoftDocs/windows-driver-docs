---
title: WDI task command priority and existing state
description: When the adapter is in a particular state, new commands may come down to it that could affect the existing state (for example, a scan that affects existing connections).
ms.date: 07/08/2025
---

# WDI task command priority and existing state

When the adapter is in a particular state, new commands may come down to it that could affect the existing state (for example, a scan that affects existing connections). THe following table uses these definitions

- **Important**: Prioritize the existing state higher than the new request. 
- **Maintain**: Prioritize the existing state and the new command equally.
- **Throttle**: Throttle down the servicing of the existing state so that it works, but prioritize the new command higher.
- **Pause**: Stop servicing the existing state and attempt to finish the existing state as soon as possible.

to describe how new commands should be prioritized against the existing state in the adapter. The columns describe how to service the existing state when the new command comes in.

| New Command                        | Connection Quality (EAP)<br>Priority 1 | P2P Listen<br>Priority 2 | Connection Quality Latency (Media Streaming)<br>Priority 3 | Existing Connections<br>Priority 4 |
|-------------------------------------|:--------------------------------------:|:-----------------------:|:---------------------------------------------------------:|:----------------------------------:|
| Scan/P2P Discovery (forced)         | Important (delay scan)                 | Pause                  | Pause                                                      | Throttle                          |
| Scan/P2P Discovery (not forced)     | Important (skip scan)                  | Maintain               | Important (skip scan)                                      | Throttle                          |
| Station Connect, Roam, Disconnect   | Delay Connect                          | Pause                  | Pause                                                      | Throttle                          |
| P2P GO Start, GO Stop               | Delay Connect                          | Pause                  | Pause                                                      | Throttle                          |
| P2P Client Connect, Disconnect      | Delay Connect                          | Pause                  | Pause                                                      | Throttle                          |
| P2P Send Action Response            | Pause                                  | Pause                  | Pause                                                      | Throttle                          |
| P2P Send Action Request             | Delay Send                             | Maintain               | Pause                                                      | Throttle                          |

 

 

 





